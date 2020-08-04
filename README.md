[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)
[![PyPI version fury.io](https://badge.fury.io/py/git-extract.svg)](https://pypi.org/project/git-extract/)

# git-extract

Extract files or directories from a git repository


## Installation

```shell script
$ pip install git-extract --upgrade
```
[Official PyPi Repository]((https://pypi.org/project/git-extract/))

## Usage

Extract files with multiple patterns:
```shell script
$ git-extract file https://github.com/mfdeux/git-extract --pattern "*.md" --pattern "*.py" --dest ~/Downloads/test --recursive
```

Extract directory with pattern:
```shell script
$ git-extract dir https://github.com/mfdeux/git-extract --pattern "tests" --dest ~/Downloads/test
```

## Patterns

Multiple patterns are acceptable -- as many as you want!

You can think of patterns as filters.  When git-extract is looking throughout the git repository, it will match files or directories based on the patterns supplied.

All patterns are based on standard Python glob patterns.

You can read more about how to construct the patterns at:
[https://docs.python.org/3/library/glob.html](https://docs.python.org/3/library/glob.html)