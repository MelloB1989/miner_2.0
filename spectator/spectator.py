import os
import sys
import pymongo
import time
from config import mongodb_config
worker = sys.argv[1]

#DATABASE CLIENT----------------------------------------------
myclient = pymongo.MongoClient(mongodb_config.client)
db = myclient[mongodb_config.database_name]
doc = db[mongodb_config.collection]


# define the countdown func.
def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
        worker_db = doc.find_one({"instance": worker})
        #print(worker_db)
        worker_status = worker_db['status']

        file = open("./exception.txt", "r+")
        mgs = file.read()
        mgs = str(mgs)
        #file.close()
        #Check the type of exception
        if worker_status == "online":
            notify = os.system('python send_mgs_spectate.py "Worker Is Up" {}'.format(worker))
            break

        if mgs == "instance_launch_exception":
            print(mgs)
            notify = os.system('python send_mgs_spectate.py "ERROR: SPOT CAPACITY NOT AVAILABLE" {}'.format(worker))
            clear = file.write("0000000000000000000000000000000000000000000000000000000000000000000000000000000000")
        #Wait for 30 minutes while checking for exception release for every second.
            extra_wait = int(t) + 50#1800
            #t = extra_wait
            break
            #countdown(extra_wait)

        elif mgs == "ssh_timeout":
            print(mgs)
            notify = os.system('python send_mgs_spectate.py "SSH-TIMEOUT ERROR" {}'.format(worker))
            clear = file.write("0000000000000000000000000000000000000000000000000000000000000000000000000000000000")
            extra_wait = int(t) + 300
            #t = extra_wait
            break

        elif mgs == "half_install":
            print(mgs)
            notify = os.system('python send_mgs_spectate.py "SYSTEM FATAL ERROR: HALF WAY DIE" {}'.format(worker))
            clear = file.write("0000000000000000000000000000000000000000000000000000000000000000000000000000000000")
            extra_wait = int(t) + 500
            #t = extra_wait
            break

        elif mgs == "blackout" and worker_status == "offline":
            print(mgs)
            notify = os.system('python3 send_mgs_spectate.py "SYSTEM FATAL ERROR: BLACKOUT" {}'.format(worker))
            clear = file.write("0000000000000000000000000000000000000000000000000000000000000000000000000000000000")
            extra_wait = int(t) + 600
            #t = extra_wait
            break
     
    countdown(extra_wait) 
    #print('Fire in the hole!!')

# input time in seconds
t = 1000

# function call
countdown(int(t))
