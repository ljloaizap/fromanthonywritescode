# From AnthonyWritesCode
This repo is my journey coding along with Anthony using his content available in [AnthonyWritesCode Youtube Channel](https://www.youtube.com/@anthonywritescode)

# Explains

## Pytest
1. **Fixture**: functions that run before each test function to which it is applied. They are used to feed some data to the tests such as database connections, URLs, etc. Go to `explains/_487_pytest_fixtures.py` module.
1. **Parametrize:** useful to run same tests with different set of values to run multiple cases. Go to `explains/_27_pytest_parametrize.py` module.
1. **Testing exceptions:** used when need to test that source code raises a specific exception type. Also includes testing the output (exception args). Go to `explains/_176_pytest_exceptions.py` module.
1. **Testing output:** need to test if output (printed in console) is what is expected. Go to `explains/_246_pytest_output.py` module.
1. **Testing _lru_cache_ functions**: _lru_cache_ functions could cause unexpected behavior in unit tests due to cached values. Go to `explains/_94_pytest_functools_lru_cache.py` module.
1. **Testing cli**: testing CLI output with pytest. Go to `explains/_1_pytest_cli.py` module.

## Cache
1. **@functools.lru_cache decorator:** You can cache the results of a function and play with the cache size according to the needs. Go to `explains/_54_functools_lru_cache.py` module.


# Utilities

## Useful packages
- _anthonywritescode_, `explains` [Github repo](https://github.com/anthonywritescode/explains).
- `mypy` -> [link](https://pypi.org/project/mypy/)

## Useful commands
### Python
- **pytest**
    + Run a specific test case: `pytest {file_name.py} -k {test_case_name}`
    + Run tests with print output: `pytest {file_name.py} -s`

### Linux
- `hash`: see latest commands with their location
- `!$`: will give you the last argument to the previous command.
    + `set -o history`
    + `set -o histexpand`
    + `date`
    + `echo !$ # prints date`
- `$?`: returns execution status of last execute command. Any non-zero value signifies failure.
- `{command} | less`, and later `/` to search for a string, e.g., `python --help | less` and then, `/ {search phrase}`

# :evergreen_tree: Dev jungle
1. Install requirements
    > `pipenv install -r requirements.txt`
1. Run tests suite
    > `pytest`
1. Run type checker with _mypy_ package
    > `mypy all_code_sucks && mypy -p explains && mypy -p tests`
1. **Tests coverage** 🧪
    > 
    ```
    coverage run -m pytest
    coverage report
    coverage html
    ```
