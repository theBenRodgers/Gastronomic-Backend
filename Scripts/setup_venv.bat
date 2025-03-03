@echo off
setlocal

:: Set the virtual environment name
set ENV_NAME=venv

:: Check if Python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed. Please install it and try again.
    exit /b 1
)

:: Create virtual environment
python -m venv %ENV_NAME%
echo Virtual environment '%ENV_NAME%' created.

:: Activate the virtual environment
call %ENV_NAME%\Scripts\activate

echo Virtual environment activated.

:: Check if requirements.txt exists
if not exist requirements.txt (
    echo No requirements.txt found. Skipping installation of dependencies.
    exit /b 0
)

:: Install dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo Dependencies installed successfully.

:: Deactivate virtual environment
deactivate

echo Virtual environment deactivated.
