"""Gendiff formatters."""

import itertools
import json


SYMBOLS = {
    'added': '+',
    'removed': '-',
    'same': ' ',
    'changed_from_file1': '-',
    'changed_from_file2': '+',
    'new': ' '
}


def jsonize(item):
    if isinstance(item, bool) or item is None:
        return json.dumps(item)
    return item


def render(data):
    if not isinstance(data, dict):
        return jsonize(data)

    result = {}
    for key, value in sorted(data.items()):
        if not isinstance(value, dict):
            first_part = f"{SYMBOLS['new']} {key}"
            result[first_part] = jsonize(value)
            continue
        status = value.get('status', 'new')
        if status == 'changed':
            first_part_from_file1 = f"{SYMBOLS['changed_from_file1']} {key}"
            result[first_part_from_file1] = render(value['old_value'])
            first_part_from_file2 = f"{SYMBOLS['changed_from_file2']} {key}"
            result[first_part_from_file2] = render(value['new_value'])
            continue
        first_part = f"{SYMBOLS[status]} {key}"
        if value.get('children'):
            result[first_part] = render(value['children'])
            continue
        if status == 'added' or status == 'same':
            result[first_part] = render(value['new_value'])
        elif status == 'removed':
            result[first_part] = render(value['old_value'])
        else:
            result[first_part] = render(value)

    return result


def stylish(diff):

    replacer = '  '
    spaces_count = 1

    def walk(current_value, depth):
        if not isinstance(current_value, dict):
            return jsonize(current_value)

        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for first_part, second_part in current_value.items():
            lines.append(
                f'{deep_indent}{first_part}: '
                f'{walk(second_part, deep_indent_size + 1)}'
            )
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return walk(render(diff), 0)
