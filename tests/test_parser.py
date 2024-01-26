from gendiff.parser import do_parse


def test_do_parse():
    assert do_parse('tests/fixtures/file1.json') == {
        'host': 'hexlet.io',
        'timeout': 50,
        'proxy': '123.234.53.22',
        'follow': False
    }
    assert do_parse('tests/fixtures/file2.yml') == {
        'timeout': 20,
        'verbose': True,
        'host': 'hexlet.io'
    }
    assert isinstance(do_parse('tests/fixtures/file1.json'), dict)
