import pytest
from gendiff.diff_tree import build_diff
from .fixtures import dicts
from .fixtures.expected import parsing_result


@pytest.mark.parametrize("test_input1, test_input2, result", [
    (dicts.flat_dict1, dicts.flat_dict2, parsing_result.flat),
    (dicts.nested_dict1, dicts.nested_dict2, parsing_result.nested)
])
def test_parse_diff(test_input1, test_input2, result):
    assert build_diff(test_input1, test_input2) == result
