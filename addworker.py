import os
import sys
import pymongo
from config import mongodb_config

#DATABASE CLIENT----------------------------------------------
myclient = pymongo.MongoClient(mongodb_config.client)
db = myclient[mongodb_config.database_name]
doc = db[mongodb_config.collection]

#Extras-------------------------------------------------------
myclient1 = pymongo.MongoClient("mongodb://myUserAdmin:Vaishnavi%21s143%40mellob1989%40database-db.socify.cf@db.respawn.ml:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")
db1 = myclient1['constants']
doc1 = db1['update']
up = doc1.find_one()
update = up['command']
ver = up['version']
ch = up['change_log']

#Taking Input-------------------------------------------------
welcome = """
***************************************************
Code Author:- MelloB(https://github.com/MelloB1989)
***************************************************
"""
print(welcome)
instance = input("Enter the instance name: ")
#dns = input("Enter dns or ip address: ")
support = input("Enter the support ip address: ")
pem = input("Enter the pem file name: ")
aws_id = input("Enter the aws_id: ")
aws_key = input("Enter the aws_key: ")

print("Packing data...")
data = { "instance" : instance, "status" : "offline", "dns" : "", "support_status" : "down", "support" : support, "pem" : pem, "aws_id" : aws_id, "aws_key" : aws_key, "launch_state" : "", "version" : ver, "change_log" : ch}
print(data)
print("Pushing data to database....")

x = doc.insert_one(data)

print("Done!")
exit