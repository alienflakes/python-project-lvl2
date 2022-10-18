flat = {
    'follow': {
        'node_type': 'removed',
        'value': False,
        'changed_value': None,
        'children': None
    },
    'host': {
        'node_type': 'same',
        'value': 'hexlet.io',
        'changed_value': None,
        'children': None
    },
    'proxy': {
        'node_type': 'removed',
        'value': '123.234.53.22',
        'changed_value': None,
        'children': None
    },
    'timeout': {
        'node_type': 'updated',
        'value': 50,
        'changed_value': 20,
        'children': None
    },
    'verbose': {
        'node_type': 'added',
        'value': True,
        'changed_value': None,
        'children': None
    }
}


nested = {
    'common': {
        'node_type': 'nested',
        'value': None,
        'changed_value': None,
        'children': {
            'follow': {
                'node_type': 'added',
                'value': False,
                'changed_value': None,
                'children': None
            },
            'setting1': {
                'node_type': 'same',
                'value': 'Value 1',
                'changed_value': None,
                'children': None
            },
            'setting2': {
                'node_type': 'removed',
                'value': 200,
                'changed_value': None,
                'children': None
            },
            'setting3': {
                'node_type': 'updated',
                'value': True,
                'changed_value': None,
                'children': None
            },
            'setting4': {
                'node_type': 'added',
                'value': 'blah blah',
                'changed_value': None,
                'children': None
            },
            'setting5': {
                'node_type': 'added',
                'value': {
                    'key5': 'value5'
                },
                'changed_value': None,
                'children': None
            },
            'setting6': {
                'node_type': 'nested',
                'value': None,
                'changed_value': None,
                'children': {
                    'doge': {
                        'node_type': 'nested',
                        'value': None,
                        'changed_value': None,
                        'children': {
                            'wow': {
                                'node_type': 'updated',
                                'value': '',
                                'changed_value': 'so much',
                                'children': None
                            }
                        }
                    },
                    'key': {
                        'node_type': 'same',
                        'value': 'value',
                        'changed_value': None,
                        'children': None
                    },
                    'ops': {
                        'node_type': 'added',
                        'value': 'vops',
                        'changed_value': None,
                        'children': None
                    }
                }
            }
        }
    },
    'group1': {
        'node_type': 'nested',
        'value': None,
        'changed_value': None,
        'children': {
            'baz': {
                'node_type': 'updated',
                'value': 'bas',
                'changed_value': 'bars',
                'children': None
            },
            'foo': {
                'node_type': 'same',
                'value': 'bar',
                'changed_value': None,
                'children': None
            },
            'nest': {
                'node_type': 'updated',
                'value': {
                    'key': 'value'
                },
                'changed_value': 'str',
                'children': None
            }
        }
    },
    'group2': {
        'node_type': 'removed',
        'value': {
            'abc': 12345,
            'deep': {
                'id': 45
            }
        },
        'changed_value': None,
        'children': None
    },
    'group3': {
        'node_type': 'added',
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
    }
}
