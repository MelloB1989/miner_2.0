import socket
import os
import sys
import pymongo
from config import mongodb_config

worker = sys.argv[1]
#DATABASE CLIENT----------------------------------------------
myclient = pymongo.MongoClient(mongodb_config.client)
db = myclient[mongodb_config.database_name1]
doc = db[mongodb_config.collection1]

con = doc.find_one()
master = con['master']
print(master)
# take the server name and port name
host = master
port = 5000

# create a socket at server side
# using TCP / IP protocol
s = socket.socket(socket.AF_INET,
                                socket.SOCK_STREAM)

s.connect((master, port))#HERE WE ARE CONNECTING TO THE MASTER SERVER TO SEND THE OFFLINE WORKER NAME.

# send message to the client after
# encoding into binary string
#res = ''.join(format(i, '08b') for i in bytearray(worker, encoding ='utf-8'))
s.send(worker.encode())#SENDING WORKER NAME TO RE-LAUNCH THE WORKER
#print(res)
#msg = "Bye.............."
#s.send(msg.encode())

# disconnect the server
s.close()