# ----------------------------------------------------------------------------------------
# Python-Backpack - Custom Exceptions UnitTest
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------

import unittest

from backpack.cache import timed_lru_cache


class Test_Cache(unittest.TestCase):

    @timed_lru_cache(seconds=1)
    def test_function(self):
        # some heavy process here to be cached
        return True

    def test_cache(self):
        ''' testing module '''
        self.assertTrue(self.test_function())
        self.assertEqual(True, self.test_function(force_clear=True))
        self.assertEqual(True, self.test_function(force_clear=True, show_log=True))


if __name__ == '__main__':
    unittest.main()
