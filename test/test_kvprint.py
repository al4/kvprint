import logging
from six import string_types

from kvprint import kvstring, kvalign, kvprint

logging.basicConfig(level=logging.DEBUG)


def test_kvalign_returns_list():
    assert isinstance(kvalign({'foo': 'bar'}), list)


def test_kvalign_returns_empty_list_for_empty_dict():
    assert isinstance(kvalign({}), list)
    assert len(kvalign({})) == 0


def test_kvstring_returns_string():
    out = kvstring({'foo': 'bar'})
    print(out)
    assert type(out) in string_types
