# ----------------------------------------------------------------------------------------
# Python-Backpack - Custom Exceptions UnitTest
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------

import unittest

from backpack.cache import timed_lru_cache


class TestCache(unittest.TestCase):
    @timed_lru_cache(seconds=1)
    def test_function(self):
        """Some heavy process here to be cached."""
        return True

    def test_cache(self):
        """Testing module."""
        self.assertTrue(self.test_function())
        self.assertEqual(True, self.test_function(force_clear=True))
        self.assertEqual(True, self.test_function(force_clear=True, show_log=True))


if __name__ == '__main__':
    unittest.main()
