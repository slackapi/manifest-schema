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
