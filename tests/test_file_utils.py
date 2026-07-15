# ----------------------------------------------------------------------------------------
# Python-Backpack - FolderUtils Tests
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------

import pytest

from backpack.file_utils import (
    file_is_writeable,
    get_version_from_filename,
    remove_line_from_file,
    replace_strings_in_file,
)

STRINGS = ['to be replaced!', 'also replaced']
NEW_STRING = 'REPLACED'


def test_replace_strings_in_file(tmp_path):
    """Replace every configured string and preserve unrelated content."""
    test_file = tmp_path / 'replace.txt'
    test_file.write_text('keep\nto be replaced!\nalso replaced\n')

    replace_strings_in_file(str(test_file), STRINGS, NEW_STRING)

    assert test_file.read_text() == 'keep\nREPLACED\nREPLACED\n'


def test_remove_line_from_file(tmp_path):
    """Remove exact matching lines and retain other lines."""
    test_file = tmp_path / 'remove.txt'
    test_file.write_text('keep\nREMOVE_ME\nstay')

    remove_line_from_file(str(test_file), ['REMOVE_ME'], verbose=True)

    assert test_file.read_text() == 'keep\nstay'


def test_remove_line_from_file_removes_adjacent_matches(tmp_path):
    """Remove adjacent targets, including duplicate exact matches."""
    test_file = tmp_path / 'duplicates.txt'
    test_file.write_text('REMOVE_ME\nREMOVE_ME\nALSO_REMOVE\nkeep')

    remove_line_from_file(str(test_file), ['REMOVE_ME', 'ALSO_REMOVE'])

    assert test_file.read_text() == 'keep'


def test_remove_line_from_file_preserves_line_endings(tmp_path):
    """Preserve mixed line endings on retained lines."""
    test_file = tmp_path / 'line_endings.txt'
    test_file.write_bytes(b'keep\r\nREMOVE_ME\r\nstay\n')

    remove_line_from_file(str(test_file), ['REMOVE_ME'])

    assert test_file.read_bytes() == b'keep\r\nstay\n'


def test_file_is_writeable(tmp_path):
    """Report existing writable files and reject missing files."""
    existing_file = tmp_path / 'existing.txt'
    existing_file.write_text('content')

    assert file_is_writeable(str(existing_file))
    assert not file_is_writeable(str(tmp_path / 'missing.txt'))


@pytest.mark.parametrize(
    ('filename', 'expected_version'),
    [
        ('myfile_23.txt', '23'),
        ('myfile-9.txt', '9'),
        ('myfile.130.txt', '130'),
        ('myfile_v1002.txt', '1002'),
        ('name_without_separator.txt', '0'),
        ('v42.txt', '42'),
        ('myfile-alpha.txt', '0'),
        ('myfile.txt', '0'),
        ('mod_asset.1004.ma', '1004'),
        ('script_nuke_s100_v1005.ma', '1005'),
    ],
)
def test_get_version_from_filename(filename: str, expected_version: str):
    """Version extraction should handle supported separators and invalid values."""
    assert get_version_from_filename(filename) == expected_version
