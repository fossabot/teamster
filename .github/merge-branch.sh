#!/bin/bash

git switch dev

for BRANCH in ./teamster/kipp*/; do
	branch_name=$(basename -- "${BRANCH}")

	git merge origin/"${branch_name}" ./teamster/"${branch_name}"
done
