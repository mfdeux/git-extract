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