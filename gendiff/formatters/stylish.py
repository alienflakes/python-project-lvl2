import itertools
import json


SYMBOLS = {
    'added': '+',
    'removed': '-',
    'same': ' ',
    'new_inside': ' '
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
            first_part = f"{SYMBOLS['new_inside']} {key}"
            result[first_part] = jsonize(value)
            continue
        status = value.get('status', 'new_inside')
        if status == 'changed':
            first_part_removed = f"{SYMBOLS['removed']} {key}"
            result[first_part_removed] = render(value['value'])
            first_part_added = f"{SYMBOLS['added']} {key}"
            result[first_part_added] = render(value['changed_value'])
            continue
        first_part = f"{SYMBOLS[status]} {key}"
        if value.get('children'):
            result[first_part] = render(value['children'])
        else:
            result[first_part] = render(value.get('value', value))

    return result


def stylish(diff):

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
