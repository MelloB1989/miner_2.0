import threading
from discord import message
from pymongo import mongo_client
import requests
import json
import discord
import os
import sys
import pymongo
from config import mongodb_config
#Api keys and bot ids

#DATABASE CLIENT----------------------------------------------
myclient = pymongo.MongoClient(mongodb_config.client)
db = myclient[mongodb_config.database_name]
doc = db[mongodb_config.collection]

#Discord-Channel-ID
channelID = "864055019899715584"
#Bot-Token
botToken = "ODY0MDQxODIwMjY1OTA2MjA2.YOvrpw.BpdB43GA2AUUpVDF9mU3yj32owI"
#Api endpoints

#Discord
baseURL = "https://discordapp.com/api/channels/{}/messages".format(channelID)
headers = { "Authorization":"Bot {}".format(botToken), "User-Agent":"myBotThing (http://socify.co.in, v0.1)", "Content-Type":"application/json", }
#Ethermine
site_stats = 'https://api.ethermine.org/miner/0xe255fa73447a7cc3349848f763304ab666244ce1/currentStats'
workers = 'https://api.ethermine.org/miner/0xe255fa73447a7cc3349848f763304ab666244ce1/workers'.format(channelID)
site_settings = 'https://api.ethermine.org/miner/0xe255fa73447a7cc3349848f763304ab666244ce1/settings'.format(channelID)

#Json To String
set_json = requests.get(site_settings)
mine_json = requests.get(site_stats)
worker_json = requests.get(workers)
#
result_stats = json.loads(mine_json.text)
set_stats = json.loads(set_json.text)
worker_stats = json.loads(worker_json.text)

#Collecting data
payout = set_stats['data']['minPayout']
report_hash = result_stats['data']['reportedHashrate']
current_hash = result_stats['data']['currentHashrate']
average_hash = result_stats['data']['averageHashrate']
valid_shares = result_stats['data']['validShares']
invalid_shares = result_stats['data']['invalidShares']
stale_shares = result_stats['data']['staleShares']
active_workers = result_stats['data']['activeWorkers']
unpaid_balance = result_stats['data']['unpaid']
worker_data = worker_stats['data'][0]

#Cleaning the data
rhash = str(report_hash / 1000000 )[0:-5]
chash = str(current_hash / 1000000 )[0:-13]
ahash = str(average_hash / 1000000 )[0:-13]
unpaid = str(unpaid_balance / 1000000000000000000)[0:-12]
active_workers = int(active_workers)

#Function to send stats
def stat_send(rehash, cuhash, avghash, activew, shares, upay):
    #Communication Channel
    channelID = "864421689462489098"
    #Bot-Token
    botToken = "ODY0MDQxODIwMjY1OTA2MjA2.YOvrpw.BpdB43GA2AUUpVDF9mU3yj32owI"
    #Stats
    stat = "mellob!stat "+ rehash +" "+ cuhash +" "+ avghash +" "+ activew +" "+ shares +" "+ upay
    #Send-stats
    baseURL = "https://discordapp.com/api/channels/{}/messages".format(channelID)
    headers = { "Authorization":"Bot {}".format(botToken), "User-Agent":"myBotThing (http://socify.co.in, v0.1)", "Content-Type":"application/json", }
    POSTedJSON = json.dumps ( {"content":str(stat)} ) 
    r = requests.post(baseURL, headers = headers, data = POSTedJSON)


#Function to send messages/alerts in discord
def alert(work):
    wb = doc.find_one({"instance" : work})
    worker_status = wb["status"]
    if worker_status == "offline":
        x = doc.update_one({"instance" : work},{"$set": {"status" : "offline"}})
    else:
        x = doc.update_one({"instance" : work},{"$set": {"status" : "offline"}})
        #Discord-Channel-ID
        channelID = "864412058812809216"
    #Bot-Token
        botToken = "ODY0MDQxODIwMjY1OTA2MjA2.YOvrpw.BpdB43GA2AUUpVDF9mU3yj32owI"
    #print(content)
        print(work)
        send = os.system("python3 send_offline_worker.py {}".format(work))
        ale = os.system('python3 send_mgs.py "Worker Offline!" {}'.format(work))
        command = "mellob!offline "+work+worker_status
        baseURL = "https://discordapp.com/api/channels/{}/messages".format(channelID)
        headers = { "Authorization":"Bot {}".format(botToken), "User-Agent":"myBotThing (http://socify.co.in, v0.1)", "Content-Type":"application/json", }
        POSTedJSON = json.dumps ( {"content":str(command)} ) 
        r = requests.post(baseURL, headers = headers, data = POSTedJSON)


'''
def alert(work):
    #Repeat Check
    worker_db = doc.find_one({"instance": work})
    worker_db_state = worker_db['status']
    if worker_db_state == "offline":
        worker_db_state = "zdfdsfsdf"
        exit
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
'''
#Stat-send
stat_send(str(rhash), str(chash), str(ahash), str(active_workers), str(valid_shares), str(unpaid))

#Checking for any offline 
current_worker = 0
crhash = "0"
worker_name = "abhiorg"

while current_worker <= active_workers:
    if current_worker < active_workers:
        worker_rhash = worker_stats['data'][current_worker]['reportedHashrate']
        crhash = str(worker_rhash / 1000000 )[0:-5]
        worker_name = worker_stats['data'][current_worker]['worker']
        #Updating State in DataBase
        if crhash != "":
            worker_db = doc.find_one({"instance": worker_name})
            worker_db_state = worker_db['status']
            upq = { "instance": worker_name}
            update = { "$set": { "status": "online" }}
            x = doc.update_one(upq, update)

    if crhash == "":
    #if worker_name == "alicemartinorg":
        #alert("{} is offline!!".format(worker_name))
        #x = doc.update_one({"instance" : worker_name},{"$set": {"status" : "offline"}})
        alert(worker_name)        
    
    current_worker += 1
    
    



