# ----------------------------------------------------------------------------------------
# Python-Backpack - Pattern Utilities
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------
from datetime import datetime, timedelta, timezone
from functools import lru_cache, wraps
from typing import Any, Callable, Protocol, TypeVar, cast

from backpack.logger import get_logger

log = get_logger('Python Backpack - Cache')

R = TypeVar('R', covariant=True)


class TimedCachedCallable(Protocol[R]):
    """Callable returned by timed_lru_cache with cache control kwargs."""

    def __call__(
        self,
        *args: Any,
        force_clear: bool = False,
        show_log: bool = False,
        **kwargs: Any,
    ) -> R:
        """Call the cached function, optionally forcing a cache clear first."""
        ...


def timed_lru_cache(
    seconds: int,
    maxsize: int = 128,
) -> Callable[[Callable[..., R]], TimedCachedCallable[R]]:
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

    def wrapper_cache(func: Callable[..., R]) -> TimedCachedCallable[R]:
        cached_func = cast(Any, lru_cache(maxsize=maxsize)(func))
        cached_func.lifetime = timedelta(seconds=seconds)
        cached_func.expiration = datetime.now(timezone.utc) + cached_func.lifetime

        @wraps(func)
        def wrapped_func(
            *args: Any,
            force_clear: bool = False,
            show_log: bool = False,
            **kwargs: Any,
        ) -> R:
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

        return cast(TimedCachedCallable[R], wrapped_func)

    return wrapper_cache
