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

**NOTE**: The `main` branch is production!

1. <a id="step1"></a>Create a tag for your potential release
   - Your tag name will Bump the version number in adherence to [Semantic Versioning](http://semver.org/) of the previous tags
   - For example `1.2.3`, from your current branch:
     - `git tag v1.2.3`
     - `git push origin --tags`
2. Update the `$ref` fields in your JSON schemas to the files in the tag.
   - For each `$ref` field your changes affect update the value with the `raw.githubusercontent.com` of the tagged file, example:

     ```json
     {
        "$ref": "https://raw.githubusercontent.com/slackapi/manifest-schema/v1.2.3/schemas/manifest.schema.1.0.0.json"
     }
     ```

   - Commit with a message including the new version number. For example `1.2.3` & Push the commit to your branch
   - `git commit -m 'version 1.2.3'`
   - `git push origin {your-branch}`

3. Create a PR with `main`
   - Ensure all tests pass!
   - For changes based on feedback
     - Delete created tag
       - `git tag -d v1.2.3`
       - `git push origin --delete v1.2.3`
     - Make commit changes to branch
     - Repeat from [step 1](#step1).
   - Merge in release PR after getting an approval from at least one maintainer.
4. Your changes are now live on
   <https://raw.githubusercontent.com/slackapi/manifest-schema/main/schemas/manifest.schema.json>

## Everything else

When in doubt, find the other maintainers and ask.
