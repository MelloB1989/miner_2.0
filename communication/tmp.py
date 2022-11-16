import socket
import os
import sys

# take the server name and port name

host = '0.0.0.0'
port = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect it to server and port
# number on local computer.
# bind the socket with server
# and port number
s.bind(('', port))

# allow maximum 1 connection to
# the socket
s.listen(1)

# create a socket at client side
# using TCP / IP protocol
def start_server():
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
        print('Received:' + msg.decode())
        msg = c.recv(1024)

# disconnect the client
    c.close()
while True:
    start_server()