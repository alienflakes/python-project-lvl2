from itertools import chain
from .stylish import jsonize


WORDING = {
    'template': "Property {name} was ",
    'added': "added with value: {val}",
    'removed': "removed",
    'updated': "updated. From {val} to {changed_val}",
    'complex_value': "[complex value]"
}


def format_value(subject):
    """Return formatted values for Plain output."""
    if isinstance(subject, dict):
        return WORDING['complex_value']
    if isinstance(subject, str):
        return f"'{subject}'"
    else:
        return jsonize(subject)


def plain(source: dict) -> str:
    """Build Plain output."""
    lines = []

    def walk(data, path):

        for key, params in data.items():
            if params['node_type'] == 'nested':
                walk(params['children'], list(chain(path, [key])))
                continue
            if params['node_type'] == 'same':
                continue

            first_part = WORDING['template'].format(
                name=format_value('.'.join(path + [key]))
            )
            second_part = WORDING[params['node_type']].format(
                val=format_value(params['value']),
                changed_val=format_value(params['changed_value'])
            )
            lines.append(first_part + second_part)

        return '\n'.join(lines)

    return walk(source, [])
