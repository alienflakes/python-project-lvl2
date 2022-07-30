"""Parsing diff module."""


def parse_diff(dct1, dct2):
    """

    Args:
        dct1: first dict
        dct2: second dict

    Returns:
        sorted list of dicts
    """

    def make_template(status, old_value, new_value, children=None):
        return {
            'status': status,
            'old_value': old_value,
            'new_value': new_value,
            'children': children
        }

    all_diff = {}

    all_diff.update(
        {
            added_key: make_template(
                old_value=None, new_value=dct2[added_key],
                status='added'
            )
            for added_key in list(dct2.keys() - dct1.keys())
        }
    )

    all_diff.update(
        {
            removed_key: make_template(
                old_value=dct1[removed_key], new_value=None,
                status='removed'
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
                    old_value=None, new_value=None,
                    status='same', children=parse_diff(data1, data2)
                )
                }
            )
        else:
            if data1 == data2:
                all_diff.update(
                    {same_key: make_template(
                        old_value=data1, new_value=data2,
                        status='same'
                    )
                    }
                )
            else:
                all_diff.update(
                    {same_key: make_template(
                        old_value=data1, new_value=data2,
                        status='changed'
                    )
                    }
                )

    return all_diff
