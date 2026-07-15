# ----------------------------------------------------------------------------------------
# Python-Backpack - FolderUtils Tests
# Maximiliano Rocamora / maxirocamora@gmail.com
# https://github.com/MaxRocamora/python-backpack
# ----------------------------------------------------------------------------------------

from pathlib import Path
from unittest import mock

from backpack.folder_utils import (
    browse_folder,
    create_folder,
    create_folders,
    recursive_dir_copy,
    remove_files_in_dir,
)


def create_file(path: Path, content: str = '') -> Path:
    """Creates a temp txt file."""
    file_path = path / 'temp.txt'
    file_path.write_text(content)
    return file_path


def test_create_folders(tmp_path):
    """Create multiple folders and optionally clear their contents."""
    folders = [tmp_path / 'ALPHA', tmp_path / 'BETA']
    folder_names = [str(folder) for folder in folders]

    create_folders(folder_names, verbose=True)
    assert all(folder.is_dir() for folder in folders)

    create_file(folders[0])
    create_folders(folder_names, force_empty=False)
    assert (folders[0] / 'temp.txt').is_file()

    create_folders(folder_names, force_empty=True)
    assert list(folders[0].iterdir()) == []


def test_browse_folder_with_spaces(tmp_path):
    """Pass a folder containing spaces to Explorer as one argument."""
    folder = tmp_path / 'folder with spaces'
    folder.mkdir()

    with mock.patch('backpack.folder_utils.subprocess.Popen') as popen:
        assert browse_folder(str(folder)) is True

    popen.assert_called_once_with(['explorer', str(folder.resolve())])


def test_browse_folder_rejects_invalid_path(tmp_path):
    """Do not launch Explorer for missing or absent paths."""
    with mock.patch('backpack.folder_utils.subprocess.Popen') as popen:
        assert browse_folder(str(tmp_path / 'missing')) is False
        assert browse_folder(None) is False

    popen.assert_not_called()


def test_browse_folder_handles_launch_failure(tmp_path):
    """Return False when Explorer cannot be started."""
    with mock.patch(
        'backpack.folder_utils.subprocess.Popen',
        side_effect=OSError('Unable to launch Explorer'),
    ):
        assert browse_folder(str(tmp_path)) is False


@mock.patch('backpack.folder_utils.os.makedirs')
def test_create_folder_oserror(mock_makedirs, tmp_path):
    """Test OSError handling in create_folder."""
    mock_makedirs.side_effect = OSError('Permission denied')
    result = create_folder(str(tmp_path / 'error_folder'))
    assert result is True  # Should still return True even on error


def test_remove_dir(tmp_path):
    """Creates a folder with files and remove it."""
    test_dir = tmp_path / 'remove_dir'
    create_folder(str(test_dir))
    create_file(test_dir)
    nested_dir = test_dir / 'nested'
    nested_dir.mkdir()
    create_file(nested_dir)

    remove_files_in_dir(str(test_dir))

    assert test_dir.is_dir()
    assert list(test_dir.iterdir()) == []


def test_recursive_dir(tmp_path):
    """Creates a dir with sub dirs and files and copy them."""
    source_dir = tmp_path / 'recursive_dir'
    source_dir.mkdir()
    create_file(source_dir, 'root')
    nested_dir = source_dir / 'recursive_sub_dir'
    nested_dir.mkdir()
    create_file(nested_dir, 'nested')
    target_dir = tmp_path / 'recursive_target'

    recursive_dir_copy(str(source_dir), str(target_dir))

    assert (target_dir / 'temp.txt').read_text() == 'root'
    assert (target_dir / 'recursive_sub_dir' / 'temp.txt').read_text() == 'nested'
