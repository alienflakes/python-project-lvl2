"""Testing gendiff.py."""

from gendiff import generate_diff
from .fixtures import expected


def test_generate_diff_json():
    assert generate_diff(
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json'
    ) == expected.result_flat


def test_generate_diff_yaml():
    assert generate_diff(
        'tests/fixtures/file1.yaml',
        'tests/fixtures/file2.yml'
    ) == expected.result_flat
