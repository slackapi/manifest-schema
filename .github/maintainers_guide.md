# Maintainers Guide

## Python

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

### Linting

```zsh
# Run flake8 from root directory for linting
flake8 tests/

# Run black from root directory for code formatting
black .
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
./scripts/run_tests.sh
```

#### Production Deployment

1. Create the commit for the release:
   - Commit with a message including the new version number. For example `1.2.3` & Push the commit to a branch and create a PR to sanity check.
     - `git checkout -b v1.2.3-release`
     - `git commit -m 'version 1.2.3'`
     - `git push {your-fork} v1.2.3-release`
   - Merge in release PR after getting an approval from at least one maintainer.
   - Create a git tag for the release. For example `git tag v1.2.3`.
   - Push the tag up to github with `git push origin --tags`

2. Distribute the release
   - Use the latest stable Python runtime
   - `python -m venv .venv`
   - `./scripts/deploy_to_pypi_org.sh`
   - Create a GitHub release - <https://github.com/slackapi/bolt-python/releases>

   ```markdown
   ## New Features

   ### Awesome Feature 1

   Description here.

   ### Awesome Feature 2

   Description here.

   ## Changes

   * #123 Make it better - thanks @SlackHQ
   * #123 Fix something wrong - thanks @seratch
   ```

## Everything else

When in doubt, find the other maintainers and ask.
