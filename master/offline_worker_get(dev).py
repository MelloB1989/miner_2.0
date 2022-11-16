import socket
import os
import sys
import time

# take the server name and port name

host = '0.0.0.0'
port = 5000

# create a socket at client side
# using TCP / IP protocol
def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect it to server and port
# number on local computer.
# bind the socket with server
# and port number
    s.bind(('', port))

# allow maximum 1 connection to
# the socket
    s.listen(1)

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
        msg = c.recv(1024)
        ch = 0
        ps = 0
        work = ""
        pswd = ""
        st = txt
        ch = 0
        ps = 0
        work = ""
        pswd = ""
        #st = str(txt)
        length = len(st)
        while ch != length:
            cuch = st[ch]
            if cuch == "!":
                ps = ch + 1
                while ps != length:
                    pswd = pswd + st[ps]
                    ps = ps + 1
            ch = ch + 1
        ch = 0
        while ch != length:
            cuch = st[ch]
    #print(cuch)
        if cuch == "!":
            break
        else:
            work = work + cuch
            ch = ch + 1
        if pswd == "Vaishnavi!s143@mellob1989":
            print('Received:' + msg.decode())
            start_install = os.system("nohup python3 start_install.py {} > log/install.txt 2>&1 &".format(txt))
        #Send a alert message in discord
            send_mgs = os.system('python3 send_mgs.py "A worker is offline!" {}'.format(txt))
            #print('Received:' + msg.decode())
        #msg = c.recv(1024)

# disconnect the client
    c.close()
    time.sleep(8)
while True:
    start_server()