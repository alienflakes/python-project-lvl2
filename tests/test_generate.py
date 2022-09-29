"""Testing generate.py."""

from gendiff import generate_diff
from .fixtures import expected


def test_generate_diff_flat_stylish():
    assert generate_diff(
        'tests/fixtures/file1_flat.json',
        'tests/fixtures/file2_flat.json'
    ) == expected.result_stylish_flat
    assert generate_diff(
        'tests/fixtures/file1_flat.yaml',
        'tests/fixtures/file2_flat.yml'
    ) == expected.result_stylish_flat


def test_generate_diff_nested_stylish():
    assert generate_diff(
        'tests/fixtures/file1_nested.json',
        'tests/fixtures/file2_nested.json'
    ) == expected.result_stylish_nested
    assert generate_diff(
        'tests/fixtures/file1_nested.yaml',
        'tests/fixtures/file2_nested.yml'
    ) == expected.result_stylish_nested


def test_generate_diff_plain():
    assert generate_diff(
        'tests/fixtures/file1_flat.json',
        'tests/fixtures/file2_flat.json',
        'plain'
    ) == expected.result_plain_flat
    assert generate_diff(
        'tests/fixtures/file1_nested.json',
        'tests/fixtures/file2_nested.json',
        'plain'
    ) == expected.result_plain_nested


def test_generate_diff_json():
    assert generate_diff(
        'tests/fixtures/file1_flat.json',
        'tests/fixtures/file2_flat.json',
        'json'
    ) == expected.result_json_flat
    assert generate_diff(
        'tests/fixtures/file1_nested.json',
        'tests/fixtures/file2_nested.json',
        'json'
    ) == expected.result_json_nested
