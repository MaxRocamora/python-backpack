# ----------------------------------------------------------------------------------------
# Python-Backpack - File Utilities - Ascii Files Manipulation
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------

import os
import contextlib

from backpack.logger import get_logger

log = get_logger('FileUtils')


def replace_strings_in_file(ascii_file: str, strings: list, new_string: str):
    ''' Opens ascii file and replaces all occurrences from strings into new_string.
    In this class we use a full path to avoid use of os.dirname, dirname, which
    causes string encode problems.
    Args:
        ascii_file (fullpath) file to open
        strings (list) strings to replace
        new_string (string) new string or path to set
    '''
    if not strings:
        return False

    log.process('Replacing Strings...')

    new_string = new_string.replace("\\", "/")

    log.info("Opening File: %s", ascii_file)

    with open(ascii_file) as f:
        file_data = f.read()
        for i in strings:
            source = i.replace("\\", "/")
            filename = os.path.split(source)[1]
            target = os.path.join(new_string, str(filename))
            target = target.replace("\\", "/")
            log.info('Finding: %s', source)
            log.info('Replacing for: %s', target)
            log.info('-' * 50)
            try:
                file_data = file_data.replace(source, target)
            except UnicodeDecodeError as e:
                log.info('Skipping RePath due to this error.')
                log.info('UnicodeDecodeError: %s', str(e))

    with open(ascii_file, 'w') as f:
        f.write(file_data)
        f.close()
        log.info(f"Closing File: {ascii_file}")


def remove_strings_from_file(ascii_file: str, strings: str):
    '''
    removes given string list from to file.
    Args:
        ascii_file (path) ASCII File to process
        strings (path) List of lines to remove
    '''
    with open(strings) as fileData:
        stringList = fileData.read().splitlines()

    fileData = None
    with open(ascii_file) as fileData:
        fileData = fileData.read().splitlines()

    for line in stringList:
        with contextlib.suppress(ValueError):
            if line in fileData:
                fileData.pop(fileData.index(line))
    with open(ascii_file, "w") as f:
        contents = "\n".join(fileData)
        f.write(contents)
