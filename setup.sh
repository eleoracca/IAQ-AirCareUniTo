#!/bin/bash
set -e

# ~~~ Global variables
# Path to python virtual environment
VENV_DIR="env"

# Number of thread
num_threads=$(($(nproc) -1))
if [ "$num_threads" -lt 1 ]; then
    num_threads=1
fi

# ~~~ Setup commands
echo " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo " Setting up the environment for the analysis"
echo ""

# --- Creating useful directories
echo " --- Creating useful directories"
mkdir -p "./data"
mkdir -p "./raw-data"
mkdir -p "./scraping"
mkdir -p "./figures"
mkdir -p "./results"

# --- Creating a virtual environment for Python
echo " --- Creating virtual environment"
if [ ! -d "$VENV_DIR" ]; then
		python3 -m venv "$VENV_DIR"
fi

# --- Activating the virtual environment
echo " --- Activating virtual environment"
source $VENV_DIR/bin/activate

# --- Installing required Python packages
echo " --- Installing required Python packages"
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo " requirements.txt not found"
fi

# --- Deactivating the virtual environment
echo " --- Deactivating virtual environment"
deactivate

echo ""
echo " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo " Setup completed successfully."
echo " Thank you for your patience!"
