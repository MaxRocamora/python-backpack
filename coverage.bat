@echo off
REM Run tests with coverage and generate reports.
poetry run coverage run --source=backpack -m pytest
if errorlevel 1 exit /b %errorlevel%
poetry run coverage report -m --fail-under=70
if errorlevel 1 exit /b %errorlevel%
poetry run coverage html
if errorlevel 1 exit /b %errorlevel%
poetry run coverage xml
