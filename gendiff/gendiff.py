"""Compare files and generate diff.."""
import json
from os.path import abspath, isabs


def visualize(diffs):
    """
    Construct a visual representation of files' diff.
    1. Creates lists of data pairs and their status symbol.
    2. Sorts lists by name of the pair.
    3. Sets up formatted lines.
    4. Constructs the visual output.

    Args:
        diffs: dict of diff with key=status

    Returns:
        formatted string

    """

    symbols = {
        'added': '+',
        'removed': '-',
        'same': ' ',
        'changed_from_file1': '-',
        'changed_from_file2': '+'
    }

    lines = []

    for key, value in diffs.items():
        for name, data in value:
            symbol = symbols[key]
            lines.append('  {0} {1}: {2}'.format(symbol, name, data))

    first_letter_index = 4
    lines.sort(key=lambda line: line[first_letter_index])

    return '{0}\n{1}\n{2}'.format('{', '\n'.join(lines), '}')


def jsonize_bool(item):
    if type(item) is bool or None:
        return json.dumps(item)
    return item


def generate_diff(file_path1, file_path2):
    """
    Generate diff between two files.

    Args:
        file_path1: path to first file.
        file_path2: path to second file.

    Returns:
        formatted string of diff

    """
    if not isabs(file_path1):
        file_path1 = abspath(file_path1)
    if not isabs(file_path2):
        file_path2 = abspath(file_path2)

    data_dct1 = json.load(open(file_path1))
    data_dct2 = json.load(open(file_path2))

    all_diffs = {
        'added': [],
        'removed': [],
        'same': [],
        'changed_from_file1': [],
        'changed_from_file2': []
    }

    added_keys = list(data_dct2.keys() - data_dct1.keys())
    removed_keys = list(data_dct1.keys() - data_dct2.keys())
    all_diffs['added'] = [
        [key, jsonize_bool(data_dct2[key])]
        for key in added_keys
    ]
    all_diffs['removed'] = [
        [key, jsonize_bool(data_dct1[key])]
        for key in removed_keys
    ]

    both = list(data_dct1.keys() & data_dct2.keys())
    for key in both:
        value1 = jsonize_bool(data_dct1[key])
        value2 = jsonize_bool(data_dct2[key])
        if value1 == value2:
            all_diffs['same'].append(
                [key, value1]
            )
        else:
            all_diffs['changed_from_file1'].append(
                [key, value1],
            )
            all_diffs['changed_from_file2'].append(
                [key, value2],
            )

    return visualize(all_diffs)
