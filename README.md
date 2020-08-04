# git-extract

Extract files or directories from a git repository


## Installation

```shell script
$ pip install git-extract --upgrade
```

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