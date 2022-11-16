import os
import sys
import pymongo
import time
from config import mongodb_config
#Getting the arguments
worker_pem = sys.argv[1]
worker_dns = sys.argv[2]
worker_name = sys.argv[3]

#DATABASE CLIENT----------------------------------------------
myclient = pymongo.MongoClient(mongodb_config.client)
db = myclient[mongodb_config.database_name]
doc = db[mongodb_config.collection]

#Trigger instance launcher
launch_spot = os.system("nohup launcher.sh {} {}.json".format(worker_name, worker_name))

#Check if the instance is launched or not for every five seconds
launched = False
while launched != False:
    worker_db = doc.find_one({"instance": worker_name})
    launched = worker_db['launch_state']
    time.sleep(5)

#Run installation script after the instance is launched
install_miner = os.system("nohup sudo bash 3.0.sh {} {} {} &".format(worker_pem, worker_dns, worker_name))

