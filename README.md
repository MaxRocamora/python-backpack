[![PyPI Supported Python Versions](https://img.shields.io/pypi/pyversions/python-backpack.svg?style=flat-square&logo=appveyor)](https://pypi.python.org/pypi/python-backpack/)
[![PyPI version](https://badge.fury.io/py/python-backpack.svg?style=flat-square&logo=appveyor)](https://badge.fury.io/py/python-backpack)
[![GitHub version](https://badge.fury.io/gh/MaxRocamora%2Fpython-backpack.svg?style=flat-square&logo=appveyor)](https://badge.fury.io/gh/MaxRocamora%2Fpython-backpack)
[![codecov](https://codecov.io/gh/MaxRocamora/python-backpack/branch/main/graph/badge.svg?token=6D1xwYdXW2)](https://codecov.io/gh/MaxRocamora/python-backpack)


# Python-Backpack
A collection of personal scripts for json, File/Folder Operations, String Validation, Custom Errors, Cache and stuff.  


## Cache
+ timed_lru_cache()  
    *Lru_cache decorator with expiration time.*

## Custom Errors
+ EnvironmentVariableNotFound()  
*Error Raised when a required environment variable is missing from os.*
+ ApplicationNotFound()  
*Error Raised when an Application Name required is not found.*

## File Utils
+ replace_strings_in_file()  
*Opens a file and replaces all occurrences from strings into a new string.*
+ remove_line_from_file()  
*Removes given list of lines from ascii file*
+ file_is_writeable()  
*Checks if a file is writeable, returns True if it is, False otherwise.*

## Folder Utils
+ browse_folder()  
*Open windows explorer on folder*
+ create_folders()  
*Create multiple folders in a given path*
+ create_folder()  
*Create a folder in a given path, can remove old folder*
+ remove_files_in_dir()  
*Remove all files in a directory, can remove subdirectories too*
+ recursive_dir_copy()  
*Copy all files src dir to dest dir, including sub-directories.*


## Json Metadata
+ JsonMetaFile()  
    *saves/load a class/dict as a json metadata file*

## Json User Settings
+ JsonUserSettings()  
    *Class to manage load/save settings in a JSON file on local user folder*

## Json Utils
+ json_load()  
    *Function to load a JSON file with validation.*
+ json_save()  
    *Function to save a JSON file with validation.*

## Patterns
+ Singleton(): *Singleton pattern implementation.*

## String Validation
+ reformat_input_string()  
*Function to reformat an input string, leaves only alphanumeric chars and replaces spaces and hyphens for underscores.*

+ begin_or_end_with_numbers()  
*Function to check if a string begins or ends with numbers.*

+ begin_with_number()   
*Function to check if a string begins with a number.*

+ has_numbers()  
*Function to check if a string contains numbers.*

+ camelcase_to_snakecase()  
*Function to convert a camelCase string to snake_case.*

## Test Utils
+ time_function_decorator()  
*Decorator to measure the execution time of a function.*
+ random_string()  
*Generate a random string of a given length.*


---

### pip install
pip install python-backpack

