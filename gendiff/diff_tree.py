def make_template(
        node_type: str, value: any, changed_value=None, children=None) -> dict:
    """Create representation for a node."""
    return {
        'node_type': node_type,
        'value': value,
        'changed_value': changed_value,
        'children': children
    }


def build_diff(dict1: dict, dict2: dict) -> dict:
    """Construct a tree of differences between two dicts."""
    all_diff = {}

    added_keys = list(dict2.keys() - dict1.keys())
    removed_keys = list(dict1.keys() - dict2.keys())

    for key in dict1.keys() | dict2.keys():

        if key in added_keys:
            all_diff.update(
                {
                    key: make_template(node_type='added', value=dict2[key])
                }
            )
            continue
        if key in removed_keys:
            all_diff.update(
                {
                    key: make_template(node_type='removed', value=dict1[key])
                }
            )
            continue

        data1 = dict1[key]
        data2 = dict2[key]
        if isinstance(data1, dict) and isinstance(data2, dict):
            all_diff.update(
                {
                    key: make_template(node_type='nested',
                                       value=None,
                                       children=build_diff(data1, data2))
                }
            )
        elif data1 == data2:
            all_diff.update(
                {
                    key: make_template(node_type='same', value=data1)
                }
            )
        else:
            all_diff.update(
                {
                    key: make_template(node_type='updated',
                                       value=data1,
                                       changed_value=data2)
                }
            )

    return dict(sorted(all_diff.items()))
