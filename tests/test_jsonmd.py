# ----------------------------------------------------------------------------------------
# Python-Backpack - JsonMD Tests
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------

import contextlib
import os
import sys

from backpack.json_metadata import JsonMetaFile

mod_path = os.path.dirname(__file__)
if mod_path not in sys.path:
    sys.path.append(mod_path)


# test path & name
TEST_PATH = os.path.join(mod_path, 'test_json')
NAME = 'test'
CLASS_NAME = 'proxy'
ATTRIBUTES = ['foo', 'bar']


def test_metadata():
    """Testing module."""
    meta = JsonMetaFile(NAME, TEST_PATH)

    # test properties
    assert meta.name == NAME

    meta.insert(key='coins', value=12)

    # check if data have coins and value 12
    assert meta._data['coins'] == 12

    meta.save()

    # file was created
    assert meta.has_file() is True

    # check if file exists
    assert os.path.exists(meta.filepath) is True

    meta.insert('coins', 7)

    # check if data have coins and value 7
    assert meta._data['coins'] == 7

    meta.remove('coins')
    assert meta._data.get('coins', None) is None

    meta.insert(key='items', value=ATTRIBUTES)
    meta.save()

    # load
    meta_obj = meta.load_as_class()
    assert isinstance(meta_obj, type)
    assert hasattr(meta_obj, 'items') is True
    assert meta_obj.items == ATTRIBUTES

    # load class
    meta = JsonMetaFile(NAME, TEST_PATH)
    meta.load()


def test_create_from_class():
    """save_from_a_class."""
    meta = JsonMetaFile(NAME, TEST_PATH)
    assert meta.name == NAME

    proxy_class = type('Proxy', (), {'foo': 12, 'items': ATTRIBUTES})
    meta.insert_class(proxy_class)
    assert meta._data['foo'] == 12
    assert meta._data['items'] == ATTRIBUTES
    meta.save()
