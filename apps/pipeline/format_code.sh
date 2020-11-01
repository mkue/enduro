#!/usr/bin/env bash

docker-compose run videoingester sh -c ' \
autopep8 --recursive  --in-place --aggressive . /tests \
&& black --line-length 120 . /tests \
&& autoflake --recursive --in-place --remove-unused-variables --remove-all-unused-imports --expand-star-imports . /tests'
