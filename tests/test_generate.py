import pytest
from gendiff import generate_diff, read_file


nested_json1 = 'tests/fixtures/files/json/nested_file1.json'
nested_json2 = 'tests/fixtures/files/json/nested_file2.json'
nested_yaml1 = 'tests/fixtures/files/yaml/nested_file1.yaml'
nested_yaml2 = 'tests/fixtures/files/yaml/nested_file2.yml'
stylish_nested = read_file(
    'tests/fixtures/expected/formatters/stylish_nested.txt')
plain_nested = read_file(
    'tests/fixtures/expected/formatters/plain_nested.txt')
json_nested = read_file(
    'tests/fixtures/expected/formatters/json_format_nested.txt')


@pytest.mark.parametrize("dict1, dict2, formatter, result", [
    (nested_json1, nested_json2, 'stylish', stylish_nested),
    (nested_json1, nested_json2, 'plain', plain_nested),
    (nested_json1, nested_json2, 'json', json_nested),
    (nested_yaml1, nested_yaml2, 'stylish', stylish_nested),
    (nested_yaml1, nested_yaml2, 'plain', plain_nested),
    (nested_yaml1, nested_yaml2, 'json', json_nested)
])
def test_generate_diff(dict1, dict2, formatter, result):
    assert generate_diff(dict1, dict2, formatter) == result
