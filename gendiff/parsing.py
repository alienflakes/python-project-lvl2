"""Parsing diff module."""


def parse_diff(dct1, dct2):
    """
    Find diff between two dictionaries.

    Args:
        dct1: first dict
        dct2: second dict

    Returns:
        diff dict
    """

    all_diffs = {
        'added': {},
        'removed': {},
        'same': {},
        'changed_from_file1': {},
        'changed_from_file2': {}
    }

    added_keys = list(dct2.keys() - dct1.keys())
    removed_keys = list(dct1.keys() - dct2.keys())

    all_diffs['added'].update(
        {key: dct2[key] for key in added_keys}
    )
    all_diffs['removed'].update(
        {key: dct1[key] for key in removed_keys}
    )

    both = list(dct1.keys() & dct2.keys())
    for key in both:
        value1 = dct1[key]
        value2 = dct2[key]
        if value1 == value2:
            all_diffs['same'][key] = value1
        else:
            all_diffs['changed_from_file1'][key] = value1
            all_diffs['changed_from_file2'][key] = value2

    return all_diffs
