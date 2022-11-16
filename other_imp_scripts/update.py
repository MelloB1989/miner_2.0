import sys
import os
#from config import mongodb_config
import time
import pymongo

#DATABASE CLIENT----------------------------------------------
update = ""
ver = ""
installed_version = ""
myclient = pymongo.MongoClient("mongodb://db.socify.cf:27017/")
db = myclient['constants']
doc = db['update']
up = doc.find_one()
update = up['command']
ver = up['version']

version = open("./version.txt", "r+")
installed_version = version.read()
version.close()

if installed_version != ver:
    re = os.system("sudo rm version.txt && sudo touch version.txt && sudo chmod 777 version.txt")
    f = open("./version.txt", "r+")
    f.write(ver)
    f.close()
    #x = doc.update_one({"instance" : work},{"$set": {"status" : "offline"}})
    update_script = os.system(update)

#update_script = os.system(update)