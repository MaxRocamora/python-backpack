# ----------------------------------------------------------------------------------------
# Python-Backpack - File Utilities
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------

import os
import shutil
import subprocess

from backpack.logger import get_logger

log = get_logger('FileUtils')


def browse_folder(folder: str) -> bool:
    ''' Open windows explorer on folder
    Args:
        folder (path) folder to open
    '''
    if folder and os.path.isdir(folder):
        subprocess.Popen(f"explorer {os.path.abspath(folder)}")
        return True

    log.warning(f"Unable to open folder {folder}")
    return False


def create_folders(folders: list, force_empty: bool = False, verbose: bool = False):
    ''' Creates multiple folders on disc.

    Args:
        folders (list): folder list
        force_empty (bool, optional): _description_. Defaults to False.
        verbose (bool, optional):shows log. Defaults to False.
    '''
    for folder in folders:
        create_folder(folder, force_empty=force_empty, verbose=verbose)


def create_folder(path: str, force_empty: bool = False, verbose: bool = True):
    '''_summary_

    Args:
        path (str): _description_
        force_empty (bool, optional): _description_. Defaults to False.
        verbose (bool, optional): _description_. Defaults to True.
    '''
    abspath = os.path.abspath(path)
    if verbose:
        log.info(f'Creating Folder {abspath}')

    try:
        if not os.path.exists(abspath):
            os.makedirs(f'{abspath}/')
        elif force_empty:
            remove_files_in_dir(abspath)
    except OSError as e:
        log.warning(f"Unable to create folder: {path}")
        log.error(str(e))

    return True


def remove_files_in_dir(path):
    ''' clears all content in given directory '''
    for root, dirs, files in os.walk(path):
        for f in files:
            os.unlink(os.path.join(root, f))
        for d in dirs:
            shutil.rmtree(os.path.join(root, d))
