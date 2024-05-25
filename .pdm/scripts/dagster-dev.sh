#!/bin/bash

if [[ -z ${1} ]]; then
  dagster dev \
    -m teamster.kippcamden \
    -m teamster.kippmiami \
    -m teamster.kippnewark \
    -m teamster.kipptaf
else
  dagster dev -m teamster."${1}"
fi
