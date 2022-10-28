#!/bin/bash
# ./scripts/run_flake8.sh

script_dir=$(dirname $0)
cd ${script_dir}/.. && \
  black tests/ && \
  npx prettier --write schemas/**/*.json *.json tests/**/*.json
