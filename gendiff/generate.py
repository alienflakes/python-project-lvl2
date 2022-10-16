from .diff_tree import build_diff
from .parser import parse
from .extract import read_file, get_extension
from .formatters import stylish, plain, json_format


def generate_diff(
        first_path: str, second_path: str, format_name='stylish') -> str:
    """Generate stylized output of diff between two files."""

    file1 = read_file(first_path)
    file2 = read_file(second_path)

    data1 = parse(file1, get_extension(first_path))
    data2 = parse(file2, get_extension(second_path))

    if format_name == 'stylish':
        formatter = stylish
    if format_name == 'plain':
        formatter = plain
    if format_name == 'json':
        formatter = json_format

    return formatter(build_diff(data1, data2))
