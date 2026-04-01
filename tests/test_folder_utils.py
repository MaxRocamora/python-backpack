# ----------------------------------------------------------------------------------------
# Python-Backpack - FolderUtils Tests
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------

import os
import sys
from unittest import mock


from backpack.folder_utils import (
    browse_folder,
    create_folder,
    create_folders,
    recursive_dir_copy,
    remove_files_in_dir,
)

mod_path = os.path.dirname(__file__)
if mod_path not in sys.path:
    sys.path.append(mod_path)

# test folders
BASE_PATH = os.path.join(mod_path, 'test_folder')
FOLDERS = [
    os.path.join(BASE_PATH, 'ALPHA'),
    os.path.join(BASE_PATH, 'BETA'),
]
FOLDER_FILES = os.path.join(BASE_PATH, 'files')
FILES = ['readme.txt']


def create_file(path):
    """Creates a temp txt file."""
    with open(os.path.join(path, 'temp.txt'), 'w'):
        pass


def test_create_folders():
    """Testing module."""
    create_folders(FOLDERS, verbose=True)
    # check folders and files exists
    for f in FOLDERS:
        assert os.path.exists(f) is True

    # delete folders
    remove_files_in_dir(BASE_PATH)

    create_folders(FOLDERS, verbose=True, force_empty=True)
    # check folders and files exists
    for f in FOLDERS:
        assert os.path.exists(f) is True

    # test osError
    create_folder('X:/tests/force_oserror')

    # test force_empty, calling twice to ensure folder existence
    create_folders(FOLDERS, verbose=True, force_empty=False)
    create_folders(FOLDERS, verbose=True, force_empty=True)

    # delete folders
    remove_files_in_dir(BASE_PATH)


@mock.patch('subprocess.Popen')
def test_browse(mock_browse):
    """Testing module."""
    # mocked Popen, create folder, browse, delete
    create_folder(FOLDERS[0])
    browse_folder(FOLDERS[0])
    # force false
    browse_folder(None)


def test_remove_dir():
    """Creates a folder with files and remove it."""
    test_dir = os.path.join(BASE_PATH, 'remove_dir')
    create_folder(test_dir)
    create_file(test_dir)
    remove_files_in_dir(test_dir)


def test_recursive_dir():
    """Creates a dir with sub dirs and files and copy them."""
    test_dir = os.path.join(BASE_PATH, 'recursive_dir')
    create_folder(test_dir)
    create_file(test_dir)
    sub_dir = os.path.join(test_dir, 'recursive_sub_dir')
    create_folder(sub_dir)
    create_file(sub_dir)
    target_dir = os.path.join(BASE_PATH, 'recursive_target')
    recursive_dir_copy(test_dir, target_dir)
    # clear everything
    remove_files_in_dir(test_dir)
    remove_files_in_dir(sub_dir)
    remove_files_in_dir(target_dir)
