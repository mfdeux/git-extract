# git-extract

Extract files or directories from a git repository


## Installation

```shell script
$ pip install git-extract --upgrade
```

## Usage

```shell script
$ git-extract file https://github.com/mfdeux/git-extract --pattern "*.md" --pattern "*.py" --dest ~/Downloads/test --recursive
```

```shell script
$ git-extract dir https://github.com/mfdeux/git-extract --pattern "test" --dest ~/Downloads/test --recursive
```