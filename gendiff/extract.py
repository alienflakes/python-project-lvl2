import os


def read_file(file_path: str):
    if not os.path.isabs(file_path):
        file_path = os.path.abspath(file_path)
    with open(file_path) as file:
        return file.read()


def get_extension(file_path: str) -> str:
    return os.path.splitext(file_path)[1]
