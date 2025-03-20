#!/usr/bin/sh
set -e

cd scraping

for code in $(ls | grep .xls | cut -d _ -f 2 | sort | uniq) ; do
    mkdir -p $code && \
    mv *_${code}_*.xls $code/
done
