from gendiff import stylish, render, jsonize  # noqa: F401
from .fixtures import expected


def test_jsonize():
    assert jsonize(True) == 'true'
    assert jsonize(None) == 'null'
    assert jsonize('none of those') == 'none of those'
    assert jsonize(89) == 89


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
