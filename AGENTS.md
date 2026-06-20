# AGENTS.md

## Project Overview

Public JSON schemas defining Slack's `manifest.json` file structure. Used by IDEs to provide validation and autocomplete when developers edit `manifest.json` files.

## Commands

```bash
# Create and activate a virtual environment (first time only)
python -m venv .venv
source .venv/bin/activate

# Install dependencies (first time or after changes)
pip install -U -e .

# Run all tests
./scripts/test.sh

# Run a single test file
./scripts/test.sh tests/test_manifest_v2_schema.py

# Lint (flake8 for Python, Prettier for JSON)
./scripts/lint.sh

# Format (black for Python, Prettier for JSON)
./scripts/format.sh
```

## Architecture

The root `manifest.schema.json` is a version router — it uses `oneOf` to dispatch to versioned schemas based on `_metadata.major_version`. When the version is absent or unset, it defaults to v1.

Versioned schemas live in `schemas/` (e.g., `manifest.schema.1.0.0.json`, `manifest.schema.2.0.0.json`). These are self-contained files with inline `definitions` — no external `$ref` beyond the version routing in the root schema.

Tests validate manifests against the schema using `jsonschema.validate()`. Each version has `manifest.valid.json` and `manifest.invalid.json` fixtures under `tests/manifests/v{1,2}/`.

## Style

- Python: black, line length 100, flake8
- JSON: Prettier, 2-space indent, LF line endings (see `.editorconfig`)
- Schema `properties` keys are sorted alphabetically. Add new keys in their alphabetical position; reviewers should reject diffs that append to the end.
- Tests use pytest with `GIVEN/WHEN/THEN` comment structure

## Release Process

Releases tag `$ref` URLs to a specific version (e.g., `raw.githubusercontent.com/.../v1.2.3/schemas/...`). The `main` branch is production — the root schema URL always points to `main`.
