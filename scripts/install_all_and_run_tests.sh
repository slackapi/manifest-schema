#!/bin/bash
# Run all the tests or a single test
# all: ./scripts/install_all_and_run_tests.sh
# single: ./scripts/install_all_and_run_tests.sh tests/test_manifest_schema.py

script_dir=`dirname $0`
cd ${script_dir}/..

test_target="$1"

pip install -U -e .

if [[ $test_target != "" ]]
then
  black tests/ && \
    npx prettier --write schemas/**/*.json *.json tests/**/*.json && \
    pytest $1
else
  black tests/ && \
    npx prettier --write schemas/**/*.json *.json tests/**/*.json && \
    pytest
fi
