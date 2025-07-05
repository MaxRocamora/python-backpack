# ----------------------------------------------------------------------------------------
# Python-Backpack - FolderUtils Tests
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------

import os
import shutil
import sys
import unittest

from backpack.file_utils import file_is_writeable, remove_line_from_file, replace_strings_in_file

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


class TestErrors(unittest.TestCase):
    def test_replace_strings_in_file(self):
        """Testing module."""
        shutil.copy(BASE_FILE, EDITED_FILE)
        replace_strings_in_file(EDITED_FILE, STRINGS, NEW_STRING)

    def test_remove_line_from_file(self):
        """Testing module."""
        source_file = os.path.join(mod_path, 'test_files', 'origin_remove.txt')
        test_file = os.path.join(mod_path, 'test_files', 'edited_remove.txt')
        shutil.copy(source_file, test_file)
        remove_line_from_file(test_file, ['REMOVE_ME', 'to be replaced!'], verbose=True)

    def test_locked_file(self):
        """Testing module."""
        self.assertTrue(file_is_writeable(UNLOCKED_FILE))
        self.assertFalse(file_is_writeable(NO_FILE))


if __name__ == '__main__':
    unittest.main()
