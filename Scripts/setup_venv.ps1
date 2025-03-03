$envName = "venv"

# Check if Python is installed
if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    Write-Host "Python is not installed. Please install it and try again."
    exit 1
}

# Create virtual environment
python -m venv $envName
Write-Host "Virtual environment '$envName' created."

# Activate the virtual environment
& "$envName\Scripts\Activate.ps1"
Write-Host "Virtual environment activated."

# Check if requirements.txt exists
if (-Not (Test-Path "requirements.txt")) {
    Write-Host "No requirements.txt found. Skipping installation of dependencies."
    exit 0
}

# Install dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
Write-Host "Dependencies installed successfully."

# Deactivate the virtual environment
deactivate
Write-Host "Virtual environment deactivated."
