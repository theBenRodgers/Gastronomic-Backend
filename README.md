# Set Up Virtual Environment

This guide provides instructions to set up a Python virtual environment and install dependencies from a `requirements.txt` file on different operating systems.

## Prerequisites
- Python 3 must be installed on your system.
- Ensure `requirements.txt` is available if you need to install dependencies.

## Setup Instructions

### On Mac/Linux
1. Open a terminal.
2. Navigate to the directory where the script is located.
3. Give the script executable permission:
   ```bash
   chmod +x setup_venv.sh
   ```
4. Run the script:
   ```bash
   ./setup_venv.sh
   ```

### On Windows (Command Prompt)
1. Open **Command Prompt** (`cmd`).
2. Navigate to the directory where the script is located using `cd`.
3. Run the script:
   ```cmd
   setup_venv.bat
   ```

### On Windows (PowerShell)
1. Open **PowerShell**.
2. Navigate to the directory where the script is located.
3. If running for the first time, allow script execution:
   ```powershell
   Set-ExecutionPolicy Unrestricted -Scope Process
   ```
4. Run the script:
   ```powershell
   .\setup_venv.ps1
   ```

## What the Scripts Do
- Check if Python is installed.
- Create a virtual environment (`venv`).
- Activate the virtual environment.
- Check if `requirements.txt` exists.
- Install dependencies from `requirements.txt`.
- Deactivate the virtual environment.

## Notes
- If Python is not found, install it from [python.org](https://www.python.org/downloads/).
- If using Windows PowerShell, you may need to change the execution policy (`Set-ExecutionPolicy`) before running `.ps1` scripts.
- If `requirements.txt` is missing, dependencies will not be installed, but the virtual environment will still be created.
