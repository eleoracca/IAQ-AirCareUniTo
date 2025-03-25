# IAQ-AirCareUniTo
Repository for the analysis of data downloaded from the AirCare sensors placed at UniTo.


## Setup
To start using this framework, Python and R are required. Please install their dependencies before starting to work with the repository.
Then, to correctly set up your working environment, clone the repository and run the following commands in the main folder:

```console
git clone https://github.com/eleoracca/IAQ-AirCareUniTo.git
cd IAQ-AirCareUniTo
bash setup.sh
```

This will create all the necessary directories and set up the Python and R virtual environments with the required libraries to run the analysis and visualization scripts.


## Downloading the data
To download the data, **Firefox must be installed**. On Linux, the *Snap version of Firefox will not work*.
To start the download, run the following commands from the main folder of the Git repository on your PC:

```console
source env/bin/activate
python scraper.py
deactivate
```

The script will prompt you with the necessary actions and comments during the execution.
Please keep in mind that **every time you start the scraper, you need to change the default download folder to the scraping folder** of this repository; otherwise, the data will be saved elsewhere. Also, be sure not to minimize the browser window during the download, as this may cause the download to fail.
A compatibility issue was detected and solved by updating one of the Firefox drivers (geckodriver).

After the download is complete, to reorganize the files, run the following command from the main folder of the Git repository on your PC:

```console
bash moving.sh
```

This script will delete any duplicate files and group the files from the same sensors by name into subfolders created by the script itself.


## Merging data files
After the download, to improve the usability of the data, it is possible to use the *data_extraction.R* script in the *analysis* subfolder.
You can execute it through **RStudio** or from the terminal using the following commands:

```console
cd analysis
Rscript data_extraction.R
```

Make sure to execute the script from the *analysis* subfolder.
At the end of the script execution, in the directory *IAQ-AirCareUniTo/data*, you will find one CSV file for each sensor containing all the data downloaded from the site, extracted from the XLS files in each sensor's directory.

