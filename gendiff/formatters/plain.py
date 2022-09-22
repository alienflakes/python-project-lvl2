from .stylish import jsonize


WORDING = {
    'template': "Property {name} was ",
    'added': "added with value: {value}",
    'removed': "removed",
    'changed': "updated. From {value} to {changed_value}",
    'complex_value': "[complex_value]"
}


def format_value(subject):
    if isinstance(subject, str):
        return f"'{subject}'"
    else:
        return jsonize(subject)


def plain(data):
    lines = []
    for key, params in sorted(data.items()):
        if params['status'] == 'same':
            continue
        first_part = WORDING['template'].format(name=format_value(key))
        second_part = WORDING[params['status']].format(
            value=format_value(params['value']),
            changed_value=format_value(params['changed_value'])
        )
        lines.append(first_part + second_part)

    return '\n'.join(lines)
