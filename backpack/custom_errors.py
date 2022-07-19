# ----------------------------------------------------------------------------------------
# Python-Backpack - Custom Exceptions
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------

class EnvironmentVariableNotFound(Exception):
    '''Raise when a required environment variable os not found.
    Args:
        var_name (str) name of the required variable missing
    '''

    def __init__(self, var_name):
        self.var_name = var_name
        self.message = f'System required ({var_name}) Environment Variable not found.'
        super().__init__(self.message)

    def __str__(self):
        return self.message


class ApplicationNotFound(Exception):
    '''Raise when a background application is not found.'''

    def __init__(self, var_name):
        self.var_name = var_name
        self.message = f'Application ({var_name}) not found.'
        super().__init__(self.message)

    def __str__(self):
        return self.message
