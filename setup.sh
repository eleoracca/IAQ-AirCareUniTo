#!/bin/bash
set -e



# ~~~ Global variables
# Path to python virtual environment
VENV_DIR="env"
RENV_DIR="renv"

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
mkdir -p "./figures"
mkdir -p "./results"


# ~~~ Python virtual environment
echo ""
echo " ~~~ Python virtual environment"
# --- Creating a virtual environment for Python
echo " --- Creating virtual environment"
if [ ! -d "$VENV_DIR" ]; then
		python3 -m venv "$VENV_DIR"
fi


# --- Activating the virtual environment
echo " --- Activating virtual environment"
source $VENV_DIR/bin/activate


# --- Installing required Python packages
echo " --- Installing required packages"
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo " requirements.txt not found"
fi


# --- Deactivating the virtual environment
echo " --- Deactivating virtual environment"
deactivate


# ~~~ R virtual environment
echo ""
echo " ~~~ R virtual environment"


# --- Checking if renv folder exists
if [ -d "$RENV_DIR" ]; then
    echo " --- Activating virtual environment"
    Rscript -e "if (!require('renv')) install.packages('renv', repos='https://cloud.r-project.org'); renv::activate()"
else
    echo " --- Inizialising a new virtual environment"
    Rscript -e "if (!require('renv')) install.packages('renv', repos='https://cloud.r-project.org'); renv::init()"
fi


# --- Restoring libraries if renv.lock present
if [ -f "renv.lock" ]; then
    echo " --- Restoring libraries from renv.lock"
    Rscript -e "renv::restore(prompt = FALSE)"
else
    echo " --- renv.lock not found, skipping restore"
fi


# --- Ending print
echo ""
echo " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo " Setup completed successfully."
echo " Thank you for your patience!"
echo " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
