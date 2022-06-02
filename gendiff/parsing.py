"""Parsing diff module."""


def parse_diff(dct1, dct2):
    """

    Args:
        dct1: first dict
        dct2: second dict

    Returns:
        sorted list of dicts
    """

    all_diff = []

    all_diff.extend([
        {
            'name': added_key,
            'value': dct2[added_key],
            'status': 'added',
            'children': None
        }
        for added_key in list(dct2.keys() - dct1.keys())
    ])

    all_diff.extend([
        {
            'name': removed_key,
            'value': dct1[removed_key],
            'status': 'removed',
            'children': None
        }
        for removed_key in list(dct1.keys() - dct2.keys())
    ])

    for same_key in list(dct1.keys() & dct2.keys()):
        data1 = dct1[same_key]
        data2 = dct2[same_key]

        if type(data1) is dict and type(data2) is dict:
            all_diff.append(
                {
                    'name': same_key,
                    'value': None,
                    'status': 'same',
                    'children': parse_diff(data1, data2)
                }
            )
            continue
        elif type(data1) is dict:
            all_diff.append(
                {
                    'name': same_key,
                    'value': data1,
                    'status': 'changed_from_file1',
                    'children': None
                }
            )
            continue
        elif type(data2) is dict:
            all_diff.append(
                {
                    'name': same_key,
                    'value': data2,
                    'status': 'changed_from_file2',
                    'children': None
                }
            )
            continue

        else:
            if data1 == data2:
                all_diff.append(
                    {
                        'name': same_key,
                        'value': data1,
                        'status': 'same',
                        'children': None
                    }
                )
            else:
                all_diff.append(
                    {
                        'name': same_key,
                        'value': data1,
                        'status': 'changed_from_file1',
                        'children': None
                    }
                )
                all_diff.append(
                    {
                        'name': same_key,
                        'value': data2,
                        'status': 'changed_from_file2',
                        'children': None
                    }
                )

    return sorted(all_diff, key=lambda x: x['name'])
