import socket

# take the server name and port name
host = 'localhost'
port = 5000

# create a socket at server side
# using TCP / IP protocol
s = socket.socket(socket.AF_INET,
				socket.SOCK_STREAM)

s.connect(('127.0.0.1', port))

# send message to the client after
# encoding into binary string
s.send(b"HELLO, How are you ? \
	Welcome to Akash hacking World")

msg = "Bye.............."
s.send(msg.encode())

# disconnect the server
s.close()
