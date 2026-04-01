# ----------------------------------------------------------------------------------------
# Python-Backpack - Pattern Utilities
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------
from datetime import datetime, timedelta, timezone
from functools import lru_cache, wraps
from typing import Any, Callable, TypeVar, cast

from backpack.logger import get_logger

log = get_logger('Python Backpack - Cache')

F = TypeVar('F', bound=Callable[..., Any])


def timed_lru_cache(seconds: int, maxsize: int = 128) -> Callable[[F], F]:
    """Lru_cache with expiration time.

    Args:
        seconds (int): expiration time in seconds
        maxsize (int): maxsize for lru_cache
    Note:
        Wrapped function can be forced to clear cache with: force_clear=True
        Wrapped function can show log on clear with: show_log=True
    Returns:
        function result

    # * Usage:

        # * Add the decorator to your function

        @timed_lru_cache(seconds=60)
        def my_function():
            return 'Hello World'

        # * to clear the cache, use force_clear=True on the function call
        my_function(force_clear=True)

    """

    def wrapper_cache(func: F) -> F:
        cached_func = cast(Any, lru_cache(maxsize=maxsize)(func))
        cached_func.lifetime = timedelta(seconds=seconds)
        cached_func.expiration = datetime.now(timezone.utc) + cached_func.lifetime

        @wraps(func)
        def wrapped_func(*args, force_clear: bool = False, show_log: bool = False, **kwargs):
            """Wrapper function for lru_cache with expiration time.

            Args:
                *args: function arguments
                force_clear (bool): forces a clear cache
                show_log (bool): show log on clear
                **kwargs: function keyword arguments
            Returns:
                function result
            """

            if force_clear or datetime.now(timezone.utc) >= cached_func.expiration:
                if show_log:
                    log.debug(f'Cache cleared for {cached_func.__name__}')

                cached_func.cache_clear()
                cached_func.expiration = datetime.now(timezone.utc) + cached_func.lifetime

            return cached_func(*args, **kwargs)

        return cast(F, wrapped_func)

    return wrapper_cache
