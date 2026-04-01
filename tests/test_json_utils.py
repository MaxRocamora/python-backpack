# ----------------------------------------------------------------------------------------
# Python-Backpack - TestUtils Tests
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------

import os
import sys

import pytest

from backpack.folder_utils import remove_files_in_dir
from backpack.json_utils import json_load, json_save

mod_path = os.path.dirname(__file__)
if mod_path not in sys.path:
    sys.path.append(mod_path)

NO_FILE = os.path.join(mod_path, 'test_json', 'no_file.json')
JSON_LOAD_FILE = os.path.join(mod_path, 'test_json', 'data.json')
JSON_SAVE_FILE = os.path.join(mod_path, 'test_json', 'save', 'data_saved.json')
BROKEN_JSON_FILE = os.path.join(mod_path, 'test_json', 'data_broken.json')


def test_json_load():
    """Test json_load function."""
    data = json_load(JSON_LOAD_FILE)
    assert isinstance(data, dict)
    assert data.get('user') == 'Max'
    with pytest.raises(OSError):
        json_load(NO_FILE)
    with pytest.raises(OSError):
        json_load(BROKEN_JSON_FILE)


def test_json_save():
    """Test json_save function."""
    data = {'name': 'max'}
    r = json_save(data, JSON_SAVE_FILE)
    assert r
    # remove files
    remove_files_in_dir(os.path.dirname(JSON_SAVE_FILE))
    os.removedirs(os.path.dirname(JSON_SAVE_FILE))

    # force error
    assert json_save(pytest, JSON_SAVE_FILE) is False
