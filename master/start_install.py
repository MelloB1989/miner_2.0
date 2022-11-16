import sys
import os
import pymongo
import time
from config import mongodb_config

worker = sys.argv[1]
upo = False
#DATABASE CLIENT----------------------------------------------
myclient = pymongo.MongoClient(mongodb_config.client)
db = myclient[mongodb_config.database_name]
doc = db[mongodb_config.collection]

worker_db = doc.find_one({"instance": worker})
worker_status = worker_db['status']
support_status = worker_db['support_status']
ws = worker_db['support']
worker_pem = worker_db['pem']

#PEM TO JSON-----------------------------------------------
ch = 0
js = ""
st = str(worker_pem)
length = len(st)
while ch != length:
    cuch = st[ch]
    if cuch == ".":
        break
    else:
        js = js + cuch
    ch = ch + 1
worker_json = js + ".json"


#Run Install Script For Support if needed-----------------------------------------------
mgs = os.system('python3 send_mgs.py "Request to relaunch received!" {}'.format(worker))
mgs = os.system('python3 send_mgs.py "Initiating..." {}'.format(worker))
if support_status == "down":
    install = os.system("nohup python3 2vcpu_setup.py {} > log/2vcpu.txt 2>&1 &".format(worker))
    mgs = os.system('python3 send_mgs.py "Installing support server." {}'.format(worker))
else:
    upo = True

#Change DNS---------------------------------------------------
'''
ip = "0.0.0.0"
chng = os.system("change_dns.py {} {}".format(ip, worker))
'''
#Start Installation------------------------------------------
worker_support = worker_db['support']
worker_pem = worker_db['pem']
worker_dns = worker_db['dns']
per = os.system("sudo chmod 600 {}".format(worker_pem))
#PEM of worker and support is same.
#install = os.system('nohup ssh -i {} -o "StrictHostKeyChecking no" ubuntu@{} "nohup sudo bash 3.0.sh {} {} {} &" > log/3.0.txt 2>&1 &'.format(worker_pem, worker_support, worker_pem, worker_dns, worker))
while upo == False:
    support_status = worker_db['support_status']
    if support_status == "up":
        upo = True
        break
    else:
        time.sleep(5)
        continue

if upo == True:
    #mgs = os.system('python3 send_mgs.py {} {}'.format(worker, worker_json))
    install = os.system('nohup nohup ssh -i {} -o "StrictHostKeyChecking no" ubuntu@{} "nohup sudo bash launcher.sh {} {} > log/launches.txt 2>&1 &" > log/3.0.txt 2>&1 &'.format(worker_pem, worker_support, worker, worker_json))