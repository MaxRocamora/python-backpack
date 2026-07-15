# ----------------------------------------------------------------------------------------
# Python-Backpack - Other Tests
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------

import logging

from backpack.logger import get_logger
from backpack.patterns import Singleton
from backpack.test_utils import random_string
from backpack.version import VERSION_MAJOR, VERSION_MINOR, VERSION_PATCH, app_name, version


class UniqueClass(Singleton):
    def __init__(self) -> None:
        """A class that inherits from Singleton to test the singleton pattern."""
        super().__init__()


def test_version():
    """Testing module."""
    assert app_name == 'python-backpack'
    assert version == f'{VERSION_MAJOR}.{VERSION_MINOR}.{VERSION_PATCH}'


def test_logger():
    """Test logger creation."""
    log = get_logger('test')
    assert log.name == 'test'
    assert log.level == logging.DEBUG


def test_singleton():
    """Create a singleton twice and check attribute."""
    _singleton = UniqueClass()
    assert not hasattr(_singleton, 'name')
    setattr(_singleton, 'name', random_string(5))
    # create from singleton
    _singleton_b = UniqueClass()
    assert hasattr(_singleton_b, 'name')


def test_singleton_instances_are_scoped_to_subclasses():
    """Keep one instance per concrete Singleton subclass."""

    class FirstSingleton(Singleton):
        pass

    class SecondSingleton(Singleton):
        pass

    assert FirstSingleton() is FirstSingleton()
    assert SecondSingleton() is SecondSingleton()
    assert FirstSingleton() is not SecondSingleton()
