"""Gendiff formatters."""

import json


def jsonize_bool(item):
    if type(item) is bool or None:
        return json.dumps(item)
    return item


#  **NOT READY FOR NESTED DIFF, works only at flat diff for now**
def stylish(diffs):
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
