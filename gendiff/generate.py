"""Compare files and generate diff.."""

import json
import yaml
import os
from .parsing import parse_diff
from .formatters import stylish


def get_data_from_file(file_path):
    """
    Extract a Python object from JSON or YAML file.
    Args:
        file_path: path to file

    Returns:
        python object
    """
    if not os.path.isabs(file_path):
        file_path = os.path.abspath(file_path)

    extension = os.path.splitext(file_path)[1]
    data = {}

    if extension == '.json':
        with open(file_path, 'r') as file:
            data = json.load(file)
    elif extension == '.yaml' or '.yml':
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
    return data


def generate_diff(file_path1, file_path2, formatter='stylish'):
    """
    Generate diff between two files.

    Args:
        file_path1: path to first file.
        file_path2: path to second file.
        formatter: format of resulted representation

    Returns:
        formatted string of diff

    """

    data1 = get_data_from_file(file_path1)
    data2 = get_data_from_file(file_path2)

    if formatter == 'stylish':
        return stylish(parse_diff(data1, data2))
