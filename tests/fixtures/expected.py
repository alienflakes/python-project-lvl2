"""Expected results for gendiff tests."""


result_json_flat = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""

result_json_empty = """{

}"""

result_json_add_all = """{
  + host: hexlet.io
  + timeout: 20
  + verbose: true
}"""

result_json_remove_all = """{
  - follow: false
  - host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
}"""
