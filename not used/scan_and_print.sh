#!/bin/bash

# Debugging: Print start message
echo "Running scan.py..."

# Run the scan.py script
/usr/bin/python3 /home/frijol/Desktop/no_recollection/scan.py

# Debugging: Print scan completion message
echo "Finished running scan.py"

# Path to the file you want to print (not the scanned file)
FILE_TO_PRINT="/home/frijol/Desktop/no_recollection/PtintTest.pdf"

# Debugging: Print file to print
echo "File to print: $FILE_TO_PRINT"

# Run the print.py script to print the other file
/usr/bin/python3 /home/frijol/Desktop/no_recollection/print.py "$FILE_TO_PRINT"

# Debugging: Print end message
echo "Finished running print.py"
