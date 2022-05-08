"""Testing gendiff."""

from gendiff import generate_diff
from .fixtures import expected


def test_generate_diff():
    assert generate_diff(
        'tests/fixtures/empty.json',
        'tests/fixtures/file1.json'
    ) == expected.result_add_all
    assert generate_diff(
        'tests/fixtures/file1.json',
        'tests/fixtures/empty.json'
    ) == expected.result_remove_all
    assert generate_diff(
        'tests/fixtures/file2.json',
        'tests/fixtures/file2.json'
    )
    assert generate_diff(
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json'
    ) == expected.result_flat
