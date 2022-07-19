# ----------------------------------------------------------------------------------------
# Python-Backpack - Other Tests
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------

import os
import sys
import unittest

from backpack.version import app_name, version, VERSION_MAJOR, VERSION_MINOR, VERSION_PATCH

mod_path = os.path.dirname(__file__)
if mod_path not in sys.path:
    sys.path.append(mod_path)


class Test_Errors(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        pass

    def test_version(self):
        ''' testing module '''
        self.assertEqual(app_name, 'python-backpack')
        self.assertEqual(version, f'{VERSION_MAJOR}.{VERSION_MINOR}.{VERSION_PATCH}')


if __name__ == '__main__':
    unittest.main()
