# ----------------------------------------------------------------------------------------
# Python-Backpack - Custom Exceptions UnitTest
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------

from backpack.cache import timed_lru_cache


@timed_lru_cache(seconds=1)
def cached_test_function():
    """Some heavy process here to be cached."""
    return True


def test_cache():
    """Testing module."""
    assert cached_test_function()
    assert cached_test_function(force_clear=True) is True
    assert cached_test_function(force_clear=True, show_log=True) is True
