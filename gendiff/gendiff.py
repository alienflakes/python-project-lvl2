"""Compare files and generate diff.."""
import json
from os.path import abspath, isabs


def visualize(diffs_lst):
    """
    Construct a visual representation of files' diff.

    Uses a tuple of each diff, containing:
    [0]: name of changed parameter
    [1]: value of changed parameter
    [2]: symbol representing the change

    Args:
        diffs_lst: list of tuples

    Returns:
        formatted string of diffs

    """
    lines = []
    for each in diffs_lst:
        name, value, symbol = each
        lines.append('  {0} {1}: {2}'.format(symbol, name, value))
    joined = '\n'.join(lines)
    return '{0}\n{1}\n{2}'.format('{', joined, '}')


def lowercase_bool(_dict):
    """
    Replace Python bool with json-style bool as string, if found in dict.

    Modifies dict in-place.

    Args:
        _dict: dict

    """
    for k, v in _dict.items():
        if v is True:
            _dict[k] = 'true'
        if v is False:
            _dict[k] = 'false'
        if v is None:
            _dict[k] = 'none'


def generate_diff(file_path1, file_path2):
    """
    Generate diff between two files.

    Args:
        file_path1: path to first file.
        file_path2: path to second file.

    Returns:
        formatted string.

    """
    if not isabs(file_path1):
        file_path1 = abspath(file_path1)
    if not isabs(file_path2):
        file_path2 = abspath(file_path2)

    data_dct1 = json.load(open(file_path1))
    data_dct2 = json.load(open(file_path2))

    lowercase_bool(data_dct1)
    lowercase_bool(data_dct2)

    symbol_added = '+'
    symbol_removed = '-'
    symbol_same = ' '

    added_keys = list(data_dct2.keys() - data_dct1.keys())
    removed_keys = list(data_dct1.keys() - data_dct2.keys())
    added = [
        (key, data_dct2[key], symbol_added)
        for key in added_keys
    ]
    removed = [
        (key, data_dct1[key], symbol_removed)
        for key in removed_keys
    ]
    unchanged = list(data_dct1.keys() & data_dct2.keys())

    same = []
    changed_file1 = []
    changed_file2 = []

    for key in unchanged:
        value1 = data_dct1[key]
        value2 = data_dct2[key]
        if value1 == value2:
            same.append((key, value1, symbol_same))
        else:
            changed_file1.append(
                (key, value1, symbol_removed),
            )
            changed_file2.append(
                (key, value2, symbol_added),
            )

    all_diffs = added + removed + same + changed_file1 + changed_file2
    all_diffs.sort(key=lambda name: name[0])

    return visualize(all_diffs)
