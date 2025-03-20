# IAQ-AirCareUniTo
Repository for the analysis of data downloaded from the AirCare sensors placed at UniTo.


## Setup
To start using this framework, Python must be installed.
Then, to correctly set up your working environment, clone the repository and run the following commands in the main folder:

```console
git clone https://github.com/eleoracca/IAQ-AirCareUniTo.git
cd IAQ-AirCareUniTo
bash setup.sh
```

This will create all the necessary directories and set up a Python virtual environment with the required libraries to run the analysis and visualization scripts.


## Downloading the data
To download the data, **Firefox must be installed**. On Linux, the *Snap version of Firefox will not work*.
To start the download, run the following commands from the main folder of the Git repository on your PC:

```console
source env/bin/activate
python scraper.py
deactivate
```

The script will prompt you with the necessary actions.
Please keep in mind that **every time you start the scraper, you need to change the default download folder to the scraping folder** of this repository; otherwise, the data will be saved elsewhere.

After the download is complete, to reorganize the files, run the following command:

```console
bash moving.sh
```

This script will delete any duplicate files and group the files from the same sensors into subfolders.
