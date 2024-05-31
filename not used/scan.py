from time import sleep
import os

print("Hello World!")

while True:
   print("Trying to scan ...")
   os.system("./scan.sh")
   print("Tried")
   sleep(7)