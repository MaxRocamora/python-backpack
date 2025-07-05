# ----------------------------------------------------------------------------------------
# Python-Backpack - Strings UnitTest
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------

import os
import sys
import unittest

from backpack.strings import (
    begin_or_end_with_numbers,
    begin_with_number,
    camelcase_to_snakecase,
    has_numbers,
    reformat_input_string,
)

mod_path = os.path.dirname(__file__)
if mod_path not in sys.path:
    sys.path.append(mod_path)

# Tests Constants
HAS_NUMBERS_TRUE = 'blade1_runner'
HAS_NUMBERS_FALSE = 'blade_runner'
BEGIN_WITH_NUMBER_TRUE = '8blade_runner'
BEGIN_WITH_NUMBER_FALSE = 'blade_runner'
END_WITH_NUMBER_TRUE = 'blade_runner7'


REFORMAT_RESULT = 'blade_runner'
REFORMAT_REGEX = 'bla#de_runn$er'
REFORMAT_SPACE = 'blade runner'
REFORMAT_HYPHEN = 'blade-runner'
REFORMAT_BOTH = 'blade runner-2049'
REFORMAT_BOTH_RESULT = 'blade_runner_2049'


class TestStringModule(unittest.TestCase):
    def test_has_numbers(self):
        """Testing module."""
        self.assertEqual(has_numbers(HAS_NUMBERS_TRUE), True)
        self.assertEqual(has_numbers(HAS_NUMBERS_FALSE), False)

    def test_numbers(self):
        """Testing module."""
        self.assertEqual(begin_with_number(BEGIN_WITH_NUMBER_TRUE), True)
        self.assertEqual(begin_with_number(BEGIN_WITH_NUMBER_FALSE), False)

        # no numbers on ends
        self.assertEqual(begin_or_end_with_numbers(HAS_NUMBERS_FALSE), False)
        # begin with number
        self.assertEqual(begin_or_end_with_numbers(BEGIN_WITH_NUMBER_TRUE), True)
        # end with number
        self.assertEqual(begin_or_end_with_numbers(END_WITH_NUMBER_TRUE), True)

    def test_reformat(self):
        """Testing module."""
        self.assertEqual(reformat_input_string(REFORMAT_REGEX), REFORMAT_RESULT)
        self.assertEqual(reformat_input_string(REFORMAT_SPACE), REFORMAT_RESULT)
        self.assertEqual(reformat_input_string(REFORMAT_HYPHEN), REFORMAT_RESULT)
        self.assertEqual(reformat_input_string(REFORMAT_BOTH), REFORMAT_BOTH_RESULT)
        # only regex
        self.assertEqual(
            reformat_input_string(REFORMAT_BOTH, under_spaces=False, under_hyphen=False),
            REFORMAT_BOTH,
        )

    def test_camelcase_to_snakecase(self):
        """Testing module."""

        # Test case 1: Input with no uppercase characters
        input_str, expected_output = 'nocamelcase', 'nocamelcase'
        self.assertEqual(camelcase_to_snakecase(input_str), expected_output)

        # Test case 2: Input with single uppercase character
        input_str, expected_output = 'OneCamelCaseChar', 'one_camel_case_char'
        self.assertEqual(camelcase_to_snakecase(input_str), expected_output)

        # Test case 3: Input with multiple uppercase characters
        input_str, expected_output = 'MultiCamelCaseString', 'multi_camel_case_string'
        self.assertEqual(camelcase_to_snakecase(input_str), expected_output)

        # Test case 4: Input with leading and trailing underscores
        input_str, expected_output = '_CamelCase_', '_camel_case_'
        self.assertEqual(camelcase_to_snakecase(input_str), expected_output)

        # Test case 5: Input with leading and trailing underscores and lowercase
        input_str, expected_output = '_camel_Case_', '_camel_case_'
        self.assertEqual(camelcase_to_snakecase(input_str), expected_output)


if __name__ == '__main__':
    unittest.main()
