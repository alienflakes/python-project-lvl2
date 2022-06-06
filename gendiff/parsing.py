"""Parsing diff module."""


def parse_diff(dct1, dct2):
    """

    Args:
        dct1: first dict
        dct2: second dict

    Returns:
        sorted list of dicts
    """

    def make_template(name, value, status, children=None):
        return {
            'name': name,
            'value': value,
            'status': status,
            'children': children
        }

    all_diff = []

    all_diff.extend([
        make_template(
            name=added_key, value=dct2[added_key],
            status='added'
        )
        for added_key in list(dct2.keys() - dct1.keys())
    ])
    all_diff.extend([
        make_template(
            name=removed_key, value=dct1[removed_key],
            status='removed'
        )
        for removed_key in list(dct1.keys() - dct2.keys())
    ])

    for same_key in list(dct1.keys() & dct2.keys()):
        data1 = dct1[same_key]
        data2 = dct2[same_key]

        if isinstance(data1, dict) and isinstance(data2, dict):
            all_diff.append(
                make_template(
                    name=same_key, value=None,
                    status='same', children=parse_diff(data1, data2)
                )
            )
        else:
            if data1 == data2:
                all_diff.append(
                    make_template(
                        name=same_key, value=data1,
                        status='same'
                    )
                )
            else:
                all_diff.append(
                    make_template(
                        name=same_key, value=data1,
                        status='changed_from_file1'
                    )
                )
                all_diff.append(
                    make_template(
                        name=same_key, value=data2,
                        status='changed_from_file2'
                    )
                )

    return sorted(all_diff, key=lambda diff: diff['name'])
