import sys
import os
from config import mongodb_config
import time
import pymongo

#DATABASE CLIENT----------------------------------------------
myclient1 = pymongo.MongoClient(mongodb_config.client)
db1 = myclient1[mongodb_config.database_name]
doc1 = db1[mongodb_config.collection]

w = open("./work.txt", "r+")
work = w.read()
w.close()

#Getting information------------------------------------------
worker_db = doc1.find_one({"instance": work})

#DATABASE CLIENT----------------------------------------------
update = ""
ver = ""
installed_version = worker_db["version"]
myclient = pymongo.MongoClient("mongodb://myUserAdmin:Vaishnavi%21s143%40mellob1989%40database-db.socify.cf@db.respawn.ml:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")
db = myclient['constants']
doc = db['update']
up = doc.find_one()
update = up['command']
ver = up['version']
change_log = up['change_log']

if installed_version != ver:
    #re = os.system("sudo rm version.txt && sudo touch version.txt && sudo chmod 777 version.txt")
    #f = open("./version.txt", "r+")
    #f.write(ver)
    #f.close()
    up = doc1.update_one({'instance' : work}, {"$set": {'version' : ver}})
    upx = doc1.update_one({'instance' : work}, {"$set": {'change_log' : change_log}})
    update_script = os.system(update)
    done = os.system('python3 updated.py "Feels good to have that new code..." {}'.format(work))

#update_script = os.system(update)