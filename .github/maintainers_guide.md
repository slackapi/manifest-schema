# Maintainers Guide

This document describes tools, tasks and workflow that one needs to be familiar with in order to effectively maintain
this project. If you use this package within your own software as is but don't plan on modifying it, this guide is
**not** for you.

## Tools

### Python

We recommend using [pyenv](https://github.com/pyenv/pyenv) for Python runtime management. If you use macOS, follow the following steps:

```bash
brew update
brew install pyenv
```

Install necessary Python runtimes for development/testing. You can rely on Travis CI builds for testing with various major versions. <https://github.com/slackapi/bolt-python/blob/main/.travis.yml>

```bash
pyenv install -l | grep -v "-e[conda|stackless|pypy]"

pyenv install 3.10.7 # select the latest patch version
pyenv local 3.10.7

pyenv versions
   system
   3.7.13
 * 3.10.7 (set by /path-to-bolt-python/.python-version)

pyenv rehash
```

Then, you can create a new Virtual Environment this way:

```bash
python -m venv env_3.10.7
source env_3.10.7/bin/activate
```

### JSON

You need a supported version of [Node.js](https://nodejs.org/en/) (see `package.json` field "engines") and `npx` (which is distributed with Node.js).

This project contains an [`.editorconfig`](../.editorconfig) file. It is used by [Prettier](https://prettier.io/) to lint and format the JSON files

### Linting & Formatting

```zsh
# Run flake8 & prettier from root directory for linting
./scripts/lint.sh

# Run black & prettier from root directory for code formatting
./scripts/format.sh
```

## Testing

Ensure the virtual environment is activated and dependencies are installed before running scripts:

```bash
source .venv/bin/activate
pip install -U -e .
```

### Run All the Unit Tests

If you make some changes to this SDK, please write corresponding unit tests as much as possible. You can easily run all the tests by running the following script.

If this is your first time to run tests, although it may take a bit long time, running the following script is the easiest.

```bash
./scripts/install_all_and_run_tests.sh
```

Once you installed all the required dependencies, you can use the following one.

```bash
./scripts/test.sh
```

## Production Deployment

> Note: The [`manifest.schema.json`](https://github.com/slackapi/manifest-schema/blob/main/manifest.schema.json) file on the `main` branch is production!

When it's time to release find the [release candidate PR](https://github.com/slackapi/manifest-schema/pulls?q=is%3Apr+label%3Arelease+is%3Aopen) with generated changes.

Ensure [commits](https://github.com/slackapi/manifest-schema/commits/main) since the [most recent tag](https://github.com/slackapi/manifest-schema/tags) include the correct [semantic version](http://semver.org/) labels and match the proposed version.

Approve and merge these changes to publish the next release.

## Everything else

When in doubt, find the other maintainers and ask.
