"Find all files with a specific extention."

import os
from pathlib import Path

from src.constants import EXTENTIONS


def find_files_in_directory(
    directory: str | Path, *, extentions: tuple[str] | None = None
) -> list[str | Path]:
    """Find all files into a specific directory

    Args:
        - directory (str| Path):
            Give the current dircetory where we want to find the files.
        - extentions (tuple[str] | None): All the possible extentions.

    Returns:
        (list[str | Path]): All the available files on the given directory.
    """
    extentions = extentions if extentions is not None else EXTENTIONS
    files_and_dirs = os.listdir(os.path.abspath(directory))
    files: list[str | Path] = []
    for obj in files_and_dirs:
        path_filename = os.path.abspath(Path(directory, obj))
        if os.path.isfile(path_filename) and path_filename.endswith(
            extentions
        ):
            files.append(path_filename)
    return files
