"""Expected results for tests."""


result_parsing_flat = {
    'verbose': {
        'status': 'added',
        'value': True,
        'changed_value': None,
        'children': None},
    'follow': {
        'status': 'removed',
        'value': False,
        'changed_value': None,
        'children': None},
    'proxy': {
        'status': 'removed',
        'value': '123.234.53.22',
        'changed_value': None,
        'children': None},
    'timeout': {
        'status': 'changed',
        'value': 50,
        'changed_value': 20,
        'children': None},
    'host': {
        'status': 'same',
        'value': 'hexlet.io',
        'changed_value': None,
        'children': None}
}

result_parsing_nested = {
    'group3': {
        'status': 'added',
        'value': {
            'deep': {
                'id': {
                    'number': 45
                }
            },
            'fee': 100500
        },
        'changed_value': None,
        'children': None
    },
    'group2': {
        'status': 'removed',
        'value': {
            'abc': 12345,
            'deep': {
                'id': 45
            }
        },
        'changed_value': None,
        'children': None
    },
    'group1': {
        'status': 'same',
        'value': None,
        'changed_value': None,
        'children': {
            'baz': {
                'status': 'changed',
                'value': 'bas',
                'changed_value': 'bars',
                'children': None},
            'nest': {
                'status': 'changed',
                'value': {'key': 'value'},
                'changed_value': 'str',
                'children': None},
            'foo': {
                'status': 'same',
                'value': 'bar',
                'changed_value': None,
                'children': None
            }
        }
    },
    'common': {
        'status': 'same',
        'value': None,
        'changed_value': None,
        'children': {
            'setting5': {
                'status': 'added',
                'value': {
                    'key5': 'value5'
                },
                'changed_value': None,
                'children': None
            },
            'follow': {
                'status': 'added',
                'value': False,
                'changed_value': None,
                'children': None
            },
            'setting4': {
                'status': 'added',
                'value': 'blah blah',
                'changed_value': None,
                'children': None
            },
            'setting2': {
                'status': 'removed',
                'value': 200,
                'changed_value': None,
                'children': None
            },
            'setting6': {
                'status': 'same',
                'value': None,
                'changed_value': None,
                'children': {
                    'ops': {
                        'status': 'added',
                        'value': 'vops',
                        'changed_value': None,
                        'children': None
                    },
                    'key': {
                        'status': 'same',
                        'value': 'value',
                        'changed_value': None,
                        'children': None
                    },
                    'doge': {
                        'status': 'same',
                        'value': None,
                        'changed_value': None,
                        'children': {
                            'wow': {
                                'status': 'changed',
                                'value': '',
                                'changed_value': 'so much',
                                'children': None
                            }
                        }
                    }
                }
            },
            'setting3': {
                'status': 'changed',
                'value': True,
                'changed_value': None,
                'children': None
            },
            'setting1': {
                'status': 'same',
                'value': 'Value 1',
                'changed_value': None,
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

""""{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

result_plain_flat = """Property 'follow' was removed
Property 'proxy' was removed
Property 'timeout' was updated. From 50 to 20
Property 'verbose' was added with value: true"""

result_plain_nested = """Property 'common.follow' was added with value: false
Property 'common.setting2' was removed
Property 'common.setting3' was updated. From true to null
Property 'common.setting4' was added with value: 'blah blah'
Property 'common.setting5' was added with value: [complex value]
Property 'common.setting6.doge.wow' was updated. From '' to 'so much'
Property 'common.setting6.ops' was added with value: 'vops'
Property 'group1.baz' was updated. From 'bas' to 'bars'
Property 'group1.nest' was updated. From [complex value] to 'str'
Property 'group2' was removed
Property 'group3' was added with value: [complex value]"""

result_json_flat = """{
  "follow": {
    "changed_value": null,
    "children": null,
    "status": "removed",
    "value": false
  },
  "host": {
    "changed_value": null,
    "children": null,
    "status": "same",
    "value": "hexlet.io"
  },
  "proxy": {
    "changed_value": null,
    "children": null,
    "status": "removed",
    "value": "123.234.53.22"
  },
  "timeout": {
    "changed_value": 20,
    "children": null,
    "status": "changed",
    "value": 50
  },
  "verbose": {
    "changed_value": null,
    "children": null,
    "status": "added",
    "value": true
  }
}"""

result_json_nested = """{
  "common": {
    "changed_value": null,
    "children": {
      "follow": {
        "changed_value": null,
        "children": null,
        "status": "added",
        "value": false
      },
      "setting1": {
        "changed_value": null,
        "children": null,
        "status": "same",
        "value": "Value 1"
      },
      "setting2": {
        "changed_value": null,
        "children": null,
        "status": "removed",
        "value": 200
      },
      "setting3": {
        "changed_value": null,
        "children": null,
        "status": "changed",
        "value": true
      },
      "setting4": {
        "changed_value": null,
        "children": null,
        "status": "added",
        "value": "blah blah"
      },
      "setting5": {
        "changed_value": null,
        "children": null,
        "status": "added",
        "value": {
          "key5": "value5"
        }
      },
      "setting6": {
        "changed_value": null,
        "children": {
          "doge": {
            "changed_value": null,
            "children": {
              "wow": {
                "changed_value": "so much",
                "children": null,
                "status": "changed",
                "value": ""
              }
            },
            "status": "same",
            "value": null
          },
          "key": {
            "changed_value": null,
            "children": null,
            "status": "same",
            "value": "value"
          },
          "ops": {
            "changed_value": null,
            "children": null,
            "status": "added",
            "value": "vops"
          }
        },
        "status": "same",
        "value": null
      }
    },
    "status": "same",
    "value": null
  },
  "group1": {
    "changed_value": null,
    "children": {
      "baz": {
        "changed_value": "bars",
        "children": null,
        "status": "changed",
        "value": "bas"
      },
      "foo": {
        "changed_value": null,
        "children": null,
        "status": "same",
        "value": "bar"
      },
      "nest": {
        "changed_value": "str",
        "children": null,
        "status": "changed",
        "value": {
          "key": "value"
        }
      }
    },
    "status": "same",
    "value": null
  },
  "group2": {
    "changed_value": null,
    "children": null,
    "status": "removed",
    "value": {
      "abc": 12345,
      "deep": {
        "id": 45
      }
    }
  },
  "group3": {
    "changed_value": null,
    "children": null,
    "status": "added",
    "value": {
      "deep": {
        "id": {
          "number": 45
        }
      },
      "fee": 100500
    }
  }
}"""
