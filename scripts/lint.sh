#!/bin/bash
# ./scripts/run_flake8.sh

script_dir=$(dirname $0)
cd ${script_dir}/.. && \
  flake8 tests/ && \
  npx prettier --check schemas/**/*.json *.json tests/**/*.json
