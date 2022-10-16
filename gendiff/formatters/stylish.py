import itertools
import json


SYMBOLS = {
    'added': '+',
    'removed': '-',
    'same': ' ',
    'nested': ' ',
    'new_inside_nested': ' '
}


def jsonize(item):
    """Return JSON representation of a Python object."""
    if isinstance(item, bool) or item is None:
        return json.dumps(item)
    return item


def render(data: dict) -> dict:
    """Build a tree of string parts for Stylish output."""
    if not isinstance(data, dict):
        return jsonize(data)

    result = {}
    for key, value in data.items():
        if not isinstance(value, dict):
            first_part = f"{SYMBOLS['new_inside_nested']} {key}"
            result[first_part] = jsonize(value)
            continue
        node_type = value.get('node_type', 'new_inside_nested')
        if node_type == 'updated':
            first_part_removed = f"{SYMBOLS['removed']} {key}"
            result[first_part_removed] = render(value['value'])
            first_part_added = f"{SYMBOLS['added']} {key}"
            result[first_part_added] = render(value['changed_value'])
            continue
        first_part = f"{SYMBOLS[node_type]} {key}"
        if node_type == 'nested':
            result[first_part] = render(value['children'])
        else:
            result[first_part] = render(value.get('value', value))

    return result


def stylish(diff: dict) -> str:
    """Construct Stylish output from tree of strings."""

    replacer = '  '
    spaces_count = 1

    def walk(current_value, depth):
        if not isinstance(current_value, dict):
            return current_value

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
