# ----------------------------------------------------------------------------------------
# Python-Backpack - Other Tests
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------

import logging
import os
import sys
import unittest

from backpack.logger import get_logger
from backpack.patterns import Singleton
from backpack.test_utils import random_string
from backpack.version import VERSION_MAJOR, VERSION_MINOR, VERSION_PATCH, app_name, version

mod_path = os.path.dirname(__file__)
if mod_path not in sys.path:
    sys.path.append(mod_path)


class UniqueClass(Singleton):
    def __init__(self) -> None:
        """A class that inherits from Singleton to test the singleton pattern."""
        super().__init__()


class TestErrors(unittest.TestCase):
    @classmethod
    def tearDownClass(cls):
        """Closing test."""
        pass

    def test_version(self):
        """Testing module."""
        self.assertEqual(app_name, 'python-backpack')
        self.assertEqual(version, f'{VERSION_MAJOR}.{VERSION_MINOR}.{VERSION_PATCH}')

    def test_logger(self):
        """Test logger creation."""
        log = get_logger('test')
        self.assertEqual(log.name, 'test')
        self.assertEqual(log.level, logging.DEBUG)

    def test_singleton(self):
        """Create a singleton twice and check attribute."""
        _singleton = UniqueClass()
        self.assertFalse(hasattr(_singleton, 'name'))
        _singleton.name = random_string(5)
        # create from singleton
        _singleton_b = UniqueClass()
        self.assertTrue(hasattr(_singleton_b, 'name'))


if __name__ == '__main__':
    unittest.main()
