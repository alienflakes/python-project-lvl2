"""Testing gendiff."""

from gendiff import generate_diff
from .fixtures import expected


def test_generate_diff():
    assert generate_diff(
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json'
    ) == expected.result_json_flat
    assert generate_diff(
        'tests/fixtures/empty_file1.json',
        'tests/fixtures/empty_file2.json'
    ) == expected.result_json_empty
    assert generate_diff(
        'tests/fixtures/empty_file1.json',
        'tests/fixtures/file2.json'
    ) == expected.result_json_add_all
    assert generate_diff(
        'tests/fixtures/file1.json',
        'tests/fixtures/empty_file2.json'
    ) == expected.result_json_remove_all
