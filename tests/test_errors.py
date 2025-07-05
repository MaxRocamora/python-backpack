# ----------------------------------------------------------------------------------------
# Python-Backpack - Custom Exceptions UnitTest
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------

import os
import sys
import unittest

from backpack.custom_errors import ApplicationNotFoundError, EnvironmentVariableNotFoundError

mod_path = os.path.dirname(__file__)
if mod_path not in sys.path:
    sys.path.append(mod_path)


def get_env_var(name: str):
    """Call for an env var or raise EnvironmentVariableNotFoundError."""
    try:
        value = os.environ[name]
    except KeyError as e:
        raise EnvironmentVariableNotFoundError(name) from e
    return value


def get_app(name: str):
    """Raisers error."""
    raise ApplicationNotFoundError(f'Background executable not found {name}')


class TestErrors(unittest.TestCase):
    def test_env_var_error(self):
        """Testing module."""
        self.assertRaises(EnvironmentVariableNotFoundError, get_env_var, 'my_env_var')
        error = EnvironmentVariableNotFoundError('my_env_var')
        self.assertEqual(str(error), error.message)

    def test_env_app_error(self):
        """Testing module."""
        self.assertRaises(ApplicationNotFoundError, get_app, 'my_app.exe')

        error = ApplicationNotFoundError('my_app.exe')
        self.assertEqual(str(error), error.message)


if __name__ == '__main__':
    unittest.main()
