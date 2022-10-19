#!/bin/bash
# Run all the tests or a single test
# all: ./scripts/run_tests.sh
# single: ./scripts/run_tests.sh tests/test_manifest_schema.py

script_dir=`dirname $0`
cd ${script_dir}/..

test_target="$1"

if [[ $test_target != "" ]]
then
  black tests/ && \
    pytest -vv $1
else
  black tests/ && pytest -vv
fi
