from gendiff.formatters import jsonize, stylish, render, plain, format_value, json_format   # noqa: F401
from .fixtures import expected


def test_jsonize():
    assert jsonize(None) == 'null'
    assert jsonize(False) == 'false'
    assert jsonize('hello json') == 'hello json'


def test_format_value():
    assert format_value(True) == 'true'
    assert format_value(50) == 50
    assert format_value('some string') == "'some string'"


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


def test_plain():
    assert plain(
        expected.result_parsing_flat
    ) == expected.result_plain_flat
    assert plain(
        expected.result_parsing_nested
    ) == expected.result_plain_nested


def test_json_format():
    assert json_format(
        expected.result_parsing_flat) == expected.result_json_flat
    assert json_format(
        expected.result_parsing_nested) == expected.result_json_nested
