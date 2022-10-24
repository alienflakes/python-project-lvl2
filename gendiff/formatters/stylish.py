import itertools
import json


SYMBOLS = {
    'added': '+',
    'removed': '-',
    'same': ' ',
    'nested': ' '
}


def jsonize(item):
    """Return JSON representation of a Python object."""
    if isinstance(item, bool) or item is None:
        return json.dumps(item)
    return item


def build_line(indent: str, key: str, value, replacer: str = '') -> str:
    """Return formatted line of Stylish diff representation."""
    return f'{indent}{replacer}{key}: {value}'


def stringify_value(value, depth: int = 0) -> str:
    """Format node's value."""
    if not isinstance(value, dict):
        return jsonize(value)

    indent = ' ' * 4
    lines = []

    for k, v in value.items():
        lines.append(
            build_line(
                indent=indent * (depth + 1), key=k,
                value=stringify_value(v, depth + 1)
            )
        )

    result = itertools.chain('{', lines, [(indent * depth) + '}'])
    return '\n'.join(result)


def stringify_node(key: str, node: dict, depth: int) -> str:
    """Format nodes with their values."""

    def replacer_by_type(_symbol):
        return f'  {_symbol} '

    indent = ' ' * 4
    current_indent = indent * depth

    lines = []
    node_type = node['node_type']

    if node_type == 'updated':
        lines.append(
            build_line(
                indent=current_indent, key=key,
                value=stringify_value(node['value'], depth + 1),
                replacer=replacer_by_type(SYMBOLS['removed'])
            )
        )
        lines.append(
            build_line(
                indent=current_indent, key=key,
                value=stringify_value(node['changed_value'], depth + 1),
                replacer=replacer_by_type(SYMBOLS['added'])
            )
        )
        return '\n'.join(lines)

    symbol = SYMBOLS[node_type]
    replacer_with_symbol = replacer_by_type(symbol)

    if node_type == 'nested':
        nested_lines = [
            stringify_node(key, value, depth + 1)
            for key, value in node['children'].items()
        ]
        result = itertools.chain(
            '{', nested_lines, [indent * (depth + 1) + '}']
        )
        value = '\n'.join(result)
        lines.append(
            build_line(
                indent=current_indent, key=key,
                value=value,
                replacer=replacer_with_symbol
            )
        )
    else:
        value = stringify_value(node['value'], depth + 1)
        lines.append(
            build_line(
                indent=current_indent, key=key,
                value=value,
                replacer=replacer_with_symbol
            )
        )

    return '\n'.join(lines)


def stylish(data: dict) -> str:
    """Return formatted diff in Stylish representation."""
    lines = [stringify_node(key, value, 0) for key, value in data.items()]
    result = itertools.chain('{', lines, '}')
    return '\n'.join(result)
