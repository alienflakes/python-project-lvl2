from .diff_tree import build_diff
from .parser import parse
from .extract import read_file, get_extension
from .formatters import choose_formatter


def generate_diff(
        first_path: str, second_path: str, format_name='stylish') -> str:
    """Generate stylized output of diff between two files."""

    file1 = read_file(first_path)
    file2 = read_file(second_path)

    data1 = parse(file1, get_extension(first_path))
    data2 = parse(file2, get_extension(second_path))

    formatter = choose_formatter(format_name)

    return formatter(build_diff(data1, data2))
