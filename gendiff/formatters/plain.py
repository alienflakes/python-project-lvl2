WORDING = {
    'template': "Property '{name}' was ",
    'added': "added with value: {value}",
    'removed': "removed",
    'changed': "updated. From {value} to {changed_value}",
    'complex_value': "[complex_value]"
}


def plain(data):

    lines = []
    for key, params in sorted(data.items()):
        if params['status'] == 'same':
            continue
        first_part = WORDING['template'].format(name=key)
        second_part = WORDING[params['status']].format(
            value=params['value'], changed_value=params['changed_value']
        )
        lines.append(first_part + second_part)

    return '\n'.join(lines)
