#!/bin/bash
# ./scripts/lint.sh

script_dir=$(dirname $0)
cd ${script_dir}/.. && \
  ruff check tests/ && \
  ruff format --check tests/ && \
  npx prettier --check schemas/**/*.json *.json tests/**/*.json
