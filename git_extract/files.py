import os
import shutil
import tempfile
import typing
from pathlib import Path

import git
from git import RemoteProgress


def download_git_repo(repo: str):
    """
    Download remote git repo
    """
    local_filename = repo.split("/")[-1]

    class CloneProgress(RemoteProgress):
        def update(self, op_code, cur_count, max_count=None, message=""):
            if message:
                print(message)

    td = tempfile.mkdtemp()
    repo_local_path = os.path.join(td, local_filename)

    git.Repo.clone_from(
        repo, repo_local_path, branch="master", progress=CloneProgress(), depth=1
    )
    return repo_local_path


def find_files_in_dir(
        path: str, patterns: typing.List[str] = None, recursive: bool = False
) -> typing.List[Path]:
    """
    Find specified files in directory

    """
    if not patterns:
        patterns = ['*']

    base_dir = Path(path)
    files = []

    for pattern in patterns:
        if recursive:
            for found_file in base_dir.rglob(pattern):
                if found_file.is_file():
                    files.append(found_file)
        else:
            for found_file in base_dir.glob(pattern):
                if found_file.is_file():
                    files.append(found_file)

    return files


def find_dirs_in_dir(
        path: str, patterns: typing.List[str] = None, recursive: bool = False
) -> typing.List[Path]:
    """
    Find specified files in directory

    """
    if not patterns:
        patterns = ['*']

    base_dir = Path(path)
    dirs = []

    for pattern in patterns:
        if recursive:
            for found_dir in base_dir.rglob(pattern):
                if found_dir.is_dir():
                    dirs.append(found_dir)
        else:
            for found_dir in base_dir.glob(pattern):
                if found_dir.is_dir():
                    dirs.append(found_dir)

    return dirs


def remove_dir(path: str):
    shutil.rmtree(path)


def copy_file(src: typing.Union[str, Path], dest: str, create_dest: bool = True):
    dest_path = Path(dest)
    if create_dest:
        dest_path.mkdir(parents=True, exist_ok=True)
    else:
        if not dest_path.exists():
            raise Exception('destination directory does not exist')
    shutil.copy(src, dest)


def copy_dir(src: typing.Union[str, Path], dest: str, create_dest: bool = True):
    dest_path = Path(dest)
    new_dest_dir = os.path.join(dest, os.path.basename(src))
    if create_dest:
        dest_path.mkdir(parents=True, exist_ok=True)
    else:
        if not dest_path.exists():
            raise Exception('destination directory does not exist')
    shutil.copytree(src, new_dest_dir, dirs_exist_ok=True)
