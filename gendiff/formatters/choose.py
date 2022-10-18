from .stylish import stylish
from .plain import plain
from .json_format import json_format


def choose_formatter(format_name: str) -> callable:
    """Return chosen formatter function."""
    if format_name == 'stylish':
        return stylish
    elif format_name == 'plain':
        return plain
    elif format_name == 'json':
        return json_format
