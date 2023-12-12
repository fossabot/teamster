import time

import google.auth
import gspread
from dagster import ConfigurableResource, InitResourceContext
from dagster._utils.backoff import backoff
from googleapiclient import discovery, errors
from gspread.utils import rowcol_to_a1
from pydantic import PrivateAttr


class GoogleDirectoryResource(ConfigurableResource):
    customer_id: str
    service_account_file_path: str = None
    delegated_account: str = None
    version: str = "v1"
    scopes: list = [
        "https://www.googleapis.com/auth/admin.directory.user",
        "https://www.googleapis.com/auth/admin.directory.group",
        "https://www.googleapis.com/auth/admin.directory.rolemanagement",
        "https://www.googleapis.com/auth/admin.directory.orgunit",
    ]
    max_results: int = 500

    _service: discovery.Resource = PrivateAttr()

    def setup_for_execution(self, context: InitResourceContext) -> None:
        if self.service_account_file_path is not None:
            credentials, project_id = google.auth.load_credentials_from_file(
                filename=self.service_account_file_path, scopes=self.scopes
            )

            credentials = credentials.with_subject(self.delegated_account)
        else:
            credentials, project_id = google.auth.default(scopes=self.scopes)

        self._service = discovery.build(
            serviceName="admin",
            version=f"directory_{self.version}",
            credentials=credentials,
        )

    def _list(self, api_name, **kwargs):
        data = []
        next_page_token = None

        response_data_key = kwargs.pop("response_data_key", api_name)
        max_results = kwargs.pop("max_results", self.max_results)

        while True:
            response = (
                getattr(self._service, api_name)()
                .list(pageToken=next_page_token, maxResults=max_results, **kwargs)
                .execute()
            )

            next_page_token = response.get("nextPageToken")
            data.extend(response[response_data_key])

            self.get_resource_context().log.debug(f"Retrieved {len(data)} records")

            if next_page_token is None:
                break

        return data

    def list_orgunits(
        self, org_unit_path=None, org_unit_type=None, customer_id=None, **kwargs
    ):
        return (
            self._service.orgunits()
            .list(
                customerId=(customer_id or self.customer_id),
                orgUnitPath=org_unit_path,
                type=org_unit_type,
                **kwargs,
            )
            .execute()
        )

    def get_orgunit(self, org_unit_path, customer_id=None, **kwargs):
        return (
            self._service.orgunits()
            .get(
                customerId=(customer_id or self.customer_id),
                orgUnitPath=org_unit_path,
                **kwargs,
            )
            .execute()
        )

    def list_users(self, **kwargs):
        return self._list(
            "users", customer=kwargs.get("customer", self.customer_id), **kwargs
        )

    def get_user(self, user_key, **kwargs):
        return self._service.users().get(userKey=user_key, **kwargs).execute()

    def list_groups(self, **kwargs):
        return self._list(
            "groups", customer=kwargs.get("customer", self.customer_id), **kwargs
        )

    def list_members(self, group_key, **kwargs):
        return self._list("members", groupKey=group_key, **kwargs)

    def list_roles(self, **kwargs):
        return self._list(
            "roles",
            customer=kwargs.get("customer", self.customer_id),
            max_results=kwargs.get("max_results", 100),
            response_data_key="items",
            **kwargs,
        )

    def list_role_assignments(self, **kwargs):
        return self._list(
            "roleAssignments",
            customer=kwargs.get("customer", self.customer_id),
            max_results=kwargs.get("max_results", 200),
            response_data_key="items",
            **kwargs,
        )

    def insert_user(self, body):
        return self._service.users().insert(body=body).execute()

    def update_user(self, user_key, body):
        return self._service.users().update(userKey=user_key, body=body).execute()

    @staticmethod
    def _batch_list(list, size):
        """via https://stackoverflow.com/a/312464"""
        for i in range(0, len(list), size):
            yield list[i : i + size]

    @staticmethod
    def backoff_delay_generator():
        i = 1
        while True:
            yield i
            i = i * 2

    def batch_insert_users(self, users):
        def callback(request_id, response, exception):
            context = self.get_resource_context()

            if exception is not None:
                context.log.error(exception)
                if exception.status_code == 403:
                    raise exception
                elif exception.status_code == 409 and exception.reason not in [
                    "Entity already exists.",
                    "Invalid Given/Family Name: GivenName",
                ]:
                    raise exception
            else:
                context.log.info(
                    msg=(
                        f"CREATED {response['primaryEmail']}: "
                        f"{response['name'].get('givenName')} "
                        f"{response['name'].get('familyName')} "
                        f"OU={response['orgUnitPath']} "
                        f"changepassword={response['changePasswordAtNextLogin']}"
                    )
                )

        # You cannot create more than 10 users per domain per second using the
        # Directory API
        # https://developers.google.com/admin-sdk/directory/v1/limits#api-limits-and-quotas
        batches = self._batch_list(list=users, size=10)

        for i, batch in enumerate(batches):
            self.get_resource_context().log.info(f"Processing batch {i + 1}")

            batch_request = self._service.new_batch_http_request(callback=callback)

            for user in batch:
                batch_request.add(self._service.users().insert(body=user))

            backoff(fn=batch_request.execute, retry_on=(errors.HttpError,))

            time.sleep(1)

    def batch_update_users(self, users):
        def callback(request_id, response, exception):
            context = self.get_resource_context()

            if exception is not None:
                context.log.error(exception)
                if exception.status_code in [403, 409]:
                    raise exception
            else:
                context.log.info(
                    msg=(
                        f"UPDATED {response['primaryEmail']}: "
                        f"{response['name'].get('givenName')} "
                        f"{response['name'].get('familyName')} "
                        f"OU={response['orgUnitPath']} "
                        f"suspended={response['suspended']}"
                    )
                )

        # Queries per minute per user == 2400 (40/sec)
        batches = self._batch_list(list=users, size=40)

        for i, batch in enumerate(batches):
            self.get_resource_context().log.info(f"Processing batch {i + 1}")

            batch_request = self._service.new_batch_http_request(callback=callback)

            for user in batch:
                batch_request.add(
                    self._service.users().update(
                        userKey=user["primaryEmail"], body=user
                    )
                )

            backoff(fn=batch_request.execute, retry_on=(errors.HttpError,))

            time.sleep(1)

    def batch_insert_members(self, members):
        context = self.get_resource_context()

        def callback(request_id, response, exception):
            context = self.get_resource_context()

            if exception is not None:
                context.log.error(exception)
                if exception.status_code == 403:
                    raise exception
                elif (
                    exception.status_code == 409
                    and exception.reason != "Member already exists."
                ):
                    raise exception

        # Queries per minute per user == 2400 (40/sec)
        batches = self._batch_list(list=members, size=40)

        for i, batch in enumerate(batches):
            self.get_resource_context().log.info(f"Processing batch {i + 1}")

            batch_request = self._service.new_batch_http_request(callback=callback)

            for member in batch:
                context.log.info(f"ADDING {member['email']} to {member['groupKey']}")
                batch_request.add(
                    self._service.members().insert(
                        groupKey=member["groupKey"], body=member
                    )
                )

            backoff(fn=batch_request.execute, retry_on=(errors.HttpError,))

            time.sleep(1)

    def batch_insert_role_assignments(self, role_assignments, customer=None):
        def callback(request_id, response, exception):
            context = self.get_resource_context()

            if exception is not None:
                context.log.error(exception)
                if exception.status_code == 403:
                    raise exception
                elif (
                    exception.status_code == 409
                    and exception.reason
                    != "Role assignment already exists for the role"
                ):
                    raise exception

        batches = self._batch_list(list=role_assignments, size=10)

        for i, batch in enumerate(batches):
            self.get_resource_context().log.info(f"Processing batch {i + 1}")

            batch_request = self._service.new_batch_http_request(callback=callback)

            for role_assignment in batch:
                batch_request.add(
                    self._service.roleAssignments().insert(
                        customer=(customer or self.customer_id),
                        body=role_assignment,
                    )
                )

            backoff(
                fn=batch_request.execute,
                retry_on=(errors.HttpError,),
                delay_generator=self.backoff_delay_generator(),
            )

            time.sleep(1)


class GoogleFormsResource(ConfigurableResource):
    service_account_file_path: str = None
    version: str = "v1"
    scopes: list = [
        "https://www.googleapis.com/auth/forms.body.readonly",
        "https://www.googleapis.com/auth/forms.responses.readonly",
    ]

    _service: discovery.Resource = PrivateAttr()

    def setup_for_execution(self, context: InitResourceContext) -> None:
        if self.service_account_file_path is not None:
            credentials, project_id = google.auth.load_credentials_from_file(
                filename=self.service_account_file_path, scopes=self.scopes
            )
        else:
            credentials, project_id = google.auth.default(scopes=self.scopes)

        self._service = discovery.build(
            serviceName="forms", version=self.version, credentials=credentials
        ).forms()

    def get_form(self, form_id):
        return self._service.get(formId=form_id).execute()

    def list_responses(self, form_id, **kwargs):
        return self._service.responses().list(formId=form_id, **kwargs).execute()


class GoogleSheetsResource(ConfigurableResource):
    service_account_file_path: str = None

    _client: gspread.Client = PrivateAttr()

    def setup_for_execution(self, context: InitResourceContext) -> None:
        if self.service_account_file_path is not None:
            self._client = gspread.service_account(
                filename=self.service_account_file_path
            )
        else:
            credentials, project_id = google.auth.default(
                scopes=[
                    "https://www.googleapis.com/auth/spreadsheets",
                    "https://www.googleapis.com/auth/drive",
                ]
            )

            self._client = gspread.authorize(credentials=credentials)

    def open(self, **kwargs):
        kwargs_keys = kwargs.keys()

        if "title" in kwargs_keys:
            return self._client.open(**kwargs)
        elif "sheet_id" in kwargs_keys:
            return self._client.open_by_key(key=kwargs["sheet_id"])
        elif "url" in kwargs_keys:
            return self._client.open_by_url(**kwargs)

    def open_or_create_sheet(self, **kwargs):
        try:
            spreadsheet = self.open(**kwargs)
        except gspread.exceptions.SpreadsheetNotFound as e:
            context = self.get_resource_context()

            context.log.warning(e)
            context.log.info("Creating new Sheet")

            spreadsheet = self._client.create(**kwargs)

        return spreadsheet

    @staticmethod
    def rowcol_to_a1(row, col):
        return rowcol_to_a1(row=row, col=col)