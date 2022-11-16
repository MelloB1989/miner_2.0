import sys
import os
from config import mongodb_config
import time
import pymongo

#Getting Region-----------------------------------------------
work = sys.argv[1]

#DATABASE CLIENT----------------------------------------------
myclient = pymongo.MongoClient(mongodb_config.client)
db = myclient[mongodb_config.database_name]
doc = db[mongodb_config.collection]

#Getting information------------------------------------------
worker_db = doc.find_one({"instance": work})
#print(str(worker_db))
worker_support = worker_db['support']
worker_pem = worker_db['pem']
worker_aws_access_key_id = worker_db['aws_id']
worker_secret_access_key = worker_db['aws_key']
#print("PEM------------------"+worker_pem+worker_support)

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
#---------------------------------------------------------
basic_install = os.system("nohup sudo bash basic_support_install.sh {} {} {} {} > log/basic.txt 2>&1 &".format(worker_pem, worker_support, worker_pem, worker_json))
time.sleep(200)
aws_cli_install = os.system("nohup sudo bash aws_cli_install.sh {} {} {} {} {} > log/aws.txt 2>&1 &".format(worker_pem, worker_support, worker_aws_access_key_id, worker_secret_access_key, work))
time.sleep(100)
print("Install Complete!")
#{ "support_staus" : "down" }
#update = { "support_status" : "up" }
up = doc.update_one({'instance' : work}, {"$set": {'support_status' : 'up'}})
mgs = os.system('python3 send_mgs.py "Installed support server." {}'.format(work))
next = os.system('sudo python3 start_install.py {}'.format(work))