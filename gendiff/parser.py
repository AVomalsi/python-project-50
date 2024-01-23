from json import loads
from yaml import safe_load


def read_file(file):
    with open(file, 'r') as data:
        return data.read()


def do_parse(file):
    content = read_file(file)
    if file.endswith('.json'):
        return loads(content)
    elif file.endswith('.yaml') or file.endswith('.yml'):
        return safe_load(content)
