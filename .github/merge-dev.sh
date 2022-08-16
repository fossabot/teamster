#!/bin/bash

for BRANCH in ./teamster/kipp*/; do
	branch_name=$(basename -- "${BRANCH}")

	git switch "${branch_name}"
	git merge dev
done

git switch dev
