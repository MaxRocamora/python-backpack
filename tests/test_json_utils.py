# ----------------------------------------------------------------------------------------
# Python-Backpack - TestUtils Tests
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------

import pytest

from backpack.json_utils import json_load, json_save


def test_json_load(tmp_path):
    """Test json_load function."""
    json_file = tmp_path / 'data.json'
    json_file.write_text('{"user": "Max"}')
    broken_file = tmp_path / 'broken.json'
    broken_file.write_text('{broken')

    assert json_load(str(json_file)) == {'user': 'Max'}

    with pytest.raises(OSError):
        json_load(str(tmp_path / 'missing.json'))
    with pytest.raises(OSError):
        json_load(str(broken_file))


def test_json_save(tmp_path):
    """Test json_save function."""
    data = {'name': 'max'}
    json_file = tmp_path / 'save' / 'data.json'

    assert json_save(data, str(json_file)) is True
    assert json_load(str(json_file)) == data

    assert json_save(pytest, str(tmp_path / 'invalid.json')) is False
