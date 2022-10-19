#!/bin/bash
# Run all the tests or a single test
# all: ./scripts/install_all_and_run_tests.sh
# single: ./scripts/install_all_and_run_tests.sh tests/test_manifest_schema.py

script_dir=`dirname $0`
cd ${script_dir}/..

test_target="$1"

pip install -e .

if [[ $test_target != "" ]]
then
  pip install -U -r requirements.txt && \
    black tests/ && \
    pytest $1
else
  pip install -U -r requirements.txt && \
    black tests/ && \
    pytest
fi
