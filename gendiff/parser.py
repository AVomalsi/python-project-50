from json import loads
from yaml import safe_load


def do_parse(content):
    if content.endswith('.json'):
        with open(content, 'r') as f:
            return loads(f.read())
    elif content.endswith('.yaml') or content.endswith('.yml'):
        with open(content, 'r') as f:
            return safe_load(f.read())
