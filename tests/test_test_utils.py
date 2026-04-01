# ----------------------------------------------------------------------------------------
# Python-Backpack - TestUtils Tests
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------

import os
import sys
import time

from backpack.test_utils import random_string, time_function_decorator

mod_path = os.path.dirname(__file__)
if mod_path not in sys.path:
    sys.path.append(mod_path)


@time_function_decorator
def one_second_delay():
    """One second delay to test time_function_decorator."""
    time.sleep(1)


def test_random_string():
    """Testing module."""
    r = random_string(10)
    assert len(r) == 10
    assert isinstance(r, str) is True
    r = random_string(0)
    assert len(r) == 0


def test_delay():
    """Testing time_function_decorator."""
    one_second_delay()
