"""Expected results for tests."""


result_parsing_flat = {
    'verbose': {
        'status': 'added',
        'old_value': None,
        'new_value': True,
        'children': None},
    'follow': {
        'status': 'removed',
        'old_value': False,
        'new_value': None,
        'children': None
    },
    'proxy': {
        'status': 'removed',
        'old_value': '123.234.53.22',
        'new_value': None,
        'children': None
    },
    'host': {
        'status': 'same',
        'old_value': 'hexlet.io',
        'new_value': 'hexlet.io',
        'children': None
    },
    'timeout': {
        'status': 'changed',
        'old_value': 50,
        'new_value': 20,
        'children': None
    }
}

result_parsing_nested = {
    'group3': {
        'status': 'added',
        'old_value': None,
        'new_value': {
            'deep': {
                'id': {
                    'number': 45
                }
            },
            'fee': 100500
        },
        'children': None
    },
    'group2': {
        'status': 'removed',
        'old_value': {
            'abc': 12345,
            'deep': {
                'id': 45
            }
        },
        'new_value': None,
        'children': None
    },
    'common': {
        'status': 'same',
        'old_value': None,
        'new_value': None,
        'children': {
            'setting5': {
                'status': 'added',
                'old_value': None,
                'new_value': {
                    'key5': 'value5'
                },
                'children': None
            },
            'follow': {
                'status': 'added',
                'old_value': None,
                'new_value': False,
                'children': None
            },
            'setting4': {
                'status': 'added',
                'old_value': None,
                'new_value': 'blah blah',
                'children': None
            },
            'setting2': {
                'status': 'removed',
                'old_value': 200,
                'new_value': None,
                'children': None
            },
            'setting6': {
                'status': 'same',
                'old_value': None,
                'new_value': None,
                'children': {
                    'ops': {
                        'status': 'added',
                        'old_value': None,
                        'new_value': 'vops',
                        'children': None
                    },
                    'doge': {
                        'status': 'same',
                        'old_value': None,
                        'new_value': None,
                        'children': {
                            'wow': {
                                'status': 'changed',
                                'old_value': '',
                                'new_value': 'so much',
                                'children': None
                            }
                        }
                    },
                    'key': {
                        'status': 'same',
                        'old_value': 'value',
                        'new_value': 'value',
                        'children': None
                    }
                }
            },
            'setting1': {
                'status': 'same',
                'old_value': 'Value 1',
                'new_value': 'Value 1',
                'children': None
            },
            'setting3': {
                'status': 'changed',
                'old_value': True,
                'new_value': None,
                'children': None
            }
        }
    },
    'group1': {
        'status': 'same',
        'old_value': None,
        'new_value': None,
        'children': {
            'foo': {
                'status': 'same',
                'old_value': 'bar',
                'new_value': 'bar',
                'children': None
            },
            'baz': {
                'status': 'changed',
                'old_value': 'bas',
                'new_value': 'bars',
                'children': None
            },
            'nest': {
                'status': 'changed',
                'old_value': {
                    'key': 'value'
                },
                'new_value': 'str',
                'children': None
            }
        }
    }
}

result_render_flat = {
    '- follow': 'false',
    '  host': 'hexlet.io',
    '- proxy': '123.234.53.22',
    '- timeout': 50,
    '+ timeout': 20,
    '+ verbose': 'true'
}

result_render_nested = {
    '  common': {
        '+ follow': 'false',
        '  setting1': 'Value 1',
        '- setting2': 200,
        '- setting3': 'true',
        '+ setting3': 'null',
        '+ setting4': 'blah blah',
        '+ setting5': {
            '  key5': 'value5'
        },
        '  setting6': {
            '  doge': {
                '- wow': '',
                '+ wow': 'so much'
            },
            '  key': 'value',
            '+ ops': 'vops'
        }
    },
    '  group1': {
        '- baz': 'bas',
        '+ baz': 'bars',
        '  foo': 'bar',
        '- nest': {
            '  key': 'value'
        },
        '+ nest': 'str'
    },
    '- group2': {
        '  abc': 12345,
        '  deep': {
            '  id': 45
        }
    },
    '+ group3': {
        '  deep': {
            '  id': {
                '  number': 45
            }
        },
        '  fee': 100500
    }
}

result_stylish_flat = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

result_stylish_nested = """{
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

