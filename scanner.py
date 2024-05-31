#! /home/frijol/Desktop/no_recollection/venv/bin python

import subprocess

def scan():
   print("Trying to scan ...")
   result = subprocess.run(['/home/frijol/Desktop/no_recollection/scan.sh'], capture_output=True, text=True)
   result = int(result.stdout.strip())
   return(result)