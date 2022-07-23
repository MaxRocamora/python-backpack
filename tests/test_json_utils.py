# ----------------------------------------------------------------------------------------
# Python-Backpack - TestUtils Tests
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------

import os
import sys
import unittest

from backpack.folder_utils import remove_files_in_dir
from backpack.json_utils import json_load, json_save

mod_path = os.path.dirname(__file__)
if mod_path not in sys.path:
    sys.path.append(mod_path)

NO_FILE = os.path.join(mod_path, 'test_files', 'no_file.json')
JSON_FILE = os.path.join(mod_path, 'test_files', 'data.json')
JSON_SAVE_FILE = os.path.join(mod_path, 'test_files', 'save', 'data_saved.json')
BROKEN_JSON_FILE = os.path.join(mod_path, 'test_files', 'data_broken.json')


class Test_Errors(unittest.TestCase):

    def test_json_open(self):
        ''' testing module '''
        data = json_load(JSON_FILE)
        self.assertTrue(type(data), dict)
        self.assertTrue(data.get('user'), 'Max')
        self.assertRaises(OSError, json_load, NO_FILE)
        self.assertRaises(OSError, json_load, BROKEN_JSON_FILE)

    def test_json_save(self):
        data = {'name': 'max'}
        r = json_save(data, JSON_SAVE_FILE)
        self.assertTrue(r)
        remove_files_in_dir(os.path.dirname(JSON_SAVE_FILE))
        os.removedirs(os.path.dirname(JSON_SAVE_FILE))


if __name__ == '__main__':
    unittest.main()
