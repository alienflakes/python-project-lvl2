"""Testing parsing.py."""

from gendiff import parse_diff   # noqa: F401
from .fixtures import fixture, expected


def test_parse_diff_flat():
    assert parse_diff(
        fixture.fixture_flat_dict1, fixture.fixture_flat_dict2
    ) == expected.result_parsing_flat


def test_parse_diff_nested():
    assert parse_diff(
        fixture.fixture_nested_dict1, fixture.fixture_nested_dict2
    ) == expected.result_parsing_nested
