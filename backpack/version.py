# ----------------------------------------------------------------------------------------
# 1.0.0 07/2022 - Initial Release
# 1.0.2 07/2022 - More Methods and tests
# 1.0.3 07/2022 - JsonMetaFile, JsonUserSettings
# 1.0.4 04/2023 - Added camelcase_to_snakecase function
# 1.0.5 05/2023 - Refactor JsonMetaFile, Added Cache, Some type hints / docstrings
# 1.1.0 01/2024 - Ruff Formatting
# 1.1.1 07/2025 - Update Python version matrix to include 3.10 and 3.11, update actions versions
# 1.1.2 07/2025 - Update actions versions, remove unused badge from README
# 1.1.3 07/2025 - Improve test class names and docstrings for clarity, ruff formatting
# 1.1.4 07/2025 - Moved from pipenv to poetry for dependency management.toml
# 2.0.1 05/2026 - Remove tox workflow and setup.py, standardize uv + coverage tooling
# 2.0.2 05/2026 - Add PyPI long description metadata and release polish
# 2.0.3 06/2026 - Add type hints to backpack.cache, backpack.folder_utils, backpack.json_user_settings, backpack.json_utils, and backpack.logger, refactor backpack.cache to use functools.lru_cache, and add tests for backpack.cache and backpack.folder_utils.
# ----------------------------------------------------------------------------------------

__version__ = '2.0.3'

VERSION_MAJOR, VERSION_MINOR, VERSION_PATCH = map(int, __version__.split('.'))

version = __version__

app_name = 'python-backpack'
