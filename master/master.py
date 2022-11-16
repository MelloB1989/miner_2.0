import os
import sys
import socket
import pymongo
from config import mongodb_config

#DATABASE CLIENT----------------------------------------------
myclient = pymongo.MongoClient(mongodb_config.client)
db = myclient[mongodb_config.database_name]
doc = db[mongodb_config.collection]

#Start_Install
def start_install(worker):
    print(worker)
    worker_db = doc.find_one({"instance": worker})
    worker_status = worker_db['status']
    dns = worker_db['dns']
    print(worker_db)
    worker_dns = worker_db['dns']
    if worker_status == "offline":
        #TODO LAUNCH INSTANCE-----------------------------------------
        ip = "0.0.0.0"
        change = os.system("sudo bash change_dns.sh {} {}".format(ip, dns))
        install = os.system("python3 start_install.py {}".format(str(worker)))

#Start_Install
def exception_master(worker):
    print(worker)

#Start_Install
def mgs_spectate(worker):
    print(worker)
#Communication Setup
host = '0.0.0.0'
port = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', port))
s.listen(1)
def receive():
# wait till a client accept
# connection
    c, addr = s.accept()

# display client address
    print("CONNECTION FROM:", str(addr))


# receive message string from
# server, at a time 1024 B
    msg = c.recv(1024)

# repeat as long as message
# string are not empty
    while msg:
        txt = str(msg.decode())
        file = open("./mgs.txt", "r+")
        wr = file.write(txt)
        #Checking Received Data------------------------------------------------
        if str(addr) == "0.0.0.0" or str(addr) == "ethbot.socify.cf" or True:
            start_install(msg.decode())

        elif str(addr) == "127.0.0.0" or str(addr) == "socify.cf":
            exception_master(msg.decode())

        elif str(addr) == "54.188.199.67" or str(addr) == "spectate.socify.cf":
            mgs_spectate(msg.decode())
        print('Received:' + msg.decode())
        msg = c.recv(1024)

# disconnect the client
    c.close()
while True:
    receive()
