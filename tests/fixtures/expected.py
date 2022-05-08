"""Expected results for gendiff tests."""


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
