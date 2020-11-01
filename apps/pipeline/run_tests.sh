#!/usr/bin/env bash

docker-compose run videoingester sh -c '
black --check --line-length 120 . /tests \
&& mypy --ignore-missing-imports . \
&& bandit -q -r . \
&& /wait \
&& python -m pytest /tests/ --junitxml=/tests/test-reports/pytest/results.xml'