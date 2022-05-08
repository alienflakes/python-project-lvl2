"""Expected results for tests."""


result_flat = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

result_add_all = """{
  + follow: false
  + host: hexlet.io
  + proxy: 123.234.53.22
  + timeout: 50
}"""

result_remove_all = """{
  - follow: false
  - host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
}"""

result_same = """{
    host: hexlet.io
    timeout: 20
    verbose: true
}"""

test_dict1 = {
  "host": "hexlet.io",
  "timeout": 50,
  "proxy": "123.234.53.22",
  "follow": False
}

test_dict2 = {
  "timeout": 20,
  "verbose": True,
  "host": "hexlet.io"
}
