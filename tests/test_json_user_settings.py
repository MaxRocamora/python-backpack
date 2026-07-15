# ----------------------------------------------------------------------------------------
# Python-Backpack - json user settings Tests
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------

from pathlib import Path

import pytest

from backpack.json_user_settings import JsonUserSettings

FOLDER = 'tox_test_folder'


@pytest.fixture(autouse=True)
def settings_home(monkeypatch, tmp_path):
    """Redirect user settings into an isolated temporary home folder."""
    monkeypatch.setattr(
        JsonUserSettings,
        'os_user_folder',
        property(lambda self: str(tmp_path)),
    )
    return tmp_path


def test_json_user_settings(settings_home):
    """Make sure folder does not exist."""
    js = JsonUserSettings(FOLDER, 'user')
    assert Path(js.filepath).parent == settings_home / FOLDER
    assert settings_home.is_dir()
    assert isinstance(js.user_data, dict)

    js.filename = 'random_file'
    assert js.load_settings() is False


def test_json_settings_save(settings_home):
    """Test json settings: save."""
    js = JsonUserSettings(FOLDER, 'tox')
    data = {'age': 99}
    assert js.save_settings(data)
    assert Path(js.filepath).is_file()

    js = JsonUserSettings(FOLDER, 'tox')
    data = js.load_settings()
    assert isinstance(data, dict)
    assert data['age'] == 99

    js.user_data = {'custom': 'value'}
    assert js.save_settings()
    data = js.load_settings()
    assert isinstance(data, dict)
    assert data['custom'] == 'value'
    assert Path(js.filepath).parent == settings_home / FOLDER


def test_user_settings_creates_missing_directory(settings_home):
    """Constructor should create a settings folder when it does not exist."""
    folder_name = 'new_settings_folder'
    target_dir = settings_home / folder_name

    assert target_dir.exists() is False
    js = JsonUserSettings(folder_name, 'user')

    assert target_dir.exists() is True
    assert Path(js.filepath).parent == target_dir
