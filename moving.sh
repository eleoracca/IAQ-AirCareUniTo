#!/usr/bin/sh
set -e

echo " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo " Script to remove duplicated files and move them to the sensors' folders."
echo ""

# Opening folder with data files
cd scraping

# Removing possible duplicated downloaded files
echo " --- Removing duplicated files"
find . -type f -regextype posix-extended -regex '.*\([0-9]+\)\.xls' -delete

# Moving files to sensors' subfolders
echo ""
echo " --- Moving files to sensors' folders"
for code in $(ls | grep .xls | cut -d _ -f 2 | sort | uniq) ; do
    mkdir -p $code && \
    mv *_${code}_*.xls $code/
done

echo ""
echo " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
echo " Removal and file movement ended."
echo " Thank you for your patience!"
echo " ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
