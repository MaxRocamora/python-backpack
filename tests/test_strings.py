# ----------------------------------------------------------------------------------------
# Python-Backpack - Strings UnitTest
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------

import os
import sys

import pytest

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


@pytest.mark.parametrize(
    ('value', 'expected'),
    [
        (HAS_NUMBERS_TRUE, True),
        (HAS_NUMBERS_FALSE, False),
    ],
    ids=['contains-number', 'no-number'],
)
def test_has_numbers(value, expected):
    """Testing module."""
    assert has_numbers(value) is expected


@pytest.mark.parametrize(
    ('value', 'expected'),
    [
        (BEGIN_WITH_NUMBER_TRUE, True),
        (BEGIN_WITH_NUMBER_FALSE, False),
    ],
    ids=['starts-with-number', 'starts-with-letter'],
)
def test_begin_with_number(value, expected):
    """Testing module."""
    assert begin_with_number(value) is expected


@pytest.mark.parametrize(
    ('value', 'expected'),
    [
        (HAS_NUMBERS_FALSE, False),
        (BEGIN_WITH_NUMBER_TRUE, True),
        (END_WITH_NUMBER_TRUE, True),
    ],
    ids=['number-in-middle-only', 'number-at-start', 'number-at-end'],
)
def test_begin_or_end_with_numbers(value, expected):
    """Testing module."""
    assert begin_or_end_with_numbers(value) is expected


@pytest.mark.parametrize(
    ('value', 'kwargs', 'expected'),
    [
        (REFORMAT_REGEX, {}, REFORMAT_RESULT),
        (REFORMAT_SPACE, {}, REFORMAT_RESULT),
        (REFORMAT_HYPHEN, {}, REFORMAT_RESULT),
        (REFORMAT_BOTH, {}, REFORMAT_BOTH_RESULT),
        (REFORMAT_BOTH, {'under_spaces': False, 'under_hyphen': False}, REFORMAT_BOTH),
    ],
    ids=[
        'regex-cleanup',
        'space-to-underscore',
        'hyphen-to-underscore',
        'space-and-hyphen',
        'keep-separators',
    ],
)
def test_reformat(value, kwargs, expected):
    """Testing module."""
    assert reformat_input_string(value, **kwargs) == expected


@pytest.mark.parametrize(
    ('input_str', 'expected_output'),
    [
        ('nocamelcase', 'nocamelcase'),
        ('OneCamelCaseChar', 'one_camel_case_char'),
        ('MultiCamelCaseString', 'multi_camel_case_string'),
        ('_CamelCase_', '_camel_case_'),
        ('_camel_Case_', '_camel_case_'),
    ],
    ids=[
        'already-snake',
        'single-camel',
        'multi-camel',
        'wrapped-underscore',
        'mixed-underscore-camel',
    ],
)
def test_camelcase_to_snakecase(input_str, expected_output):
    """Testing module."""
    assert camelcase_to_snakecase(input_str) == expected_output
