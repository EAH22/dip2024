#! /bin/sh

scanimage --format=png --output-file /home/frijol/Desktop/no_recollection/scans/tmp/scan.png
sleep 3

find /home/frijol/Desktop/no_recollection/scans/tmp/ -type f -empty -print0 | xargs -0 rm

if test -e /home/frijol/Desktop/no_recollection/scans/tmp/scan.png; then
    file_created=1
    cp /home/frijol/Desktop/no_recollection/scans/tmp/scan.png /home/frijol/Desktop/no_recollection/scans/archive/postcard-$(date "+%FT%H%M%S").png
else
    file_created=0
fi

echo $file_created