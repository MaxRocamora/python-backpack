# ----------------------------------------------------------------------------------------
# Python-Backpack - TestUtils Tests
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------

from backpack.test_utils import random_string, time_function_decorator


@time_function_decorator
def decorated_double(value: int) -> int:
    """Double a value for decorator behavior tests."""
    return value * 2


def test_random_string():
    """Testing module."""
    r = random_string(10)
    assert len(r) == 10
    assert isinstance(r, str) is True
    r = random_string(0)
    assert len(r) == 0


def test_time_function_decorator_preserves_return_value():
    """Return the wrapped function's result unchanged."""
    assert decorated_double(4) == 8


def test_time_function_decorator_preserves_metadata():
    """Expose the wrapped function's name and docstring."""
    assert decorated_double.__name__ == 'decorated_double'
    assert decorated_double.__doc__ == 'Double a value for decorator behavior tests.'
