#Code Author:- Kartik Deshmukh

import os
import sys
import requests
import json
import time
from config import mongodb_config
import pymongo

#DATABASE CLIENT----------------------------------------------
myclient = pymongo.MongoClient(mongodb_config.client)
db = myclient[mongodb_config.database_name]
doc = db[mongodb_config.collection]
#Environment variables----------------------------------------
launched = False
TIME_CHECK = 0
checked = 0
next_token = ""
#Getting the arguments passed---------------------------------
worker = sys.argv[1]
spot_id = sys.argv[2]
spot_year = sys.argv[3]
spot_month = sys.argv[4]
spot_day = sys.argv[5]
spot_hour = sys.argv[6]
spot_min = sys.argv[7]

print("SRF ID: "+spot_id)
#SAVE THE SRF ID IN A FILE
#Remove previous file if present
s_r = os.system("sudo rm srf.txt")
#Create a file
c_r = os.system("sudo touch srf.txt && sudo chmod 777 srf.txt")
#Store the srf id
srf_file = open("./srf.txt", "r+")
srf_file.write(spot_id)
srf_file.close

if int(spot_hour) < 10:
    hourf = int(spot_hour) - 1
    hour = "0" + str(hourf)
else:
    hour = 0
    hour = int(spot_hour) - 1
#Formatting time in UTC format--------------------------------
utc = spot_year + "-" + spot_month + "-" + spot_day + "T" + str(hour) + ":" + spot_min + ":00Z"
print("Timing: "+utc)
worker_db = doc.find_one({"instance": worker})
worker_support = worker_db['support']
worker_pem = worker_db['pem']
worker_dns = worker_db['dns']
worker_name = worker_db['instance']
stat = os.system('python3 launch_stat_send.py "Launch Request Placed For {}!" {}'.format(worker ,worker_support))

#########################################################################################################################
#Function to continue installation after the launch-------------------------------------------------
def continue_further(id):
    #Send a message to discord*****************
    stat = os.system('python3 launch_stat_send.py "{} Launched!(chaliye shuru karte hai!)" {}'.format(worker ,worker_support))
    #Get the Ip Address************************
    remove = os.system("sudo rm /var/www/html/id.json")
    get_ip = os.system('aws ec2 describe-instances --instance-ids {} --output json > /var/www/html/id.json 2>&1'.format(id))
    url = "http://localhost/id.json"
    try:
        set_json = requests.get(url)
        instance_details = json.loads(set_json.text)
    except:
        al = os.system('sudo python3 launch_stat_send.py "Error occured! Retrying..." {}'.format(worker_support))
        #utc = spot_year + "-" + spot_month + "-" + spot_day + "T" + "0" + str(hour) + ":" + spot_min + ":00Z"
    ip = instance_details["Reservations"][0]["Instances"][0]["PublicIpAddress"]
    state = instance_details["Reservations"][0]["Instances"][0]["State"]["Name"]
    #Update everything to database*************
    launch_state = doc.update_one({ 'dns' : worker_dns}, {"$set" : {'launch_state' : state}})
    up = doc.update_one({ 'dns' : worker_dns}, {"$set": {'dns' : ip}})

    #Start the Installation********************
    start = os.system("nohup bash 3.0.sh {} {} {}".format(worker_pem, ip, worker_name))
#########################################################################################################################
    
#Check if the instance is launched---------------------------------------------------------------------------------------
while launched == False:
    #Check for the presence of next token*****************
    print(next_token)
    if next_token == "":
        rm = os.system("sudo rm /var/www/html/history.json")
        get_status = os.system("aws ec2 describe-spot-fleet-request-history --spot-fleet-request-id {} --start-time {} > /var/www/html/history.json 2>&1".format(spot_id, utc))
    else:
        rm = os.system("sudo rm /var/www/html/history.json")
        get_status = os.system("aws ec2 describe-spot-fleet-request-history --spot-fleet-request-id {} --start-time {} --next-token {} > /var/www/html/history.json 2>&1".format(spot_id, utc, next_token))
    
    history = "http://localhost/history.json"
    #Getting the json file********************************
    try:
        set_json = requests.get(history)
        fleet_history = json.loads(set_json.text)
    except:
        if TIME_CHECK == 0:
            al = os.system('sudo python3 launch_stat_send.py "Error occured! Retrying..." {}'.format(worker_support))
            utc = spot_year + "-" + spot_month + "-" + spot_day + "T" + "0" + str(hour) + ":" + spot_min + ":00Z"
            TIME_CHECK = 1
        else:
            al = os.system('sudo python3 launch_stat_send.py "Error occured! Unsolved!" {}'.format(worker_support))
            exit()

    #Calculating the number of events*********************
    range = len(fleet_history["HistoryRecords"]) - 1
    rl = len(fleet_history)
    current_range = 0
    #Try toget the next token and continue if exception***
    try:
        next_token = fleet_history["NextToken"]
    except:
        next_token = ""
    #Checking each and every event one by one**************
    try:
        while current_range <= range:
        #Get the event name********************************
            event_type = fleet_history["HistoryRecords"][current_range]["EventType"]
        #Get the event time********************************
            utc2 = fleet_history["HistoryRecords"][current_range]["Timestamp"]
            print(str(utc2) + " ----:>" + str(event_type))
            if event_type == "error":
            #Print message with timings********************
                print(str(utc2) + " ----:>" + "Exception: Given Spot capacity is not available!")
                launched = False

            elif fleet_history["HistoryRecords"][current_range]["EventInformation"]["EventSubType"] == "cancelled":
                launched = False
                print(str(utc2) + " ----:>" + "CANCELLLEDDDDD")
                stat = os.system('python3 launch_stat_send.py "The request was cancelled!! @everyone" {}'.format(worker_support))
                exit()
        
            elif event_type == "instanceChange":
                if fleet_history["HistoryRecords"][current_range]["EventInformation"]["EventSubType"] == "launched":
                    instance_id = fleet_history["HistoryRecords"][current_range]["EventInformation"]["InstanceId"]
                    launched = True
                    send_exception = os.system('python3 send_exception.py "{} Launched!" {}'.format(worker ,worker_support))
                    continue_further(instance_id)

            current_range = current_range + 1
        time.sleep(5)

    except:
        print(str(utc2) + " ----:>" + "There was some unexpected error. Please code me well!")
        alert_message = """
        There some unexpected error in launching {}. Please code me well!
        @everyone @here
        """.format(worker)
        #SEND AN ALERT IN DISCORD
        al = os.system('sudo python3 launch_stat_send.py {} {}'.format(alert_message, worker_support))
        print("Quitting...")
        exit