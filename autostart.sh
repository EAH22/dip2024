bash
#!/bin/bash

# !!!
# To enable/disable this script, in terminal: 
# sudo systemctl disable recollection.service
# then reboot

truncate -s 0 /home/frijol/Desktop/no_recollection/recollection.log

# Wait 10s.
sleep 10

# Activate virtual environment
source /home/frijol/Desktop/no_recollection/venv/bin/activate

# Launch script. Log output to recollection.log
python -u /home/frijol/Desktop/no_recollection/main.py > /home/frijol/Desktop/no_recollection/recollection.log