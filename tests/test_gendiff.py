"""Testing gendiff."""

from gendiff.gendiff import generate_diff
from .fixtures import expected


def test_gendiff():

    assert generate_diff(
        'tests/fixtures/file1.json',
        'tests/fixtures/file2.json'
    ) == expected.expected_test_gendiff_flat_json
