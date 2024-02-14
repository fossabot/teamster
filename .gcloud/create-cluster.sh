#!/bin/bash
# https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#authenticating_to

project_id=teamster-332318
service_account_name=user-cloud-dagster-cloud-agent
service_account=${service_account_name}@${project}.iam.gserviceaccount.com

kubectl create namespace dagster-cloud

# Create an IAM service account for your application
# or use an existing IAM service account instead.
gcloud iam service-accounts create \
  "${service_account_name}" \
  --project="${project_id}"

# Ensure that your IAM service account has the roles you need.
# You can grant additional roles using the following command:
gcloud projects add-iam-policy-binding \
  "${project_id}" \
  --role "roles/storage.admin" \
  --member "serviceAccount:${service_account}"

# Allow the Kubernetes service account to impersonate the IAM service account
# by adding an IAM policy binding between the two service accounts.
# This binding allows the Kubernetes service account to act as the IAM service account.
gcloud iam service-accounts add-iam-policy-binding \
  "${service_account}" \
  --role roles/iam.workloadIdentityUser \
  --member "serviceAccount:${project_id}.svc.id.goog[dagster-cloud/${service_account_name}]"

# set up Workload Identity Federation for GitHub actions
# create WI pool
gcloud iam workload-identity-pools create \
  "github-pool" \
  --project="teamster-332318" \
  --location="global" \
  --display-name="GitHub Pool"

# create WI provider for pool
gcloud iam workload-identity-pools providers create-oidc \
  "github-provider" \
  --project="${project_id}" \
  --location="global" \
  --display-name="GitHub Provider" \
  --workload-identity-pool="github-pool" \
  --issuer-uri="https://token.actions.githubusercontent.com" \
  --attribute-mapping="google.subject=assertion.sub,attribute.actor=assertion.actor,attribute.repository=assertion.repository"

# bind service account to WI pool
gh_org_name=$(gh repo view --json owner --jq '.owner.login')

gcloud iam service-accounts add-iam-policy-binding \
  "${service_account}" \
  --project="${project_id}" \
  --role="roles/iam.workloadIdentityUser" \
  --member="principalSet://iam.googleapis.com/projects/624231820004/locations/global/workloadIdentityPools/github-pool/attribute.repository/${gh_org_name}/teamster"

# Annotate the Kubernetes service account
# with the email address of the IAM service account.
kubectl annotate serviceaccount \
  "${service_account}" \
  --namespace=dagster-cloud \
  "iam.gke.io/gcp-service-account=${service_account}"

kubectl create secret generic \
  dagster-cloud-agent-token \
  --save-config \
  --dry-run=client \
  --namespace=dagster-cloud \
  --from-literal=DAGSTER_CLOUD_AGENT_TOKEN="${DAGSTER_CLOUD_AGENT_TOKEN}" \
  --output=yaml |
  kubectl apply -f - ||
  true
