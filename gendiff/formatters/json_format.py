import json


def json_format(data):
    return json.dumps(data, indent=2, sort_keys=True)
