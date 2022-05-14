"""Parsing diff module."""

import json


def jsonize_bool(item):
    if type(item) is bool or None:
        return json.dumps(item)
    return item


def visualize(diffs):
    """
    Construct a visual representation of files' diff.

    Args:
        diffs: dict

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
        for name, data in value.items():
            symbol = symbols[key]
            lines.append(
                '  {0} {1}: {2}'.format(symbol, name, jsonize_bool(data))
            )

    first_letter_index = 4
    lines.sort(key=lambda line: line[first_letter_index])

    return '{0}\n{1}\n{2}'.format('{', '\n'.join(lines), '}')


def parse_diff(dct1, dct2):
    """
    Find diff between two dictionaries.

    Args:
        dct1: first dict
        dct2: second dict

    Returns:
        formatted string
    """

    all_diffs = {
        'added': {},
        'removed': {},
        'same': {},
        'changed_from_file1': {},
        'changed_from_file2': {}
    }

    added_keys = list(dct2.keys() - dct1.keys())
    removed_keys = list(dct1.keys() - dct2.keys())

    all_diffs['added'].update(
        {key: dct2[key] for key in added_keys}
    )
    all_diffs['removed'].update(
        {key: dct1[key] for key in removed_keys}
    )

    both = list(dct1.keys() & dct2.keys())
    for key in both:
        value1 = dct1[key]
        value2 = dct2[key]
        if value1 == value2:
            all_diffs['same'][key] = value1
        else:
            all_diffs['changed_from_file1'][key] = value1
            all_diffs['changed_from_file2'][key] = value2

    return visualize(all_diffs)
