# ----------------------------------------------------------------------------------------
# Python-Backpack - FolderUtils Tests
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------

import os
import sys
import unittest
import mock

from backpack.folder_utils import create_folders, browse_folder, create_folder
from backpack.folder_utils import remove_files_in_dir

mod_path = os.path.dirname(__file__)
if mod_path not in sys.path:
    sys.path.append(mod_path)

# test folders
BASE_PATH = os.path.join(mod_path, 'test_folder')
FOLDERS = [os.path.join(BASE_PATH, 'ALPHA'),
           os.path.join(BASE_PATH, 'BETA'),
           ]
FOLDER_FILES = os.path.join(BASE_PATH, 'files')
FILES = ['readme.txt']


class Test_Errors(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        pass

    def test_folders(self):
        ''' testing module '''
        create_folders(FOLDERS, verbose=True)
        # check folders and files exists
        for f in FOLDERS:
            self.assertEqual(os.path.exists(f), True)

        # delete folders
        remove_files_in_dir(BASE_PATH)

        create_folders(FOLDERS, verbose=True, force_empty=True)
        # check folders and files exists
        for f in FOLDERS:
            self.assertEqual(os.path.exists(f), True)

        # test osError
        create_folder('X:/force_oserror')

        # test force_empty, calling twice to ensure folder existence
        create_folders(FOLDERS, verbose=True, force_empty=False)
        create_folders(FOLDERS, verbose=True, force_empty=True)

        # delete folders
        remove_files_in_dir(BASE_PATH)

    @mock.patch('subprocess.Popen')
    def test_browse(self, mock_browse):
        # mocked Popen, create folder, browse, delete
        create_folder(FOLDERS[0])
        browse_folder(FOLDERS[0])
        remove_files_in_dir(BASE_PATH)
        # force false
        browse_folder(None)

    def test_remove_dir(self):
        ''' creates a folder with files and remove it '''
        create_folder(FOLDER_FILES)
        with open(os.path.join(FOLDER_FILES, 'myfile.txt'), 'w'):
            pass
        remove_files_in_dir(FOLDER_FILES)


if __name__ == '__main__':
    unittest.main()
