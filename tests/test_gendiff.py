"""Testing gendiff."""

from gendiff.gendiff import generate_diff


def test_gendiff():

    assert generate_diff(
        '/home/phelix/codish/hexlet/gendiff_project/tests/fixtures/file1.json',
        'tests/fixtures/file2.json'
    ) == """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
