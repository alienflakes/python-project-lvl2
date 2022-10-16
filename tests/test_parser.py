import pytest
from gendiff import parse, read_file
from .fixtures import dicts


flat_json = read_file('tests/fixtures/files/json/flat_file1.json')
nested_json = read_file('tests/fixtures/files/json/nested_file1.json')
flat_yaml = read_file('tests/fixtures/files/yaml/flat_file1.yaml')
nested_yaml = read_file('tests/fixtures/files/yaml/nested_file1.yaml')

flat_dict = dicts.flat_dict1
nested_dict = dicts.nested_dict1


@pytest.mark.parametrize('source, _format, result', [
    (flat_json, 'json', flat_dict),
    (nested_json, 'json', nested_dict),
    (flat_yaml, 'yaml', flat_dict),
    (nested_yaml, 'yml', nested_dict)
])
def test_parse(source, _format, result):
    assert parse(source, _format) == result
