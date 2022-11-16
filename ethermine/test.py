import pymongo
import os
import sys
import json
import requests
#from discord import messages
from config import mongodb_config
#Api keys and bot ids

#DATABASE CLIENT----------------------------------------------
myclient = pymongo.MongoClient(mongodb_config.client)
db = myclient[mongodb_config.database_name]
doc = db[mongodb_config.collection]

#Discord-Channel-ID
channelID = "864055019899715584"
#Bot-Token
botToken = "ODY0MDQxODIwMjY1OTA2MjA2.YOvrpw.9nIM9TfYbV2jqz116yZ19-FfzEs"
#Api endpoints

#Discord
baseURL = "https://discordapp.com/api/channels/{}/messages".format(channelID)
headers = { "Authorization":"Bot {}".format(botToken), "User-Agent":"myBotThing (http://socify.co.in, v0.1)", "Content-Type":"application/json", }


def alert(work):
    #Repeat Check
    worker_db = doc.find_one({"instance": work})
    worker_db_state = worker_db['status']
    upq = { "status": worker_db_state }
    update_state = { "status": "offline" }
    x = doc.update_one({"instance" : work},{"$set": {"status" : "offline"}})

    #Discord-Channel-ID
    channelID = "864412058812809216"
    #Bot-Token
    botToken = "ODY0MDQxODIwMjY1OTA2MjA2.YOvrpw.9nIM9TfYbV2jqz116yZ19-FfzEs"
    #print(content)
    print(work)
    if worker_db_state != "offline":
        #SEND INSTALL REQUEST TO THE MASTER
        send = os.system("python3 send_offline_worker.py {}".format(work))
        ale = os.system('python3 send_mgs.py "Worker Offline!" {}'.format(work))
        command = "worker!offline "+work
        baseURL = "https://discordapp.com/api/channels/{}/messages".format(channelID)
        headers = { "Authorization":"Bot {}".format(botToken), "User-Agent":"myBotThing (http://socify.co.in, v0.1)", "Content-Type":"application/json", }
        POSTedJSON = json.dumps ( {"content":str(command)} ) 
        r = requests.post(baseURL, headers = headers, data = POSTedJSON)

alert("alicemartinorg")