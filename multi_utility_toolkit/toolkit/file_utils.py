"""
File Operations Custom Module

This module provides functions to:
- Create files
- Write files
- Read files
- Append files
"""

from pathlib import Path


def _get_path(filename):
    """
    Convert filename into a Path object.
    """

    filename = filename.strip()

    if not filename:

        raise ValueError(
            "Filename cannot be empty."
        )

    return Path(filename)


def create_file(filename):
    """
    Create a new empty file.
    """

    path = _get_path(
        filename
    )

    path.touch(
        exist_ok=False
    )


def write_file(
    filename,
    data
):
    """
    Write data to a file.

    Existing content will be replaced.
    """

    path = _get_path(
        filename
    )

    path.write_text(
        data,
        encoding="utf-8"
    )


def read_file(filename):
    """
    Read and return file content.
    """

    path = _get_path(
        filename
    )

    return path.read_text(
        encoding="utf-8"
    )


def append_file(
    filename,
    data
):
    """
    Append data to an existing file.
    """

    path = _get_path(
        filename
    )

    with path.open(
        "a",
        encoding="utf-8"
    ) as file:

        file.write(data)