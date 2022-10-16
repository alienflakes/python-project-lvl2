import json


def json_format(data: dict) -> str:
    """Construct output in JSON style."""
    return json.dumps(data, indent=4)
