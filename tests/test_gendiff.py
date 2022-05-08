"""Testing gendiff."""

from gendiff import generate_diff
from .fixtures import expected


def test_generate_diff():
    assert generate_diff(
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json'
    ) == expected.result_flat
