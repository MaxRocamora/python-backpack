[![PyPI Supported Python Versions](https://img.shields.io/pypi/pyversions/python-backpack.svg?style=flat-square&logo=appveyor)](https://pypi.python.org/pypi/python-backpack/)
[![PyPI version](https://badge.fury.io/py/python-backpack.svg?style=flat-square&logo=appveyor)](https://badge.fury.io/py/python-backpack)
[![GitHub version](https://badge.fury.io/gh/MaxRocamora%2Fpython-backpack.svg?style=flat-square&logo=appveyor)](https://badge.fury.io/gh/MaxRocamora%2Fpython-backpack)
[![codecov](https://codecov.io/gh/MaxRocamora/python-backpack/graph/badge.svg?token=6D1xwYdXW2)](https://codecov.io/gh/MaxRocamora/python-backpack)


# Python-Backpack

Python-Backpack is a lightweight utility collection for common scripting tasks:

- JSON load/save helpers with validation
- user settings persistence under the OS user directory
- metadata export/import to JSON files
- file and folder operations
- string normalization and case conversion
- cache decorator with expiration support
- custom exceptions, logging helper, singleton pattern, and testing helpers

## Compatibility

- Python 3.11+

## Installation

```bash
pip install python-backpack
```

## Package API Reference

### Cache (`backpack.cache`)

- `timed_lru_cache(seconds: int, maxsize: int = 128)`
    - `functools.lru_cache` decorator with expiration time.
    - Wrapped calls support `force_clear=True` and `show_log=True`.

### Custom Errors (`backpack.custom_errors`)

- `EnvironmentVariableNotFoundError(var_name: str)`
    - Raised when a required environment variable is missing.
- `ApplicationNotFoundError(app_name: str)`
    - Raised when a required application is not found.

### File Utils (`backpack.file_utils`)

- `replace_strings_in_file(ascii_file: str, strings: list, new_string: str) -> None`
    - Replaces multiple string occurrences in a text file.
- `remove_line_from_file(ascii_file: str, strings: list, verbose: bool = False) -> None`
    - Removes exact matching lines from a text file.
- `file_is_writeable(filepath: str) -> bool`
    - Checks whether a file can be opened for read/write.
- `get_version_from_filename(filename: str) -> str`
    - Extracts a numeric version token from a filename.

### Folder Utils (`backpack.folder_utils`)

- `browse_folder(folder: str) -> bool`
    - Opens a folder in Windows Explorer.
- `create_folders(folders: list, force_empty: bool = False, verbose: bool = False)`
    - Creates multiple folders.
- `create_folder(path: str, force_empty: bool = False, verbose: bool = True)`
    - Creates a folder and optionally clears it if it already exists.
- `remove_files_in_dir(path: str)`
    - Removes all files and subdirectories inside a directory.
- `recursive_dir_copy(source_path: str, target_path: str)`
    - Recursively copies files and subfolders from source to target.

### JSON Utils (`backpack.json_utils`)

- `json_load(json_file: str) -> dict`
    - Loads JSON data from file with validation and error handling.
- `json_save(data: dict, json_file: str) -> bool`
    - Saves a dictionary to JSON file.

### JSON Metadata (`backpack.json_metadata`)

- `JsonMetaFile(name: str, path: str)`
    - Manages a metadata JSON file with package/system/time information.
    - Main public methods:
        - `has_file() -> bool`
        - `load() -> None`
        - `insert(key: str, value: Any) -> None`
        - `remove(key: str) -> None`
        - `save() -> None`
        - `load_as_class() -> type`
        - `insert_class(_class: type) -> None`

### JSON User Settings (`backpack.json_user_settings`)

- `JsonUserSettings(folder: str, name: str)`
    - Saves and loads JSON settings in the current user's home directory.
    - Main public methods:
        - `save_settings(data: dict | None = None) -> bool | None`
        - `load_settings() -> dict | bool`

### Logger (`backpack.logger`)

- `get_logger(name: str) -> logging.Logger`
    - Returns a configured logger with stream handler.

### Patterns (`backpack.patterns`)

- `Singleton`
    - Base class implementing singleton behavior via `__new__`.

### Strings (`backpack.strings`)

- `normalize_input_string(input_string: str, under_spaces: bool = True, under_hyphen: bool = True, replacer: str = '_') -> str`
    - Keeps alphanumeric/space/hyphen characters and normalizes separators.
- `begin_or_end_with_numbers(input_string: str) -> bool`
    - Checks whether first or last character is numeric.
- `begin_with_number(input_string: str) -> bool`
    - Checks whether the first character is numeric.
- `has_numbers(input_string: str) -> bool`
    - Checks whether any character is numeric.
- `camelcase_to_snakecase(input_string: str) -> str`
    - Converts CamelCase to snake_case.
    - Handles acronym prefixes, for example `HTTPServer -> http_server`.

### Test Utils (`backpack.test_utils`)

- `random_string(length: int = 10) -> str`
    - Generates a random lowercase string.
- `time_function_decorator(method: type)`
    - Decorator that logs execution time.

## Quick Example

```python
from backpack.cache import timed_lru_cache
from backpack.strings import camelcase_to_snakecase, normalize_input_string
from backpack.json_utils import json_save, json_load


@timed_lru_cache(seconds=60)
def expensive_call():
        return {'ok': True}


value = camelcase_to_snakecase('HTTPServer')
clean = normalize_input_string('Blade Runner-2049')

json_save({'value': value, 'clean': clean}, 'data.json')
data = json_load('data.json')
```

