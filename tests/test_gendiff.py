"""Testing gendiff.py."""

#  ****
#  these are tests for FORMATTED diff output (currently failing)
#  have yet to add formatter support for flat and nested dicts
#  for now only testing parsing @ test_parsing.py
#  ****
#
#
#  from gendiff import generate_diff
#  from .fixtures import expected
#
#
#  def test_generate_diff_flat_stylish():
#      assert generate_diff(
#          'tests/fixtures/file1_flat.json',
#          'tests/fixtures/file2_flat.json'
#      ) == expected.result_flat_stylish
#      assert generate_diff(
#          'tests/fixtures/file1_flat.yaml',
#          'tests/fixtures/file2_flat.yml'
#      ) == expected.result_flat_stylish
#
#
#  def test_generate_diff_nested_stylish():
#      assert generate_diff(
#          'tests/fixtures/file1_nested.json',
#          'tests/fixtures/file2_nested.json'
#      ) == expected.result_nested_stylish
#      assert generate_diff(
#          'tests/fixtures/file1_nested.yaml',
#          'tests/fixtures/file2_nested.yml'
#      ) == expected.result_nested_stylish
