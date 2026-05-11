# ----------------------------------------------------------------------------------------
# Python-Backpack - File Utilities - Ascii Files Manipulation
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------

import contextlib

from backpack.logger import get_logger

log = get_logger('Python Backpack - FileUtils')


def replace_strings_in_file(ascii_file: str, strings: list, new_string: str) -> None:
    """Opens ascii file and replaces all occurrences from strings into new_string.

    In this class we use a full path to avoid use of os.dirname, which
    causes string encode problems.

    Args:
        ascii_file: (fullpath string) file to open
        strings: (list) strings to replace
        new_string: (string) new string or path to set
    """

    # force forward slashes
    new_string = new_string.replace('\\', '/')

    log.info(f'Replacing Strings, Opening File: {ascii_file}')

    with open(ascii_file) as f:
        file_data = f.read()
        for i in strings:
            log.info('Finding: %s', i)
            log.info('Replacing for: %s', new_string)
            log.info('-' * 50)
            file_data = file_data.replace(i, new_string)

    with open(ascii_file, 'w') as f:
        f.write(file_data)
        f.close()
        log.info(f'Closing File: {ascii_file}')


def remove_line_from_file(ascii_file: str, strings: list, verbose: bool = False) -> None:
    """Removes given lines from ascii file.

    Args:
        ascii_file: (string path) ASCII file to process
        strings: (list) match lines to remove
        verbose: (bool) if true, prints removed lines
    """

    with open(ascii_file) as f:
        file_content = f.read().splitlines()

    for line in file_content:
        if verbose:
            log.info(f'Checking line: {line}')
        with contextlib.suppress(ValueError):
            if line in strings:
                if verbose:
                    log.info(f'Removing line: {line}')
                file_content.pop(file_content.index(line))

    with open(ascii_file, 'w') as f:
        contents = '\n'.join(file_content)
        f.write(contents)


def file_is_writeable(filepath: str) -> bool:
    """Checks if a file is locked and can be overwritten.

    Args:
        filepath: (str) file to check
    Returns:
        bool : true if file is writeable
    """
    try:
        with open(filepath, 'r+') as _:
            return True
    except OSError as x:
        log.warning(f'{filepath} is locked ')
        log.info(x.strerror)

    return False


def get_version_from_filename(filename: str) -> str:
    """Extracts version from filename.

    Args:
        filename: (str) file name to extract version from
    Returns:
        str : version extracted from filename

    Examples:
        get_version_from_filename('myfile_23.txt') -> '23'
        get_version_from_filename('myfile-9.txt') -> '9'
        get_version_from_filename('myfile.130.txt') -> '130'
        get_version_from_filename('myfile_v1002.txt') -> '1002'

    """

    filename_no_ext = filename.rsplit('.', 1)[0]

    # guess is the separator is an underscore, dash, dot or v, and the version is the last part before the extension
    separators = ['_', '-', '.', 'v']
    if not any(sep in filename_no_ext for sep in separators):
        log.info(f'No separator found in filename: {filename_no_ext}. Using fallback extraction.')
    else:
        for sep in separators:
            if sep in filename_no_ext:
                parts = filename_no_ext.split(sep)
                version_part = parts[-1].split('.')[0]  # Get the last part before the extension
                if version_part.replace('.', '').isdigit():  # Check if it's a valid version number
                    log.info(
                        f'Extracted version: {version_part} from filename: {filename} using separator: {sep}'
                    )
                    return version_part

    # Fallback: extract from the entire filename
    version = filename_no_ext.lstrip('v')
    version = version.replace('_', '.').replace('-', '.')
    version = version if version.replace('.', '').isdigit() else '0'
    log.info(f'Extracted version: {version} from filename: {filename}')
    return version
