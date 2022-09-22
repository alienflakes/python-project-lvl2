from gendiff.formatters import stylish, render   # noqa: F401
from .fixtures import expected


def test_render():
    assert render(
        expected.result_parsing_flat
    ) == expected.result_render_flat
    assert render(
        expected.result_parsing_nested
    ) == expected.result_render_nested


def test_stylish():
    assert stylish(
        expected.result_parsing_flat
    ) == expected.result_stylish_flat
    assert stylish(
        expected.result_parsing_nested
    ) == expected.result_stylish_nested
