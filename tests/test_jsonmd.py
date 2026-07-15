# ----------------------------------------------------------------------------------------
# Python-Backpack - JsonMD Tests
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------

import json

from backpack.json_metadata import JsonMetaFile

NAME = 'test'
ATTRIBUTES = ['foo', 'bar']


def test_metadata(tmp_path):
    """Testing module."""
    meta = JsonMetaFile(NAME, str(tmp_path))

    assert meta.name == NAME

    meta.insert(key='coins', value=12)
    assert meta._data['coins'] == 12

    meta.save()
    assert meta.has_file() is True
    assert json.loads((tmp_path / meta.filename).read_text())['coins'] == 12

    meta.insert('coins', 7)
    assert meta._data['coins'] == 7

    meta.remove('coins')
    assert meta._data.get('coins', None) is None

    meta.insert(key='items', value=ATTRIBUTES)
    meta.save()

    meta_obj = meta.load_as_class()
    assert isinstance(meta_obj, type)
    assert hasattr(meta_obj, 'items') is True
    assert meta_obj.items == ATTRIBUTES

    loaded_meta = JsonMetaFile(NAME, str(tmp_path))
    loaded_meta.load()
    assert loaded_meta._data['items'] == ATTRIBUTES


def test_create_from_class(tmp_path):
    """save_from_a_class."""
    meta = JsonMetaFile(NAME, str(tmp_path))
    assert meta.name == NAME

    proxy_class = type('Proxy', (), {'foo': 12, 'items': ATTRIBUTES})
    meta.insert_class(proxy_class)
    assert meta._data['foo'] == 12
    assert meta._data['items'] == ATTRIBUTES
    meta.save()
    assert meta.has_file() is True


def test_insert_class_excludes_non_serializable_members(tmp_path):
    """Store class data without methods or descriptors that JSON cannot serialize."""

    class Proxy:
        value = 12

        @property
        def computed(self):
            return self.value

        def method(self):
            return self.value

    meta = JsonMetaFile(NAME, str(tmp_path))
    meta.insert_class(Proxy)

    assert meta._data == {'value': 12}


def test_metadata_save_creates_missing_directory(tmp_path):
    """Save should create base folder when target path does not exist."""
    base_path = tmp_path / 'missing_dir'
    meta = JsonMetaFile('missing_dir_case', str(base_path))

    assert base_path.exists() is False
    meta.save()

    assert base_path.exists() is True
    assert meta.has_file() is True
