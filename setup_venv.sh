#!/bin/bash

# Set the name of the virtual environment
env_name="venv"

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Python3 is not installed. Please install it and try again."
    exit 1
fi

# Create virtual environment
python3 -m venv $env_name

echo "Virtual environment '$env_name' created."

# Activate the virtual environment
source $env_name/bin/activate

echo "Virtual environment activated."

# Check if requirements.txt exists
if [ ! -f requirements.txt ]; then
    echo "No requirements.txt found. Skipping installation of dependencies."
    exit 0
fi

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

echo "Dependencies installed successfully."

deactivate

echo "Virtual environment deactivated."
