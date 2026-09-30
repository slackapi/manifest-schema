#!/bin/bash
# ./scripts/format.sh

script_dir=$(dirname $0)
cd ${script_dir}/.. && \
  ruff check --fix tests/ && \
  ruff format tests/ && \
  npx prettier --write schemas/**/*.json *.json tests/**/*.json
