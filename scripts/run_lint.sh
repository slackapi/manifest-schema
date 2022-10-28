#!/bin/bash
# ./scripts/run_flake8.sh

script_dir=$(dirname $0)
cd ${script_dir}/.. && \
  pip install "flake8==5.0.4" && \
  flake8 tests/ && \
  npx prettier --check schemas/**/*.json *.json tests/**/*.json
