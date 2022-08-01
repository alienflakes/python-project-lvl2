"""Parsing diff module."""


def parse_diff(dct1, dct2):
    """

    Args:
        dct1: first dict
        dct2: second dict

    Returns:
        sorted list of dicts
    """

    def make_template(status, value, changed_value=None, children=None):
        return {
            'status': status,
            'value': value,
            'changed_value': changed_value,
            'children': children
        }

    all_diff = {}

    all_diff.update(
        {
            added_key: make_template(
                status='added',
                value=dct2[added_key]
            )
            for added_key in list(dct2.keys() - dct1.keys())
        }
    )

    all_diff.update(
        {
            removed_key: make_template(
                status='removed',
                value=dct1[removed_key]
            )
            for removed_key in list(dct1.keys() - dct2.keys())
        }
    )

    for same_key in list(dct1.keys() & dct2.keys()):
        data1 = dct1[same_key]
        data2 = dct2[same_key]

        if isinstance(data1, dict) and isinstance(data2, dict):
            all_diff.update(
                {same_key: make_template(
                    status='same',
                    value=None,
                    children=parse_diff(data1, data2)
                )
                }
            )
        else:
            if data1 == data2:
                all_diff.update(
                    {same_key: make_template(
                        status='same',
                        value=data1
                    )
                    }
                )
            else:
                all_diff.update(
                    {same_key: make_template(
                        status='changed',
                        value=data1, changed_value=data2
                    )
                    }
                )

    return all_diff
