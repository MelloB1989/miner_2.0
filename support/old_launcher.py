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
#Environment variables
launched = False
checked = 0
#Getting the arguments passed
worker = sys.argv[1]
spot_id = sys.argv[2]
spot_year = sys.argv[3]
spot_month = sys.argv[4]
spot_day = sys.argv[5]
spot_hour = sys.argv[6]
spot_min = sys.argv[7]
if int(spot_hour) < 10:
    hourf = int(spot_hour) - 1
    hour = "0" + str(hourf)
else:
    hour = 0
    hour = int(spot_hour) - 1
#Formatting time in UTC format.
utc = spot_year + "-" + spot_month + "-" + spot_day + "T" + str(hour) + ":" + spot_min + ":00Z"
worker_db = doc.find_one({"instance": worker})
worker_support = worker_db['support']
worker_pem = worker_db['pem']
worker_dns = worker_db['dns']
worker_name = worker_db['instance']
stat = os.system('python3 launch_stat_send.py "Launch Request Placed!" {}'.format(worker_support))
#Function to continue installation after the launch
def continue_further(id):
    stat = os.system('python3 launch_stat_send.py "Instance Launched!(chaliye shuru karte hai!)" {}'.format(worker_support))
    remove = os.system("sudo rm /var/www/html/id.json")
    get_ip = os.system('aws ec2 describe-instances --instance-ids {} --output json > /var/www/html/id.json 2>&1'.format(id))
    url = "http://localhost/id.json".format(worker_support)
    set_json = requests.get(url)
    instance_details = json.loads(set_json.text)
    ip = instance_details["Reservations"][0]["Instances"][0]["PublicIpAddress"]
    state = instance_details["Reservations"][0]["Instances"][0]["State"]["Name"]
    #ip_addr_file = open("./ip.txt", "r+")
    #ip = ip_addr_file.read()
    #u = { "dns" : worker_dns }
    #update = { "dns" : ip }
    launch_state = doc.update_one({ 'dns' : worker_dns}, {"$set" : {'launch_state' : 'True'}})
    up = doc.update_one({ 'dns' : worker_dns}, {"$set": {'dns' : ip}})


    start = os.system("nohup bash 3.0.sh {} {} {}".format(worker_pem, ip, worker_name))
#Check if the instance is launched.
while launched == False:
    #Get the status of the instance in json and host it in the server using apache2 service.
    rm = os.system("sudo rm /var/www/html/history.json")
    get_status = os.system("aws ec2 describe-spot-fleet-request-history --spot-fleet-request-id {} --start-time {} > /var/www/html/history.json 2>&1".format(spot_id, utc))
    history = "http://{}/history.json".format(worker_support)
    #Getting the json file
    set_json = requests.get(history)
    fleet_history = json.loads(set_json.text)
    #Calculating the number of events.
    range = len(fleet_history["HistoryRecords"]) - 1
    current_range = 0
    #Checking each and every event one by one.
    while current_range <= range:
        event_type = fleet_history["HistoryRecords"][current_range]["EventType"]
        print(event_type)
        if event_type == "error":
            print("Exception: Given Spot capacity is not available!")
            launched = False
            if checked >= 300:
                print("Too long exception!")
                send_exception = os.system('python3 send_exception.py "time_taking" {}'.format(worker_support))
            else:
                send_exception = os.system('python3 send_exception.py "instance_launch_exception" {}'.format(worker_support))
            #send_exception = os.system("")

        elif event_type == "cancelled":
            launched = False
            stat = os.system('python3 launch_stat_send.py "The request was cancelled!! @everyone" {}'.format(worker_support))
            #relaunch = os.system('nohup sudo bash launcher.sh')
            break
        
        elif event_type == "instanceChange":
            if fleet_history["HistoryRecords"][current_range]["EventInformation"]["EventSubType"] == "launched":
                instance_id = fleet_history["HistoryRecords"][current_range]["EventInformation"]["InstanceId"]
                launched = True
                send_exception = os.system('python3 send_exception.py "Instance Launched!" {}'.format(worker_support))
                continue_further(instance_id)

        current_range = current_range + 1
    #Record the Number of times we triggered exceptional errors.
    checked = checked + 1
    time.sleep(5)

#aws ec2 describe-spot-fleet-request-history --spot-fleet-request-id sfr-0ace73bd-a696-4f3a-883e-5e1c65ee2d7e --start-time 2021-08-21T03:27:40Z > /var/www/html/history.json 2>&1