# ----------------------------------------------------------------------------------------
# Python-Backpack - FolderUtils Tests
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------

import os
import shutil
import sys

import pytest

from backpack.file_utils import (
    file_is_writeable,
    get_version_from_filename,
    remove_line_from_file,
    replace_strings_in_file,
)

mod_path = os.path.dirname(__file__)
if mod_path not in sys.path:
    sys.path.append(mod_path)

# test folders
BASE_FILE = os.path.join(mod_path, 'test_files', 'origin.txt')
EDITED_FILE = os.path.join(mod_path, 'test_files', 'edited.txt')
STRINGS = ['to be replaced!', 'also replaced']
NEW_STRING = 'REPLACED'
LOCKED_FILE = os.path.join(mod_path, 'test_files', 'locked_file.txt')
UNLOCKED_FILE = os.path.join(mod_path, 'test_files', 'unlocked_file.txt')
NO_FILE = os.path.join(mod_path, 'test_files', 'no_file.txt')


def test_replace_strings_in_file():
    """Testing module."""
    shutil.copy(BASE_FILE, EDITED_FILE)
    replace_strings_in_file(EDITED_FILE, STRINGS, NEW_STRING)


def test_remove_line_from_file():
    """Testing module."""
    source_file = os.path.join(mod_path, 'test_files', 'origin_remove.txt')
    test_file = os.path.join(mod_path, 'test_files', 'edited_remove.txt')
    shutil.copy(source_file, test_file)
    remove_line_from_file(test_file, ['REMOVE_ME', 'to be replaced!'], verbose=True)


def test_locked_file():
    """Testing module."""
    assert file_is_writeable(UNLOCKED_FILE)
    assert not file_is_writeable(NO_FILE)


@pytest.mark.parametrize(
    ('filename', 'expected_version'),
    [
        ('myfile_23.txt', '23'),
        ('myfile-9.txt', '9'),
        ('myfile.130.txt', '130'),
        ('myfile_v1002.txt', '1002'),
        ('name_without_separator.txt', '0'),
        ('v42.txt', '42'),
        ('myfile-alpha.txt', '0'),
        ('myfile.txt', '0'),
        ('mod_asset.1004.ma', '1004'),
        ('script_nuke_s100_v1005.ma', '1005'),
    ],
)
def test_get_version_from_filename(filename: str, expected_version: str):
    """Version extraction should handle supported separators and invalid values."""
    assert get_version_from_filename(filename) == expected_version
