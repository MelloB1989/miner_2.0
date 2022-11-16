import sys
import os
import time
#Run update script for every 10s

while True:
    time.sleep(10)
    update_node = os.system("nohup sudo python3 update.py > log/update.txt 2>&1 &")
    exit