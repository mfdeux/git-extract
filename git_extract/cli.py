import typing

import click

from .files import copy_dir, copy_file, download_git_repo, find_dirs_in_dir, find_files_in_dir, remove_dir


@click.group()
def cli():
    """
    Extract files and directories from remote git repo
    """
    pass


@cli.command()
@click.argument("repo", nargs=1)
@click.option("--pattern", multiple=True, help="Glob patterns to extract from repo")
@click.option("--dest", type=click.Path(exists=False), help="Destination directory")
@click.option(
    "--recursive/--no-recursive", default=False, help="Whether the search is recursive"
)
def file(repo: str, pattern: typing.List[str], dest: str, recursive: bool):
    """
    Extract one or more files from a git repository
    """
    path = download_git_repo(repo)
    files = find_files_in_dir(path, pattern, recursive=recursive)
    for found_file in files:
        copy_file(found_file, dest)
    remove_dir(path)


@cli.command()
@click.argument("repo", nargs=1)
@click.option("--pattern", multiple=True, help="Glob patterns to extract from repo")
@click.option("--dest", type=click.Path(exists=False), help="Destination directory")
@click.option(
    "--recursive/--no-recursive", default=False, help="Whether the search is recursive"
)
def dir(repo: str, pattern: typing.List[str], dest: str, recursive: bool):
    """
    Extract one or more directories from a git repository
    """
    path = download_git_repo(repo)
    dirs = find_dirs_in_dir(path, pattern, recursive=recursive)
    for found_dir in dirs:
        copy_dir(found_dir, dest)
    remove_dir(path)
