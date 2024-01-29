from gendiff.parser import parse_file


def test_parse_file():
    assert parse_file('tests/fixtures/file1.json') == {
        'host': 'hexlet.io',
        'timeout': 50,
        'proxy': '123.234.53.22',
        'follow': False
    }
    assert parse_file('tests/fixtures/file2.yml') == {
        'timeout': 20,
        'verbose': True,
        'host': 'hexlet.io'
    }
    assert isinstance(parse_file('tests/fixtures/file1.json'), dict)
