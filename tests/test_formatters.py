import pytest
from gendiff.formatters import jsonize, stylish, plain, format_value, json_format
from .fixtures.expected import diff_tree_result
from gendiff import read_file


@pytest.mark.parametrize("test_input, result", [
    (None, 'null'),
    (False, 'false'),
    ('hello json', 'hello json')
])
def test_jsonize(test_input, result):
    assert jsonize(test_input) == result


@pytest.mark.parametrize("test_input, result", [
    (True, 'true'),
    (50, 50),
    ('some string', "'some string'")
])
def test_format_value(test_input, result):
    assert format_value(test_input) == result


flat_input = diff_tree_result.flat
nested_input = diff_tree_result.nested


def read_from_filepath(filepath):
    with open(filepath) as file:
        return file.read()


stylish_flat = read_file('tests/fixtures/expected/formatters/stylish_flat.txt')
stylish_nested = read_file('tests/fixtures/expected/formatters/stylish_nested.txt')


@pytest.mark.parametrize("test_input, result", [
    (flat_input, stylish_flat),
    (nested_input, stylish_nested)
])
def test_stylish(test_input, result):
    assert stylish(test_input) == result


plain_flat = read_file('tests/fixtures/expected/formatters/plain_flat.txt')
plain_nested = read_file('tests/fixtures/expected/formatters/plain_nested.txt')


@pytest.mark.parametrize("test_input, result", [
    (flat_input, plain_flat),
    (nested_input, plain_nested)
])
def test_plain(test_input, result):
    assert plain(test_input) == result


json_format_flat = read_file('tests/fixtures/expected/formatters/json_format_flat.txt')
json_format_nested = read_file('tests/fixtures/expected/formatters/json_format_nested.txt')


@pytest.mark.parametrize("test_input, result", [
    (flat_input, json_format_flat),
    (nested_input, json_format_nested)
])
def test_json_format(test_input, result):
    assert json_format(test_input) == result
