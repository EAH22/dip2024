#! /bin/sh

scanimage --format=png --output-file scans/tmp/scan.png
sleep 3

find scans/tmp/ -type f -empty -print0 | xargs -0 rm

if test -e scans/tmp/scan.png; then
    echo "File exists"
    ./multicrop -c 20,20 -f 20 -d 100 scans/tmp/scan.png scans/tmp/scan_trimmed.png
     convert scans/tmp/scan_trimmed-000.png -crop 1100x+0+0 scans/postcard-$(date "+%FT%H%M%S").png
else
    echo "File does not exist"
fi