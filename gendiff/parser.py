import json
import yaml


def parse(source, _format: str) -> dict:
    """Parse a file to Python dict."""
    if _format == 'json':
        return json.loads(source)
    elif _format == 'yaml' or 'yml':
        return yaml.safe_load(source)
