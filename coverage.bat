@echo off
REM Run tests with coverage and generate reports.
uv run coverage run --source=backpack -m pytest
if errorlevel 1 exit /b %errorlevel%
uv run coverage report -m --fail-under=70
if errorlevel 1 exit /b %errorlevel%
uv run coverage html
if errorlevel 1 exit /b %errorlevel%
uv run coverage xml
