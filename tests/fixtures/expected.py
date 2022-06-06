"""Expected results for tests."""


result_flat_stylish = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""


result_nested_stylish = """{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow: 
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}"""

result_parsing_flat = [
    {'name': 'follow', 'value': False,
     'status': 'removed', 'children': None},
    {'name': 'host', 'value': 'hexlet.io',
     'status': 'same', 'children': None},
    {'name': 'proxy', 'value': '123.234.53.22',
     'status': 'removed', 'children': None},
    {'name': 'timeout', 'value': 50, 'status':
        'changed_from_file1', 'children': None},
    {'name': 'timeout', 'value': 20, 'status':
        'changed_from_file2', 'children': None},
    {'name': 'verbose', 'value': True, 'status':
        'added', 'children': None}
]

result_parsing_nested = [
    {'name': 'common',
     'value': None,
     'status': 'same',
     'children': [
         {'name': 'follow',
          'value': False,
          'status': 'added',
          'children': None},
         {'name': 'setting1',
          'value': 'Value 1',
          'status': 'same',
          'children': None},
         {'name': 'setting2',
          'value': 200,
          'status': 'removed',
          'children': None},
         {'name': 'setting3',
          'value': True,
          'status': 'changed_from_file1',
          'children': None},
         {'name': 'setting3',
          'value': None,
          'status': 'changed_from_file2',
          'children': None},
         {'name': 'setting4',
          'value': 'blah blah',
          'status': 'added',
          'children': None},
         {'name': 'setting5',
          'value': {'key5': 'value5'},
          'status': 'added',
          'children': None},
         {'name': 'setting6',
          'value': None,
          'status': 'same',
          'children': [
            {'name': 'doge',
             'value': None,
             'status': 'same',
             'children': [
                {'name': 'wow',
                 'value': '',
                 'status': 'changed_from_file1',
                 'children': None},
                {'name': 'wow',
                 'value': 'so much',
                 'status':
                 'changed_from_file2',
                 'children': None}
             ]},
            {'name': 'key',
             'value': 'value',
             'status': 'same',
             'children': None},
            {'name': 'ops',
             'value': 'vops',
             'status': 'added',
             'children': None}
          ]}
     ]},
    {'name': 'group1',
     'value': None,
     'status': 'same',
     'children': [
         {'name': 'baz',
          'value': 'bas',
          'status': 'changed_from_file1',
          'children': None},
         {'name': 'baz',
          'value': 'bars',
          'status': 'changed_from_file2',
          'children': None},
         {'name': 'foo',
          'value': 'bar',
          'status': 'same',
          'children': None},
         {'name': 'nest',
          'value': {'key': 'value'},
          'status': 'changed_from_file1',
          'children': None},
         {'name': 'nest',
          'value': 'str',
          'status': 'changed_from_file2',
          'children': None}
     ]},
    {'name': 'group2',
     'value': {'abc': 12345, 'deep': {'id': 45}},
     'status': 'removed',
     'children': None},
    {'name': 'group3',
     'value': {'deep': {'id': {'number': 45}}, 'fee': 100500},
     'status': 'added',
     'children': None}
]
