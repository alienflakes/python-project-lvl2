"""Testing gendiff.py."""

from gendiff import generate_diff
from .fixtures import expected


def test_generate_diff_json_flat_stylish():
    assert generate_diff(
        'tests/fixtures/file1_flat.json',
        'tests/fixtures/file2_flat.json'
    ) == expected.result_flat_stylish


def test_generate_diff_yaml_flat_stylish():
    assert generate_diff(
        'tests/fixtures/file1_flat.yaml',
        'tests/fixtures/file2_flat.yml'
    ) == expected.result_flat_stylish


def test_generate_diff_json_nested_stylish():
    assert generate_diff(
        'tests/fixtures/file1_nested.json',
        'tests/fixtures/file2_nested.json'
    ) == expected.result_nested_stylish


def test_generate_diff_yaml_nested_stylish():
    assert generate_diff(
        'tests/fixtures/file1_nested.yaml',
        'tests/fixtures/file2_nested.yml'
    ) == expected.result_nested_stylish
