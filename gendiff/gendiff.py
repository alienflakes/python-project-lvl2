"""Compare files and generate diff.."""

import json
import os
from .parsing import parse_diff


def generate_diff(file_path1, file_path2):
    """
    Generate diff between two files.

    Args:
        file_path1: path to first file.
        file_path2: path to second file.

    Returns:
        formatted string of diff

    """
    if not os.path.isabs(file_path1):
        file_path1 = os.path.abspath(file_path1)
    if not os.path.isabs(file_path2):
        file_path2 = os.path.abspath(file_path2)

    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))

    return parse_diff(data1, data2)
