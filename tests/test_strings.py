# ----------------------------------------------------------------------------------------
# Python-Backpack - Strings UnitTest
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------

import os
import sys
import unittest

from backpack.strings import has_numbers, begin_with_number, begin_or_end_with_numbers

mod_path = os.path.dirname(__file__)
if mod_path not in sys.path:
    sys.path.append(mod_path)

HAS_NUMBERS_TRUE = 'blade1_runner'
HAS_NUMBERS_FALSE = 'blade_runner'
BEGIN_WITH_NUMBER_TRUE = '8blade_runner'
BEGIN_WITH_NUMBER_FALSE = 'blade_runner'
END_WITH_NUMBER_TRUE = 'blade_runner7'


class Test_Errors(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        pass

    def test_has_numbers(self):
        ''' testing module '''
        self.assertEqual(has_numbers(HAS_NUMBERS_TRUE), True)
        self.assertEqual(has_numbers(HAS_NUMBERS_FALSE), False)

    def test_numbers(self):
        ''' testing module '''
        self.assertEqual(begin_with_number(BEGIN_WITH_NUMBER_TRUE), True)
        self.assertEqual(begin_with_number(BEGIN_WITH_NUMBER_FALSE), False)

        # no numbers on ends
        self.assertEqual(begin_or_end_with_numbers(HAS_NUMBERS_FALSE), False)
        # begin with number
        self.assertEqual(begin_or_end_with_numbers(BEGIN_WITH_NUMBER_TRUE), True)
        # end with number
        self.assertEqual(begin_or_end_with_numbers(END_WITH_NUMBER_TRUE), True)


if __name__ == '__main__':
    unittest.main()
