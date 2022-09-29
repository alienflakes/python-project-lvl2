from itertools import chain
from .stylish import jsonize


WORDING = {
    'template': "Property {name} was ",
    'added': "added with value: {val}",
    'removed': "removed",
    'changed': "updated. From {val} to {changed_val}",
    'complex_value': "[complex value]"
}


def format_value(subject):
    if isinstance(subject, str):
        return f"'{subject}'"
    else:
        return jsonize(subject)


def plain(source):
    lines = []

    def walk(data, path):

        for key, params in sorted(data.items()):
            if params['children']:
                walk(params['children'], list(chain(path, [key])))
                continue
            if params['status'] == 'same':
                continue
            if isinstance(params['value'], dict):
                value = WORDING['complex_value']
            else:
                value = format_value(params['value'])

            first_part = WORDING['template'].format(
                name=format_value('.'.join(path + [key]))
            )
            second_part = WORDING[params['status']].format(
                val=value,
                changed_val=format_value(params['changed_value'])
            )
            lines.append(first_part + second_part)

        return '\n'.join(lines)

    return walk(source, [])
