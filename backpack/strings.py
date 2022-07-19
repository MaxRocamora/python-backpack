# ----------------------------------------------------------------------------------------
# Python-Backpack - String Verification Methods
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------

import contextlib
import re


def reformat_input_string(input_string: str,
                          under_spaces: bool = True,
                          under_hyphen: bool = True) -> str:
    ''' Reformat the user input string.
        leaves only alphanumeric chars
        replaces spaces and hyphens for underscores.

    Args:
        input_string (str): input string to reformat
        under_spaces (bool, optional): replaces spaces. Defaults to True.
        under_hyphen (bool, optional): replaces hyphens. Defaults to True.

    Returns:
        str: reformatted string
    '''

    # re-encode string to valid chars
    with contextlib.suppress(UnicodeDecodeError):
        regex = re.sub('[^A-Za-z0-9 _-]+', '', input_string)

    for char in regex:

        # replacing " " for "_"
        if under_spaces and char == ' ':
            regex = regex.replace(' ', '_')

        # replacing "-" for "_"
        if under_hyphen and char == '-':
            regex = regex.replace('-', '_')

    return regex


def begin_or_end_with_numbers(input_string: str) -> bool:
    ''' Returns true if the input string begins or ends with number '''
    return _char_is_number(input_string[0]) or _char_is_number(input_string[-1])


def begin_with_number(input_string: str) -> bool:
    ''' Returns true if the input string begins with numbers '''
    return _char_is_number(input_string[0])


def has_numbers(input_string: str) -> bool:
    ''' returns true if the input string has numbers '''
    return any(_char_is_number(char) for char in input_string)


def _char_is_number(char: str) -> bool:
    ''' Check if a string is a number

    Args:
        char (str): character to evaluate

    Returns:
        bool: True if is a int
    '''

    try:
        int(char)
        return True
    except ValueError:
        return False
