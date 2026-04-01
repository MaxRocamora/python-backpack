# ----------------------------------------------------------------------------------------
# Python-Backpack - json user settings Tests
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------

import contextlib
import os
import sys

import pytest

from backpack.json_user_settings import JsonUserSettings

mod_path = os.path.dirname(__file__)
if mod_path not in sys.path:
    sys.path.append(mod_path)


# test path & name
FOLDER = 'tox_test_folder'
TEST_FOLDER = os.path.join(os.path.expanduser('~'), FOLDER)


def _cleanup_test_folder():
    """Remove test files."""
    with contextlib.suppress(OSError):
        os.remove(TEST_FOLDER)


@pytest.fixture(autouse=True)
def cleanup_test_folder():
    """Ensure tests run with a clean state and leave no temp setting file behind."""
    _cleanup_test_folder()
    yield
    _cleanup_test_folder()


def test_json_user_settings():
    """Make sure folder does not exist."""
    with contextlib.suppress(PermissionError, OSError):
        if os.path.exists(TEST_FOLDER):
            os.removedirs(TEST_FOLDER)

    # class and properties
    js = JsonUserSettings(FOLDER, 'user')
    assert js.filepath
    assert os.path.exists(js.os_user_folder)
    assert isinstance(js.user_data, dict)

    # load from a missing file
    js.filename = 'random_file'
    assert js.load_settings() is False


def test_json_settings_save():
    """Test json settings: save."""
    # save a setting
    js = JsonUserSettings(FOLDER, 'tox')
    data = {'age': 99}
    assert js.save_settings(data)

    # load it back
    js = JsonUserSettings(FOLDER, 'tox')
    data = js.load_settings()
    assert data['age'] == 99
    # save custom setting
    js.user_data = {'custom': 'value'}
    assert js.save_settings()
    # load it back
    data = js.load_settings()
    assert data['custom'] == 'value'
