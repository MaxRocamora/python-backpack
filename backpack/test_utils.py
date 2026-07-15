# ----------------------------------------------------------------------------------------
# Python-Backpack - Test Utilities
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------
import random
import string
import time
from functools import wraps
from typing import Callable, ParamSpec, TypeVar

from backpack.logger import get_logger

log = get_logger('Python Backpack - TestUtils')

P = ParamSpec('P')
R = TypeVar('R')


def random_string(length: int = 10) -> str:
    """Generates a random string of fixed length.

    Args:
        length (int, optional): max string length. Defaults to 10.

    Returns:
        str: random string
    """

    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def time_function_decorator(method: Callable[P, R]) -> Callable[P, R]:
    """Decorator to measure methods execution time."""

    @wraps(method)
    def timed(*args: P.args, **kw: P.kwargs) -> R:
        ts = time.perf_counter()
        result = method(*args, **kw)
        te = time.perf_counter()

        message = f'{method.__name__!r}  {(te - ts) * 1000:2.2f} ms'
        log.info(message)

        return result

    return timed
