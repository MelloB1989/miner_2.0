OVERVIEW:
Each folder represents a server(except config, communication and launcher)

Ethermine:
This server checks for offline workers every 6 minutes and if it gets any offline worker it sends its name to the master server via port 5000.


Master:
This server listens on port 5000 for offline works which are sent by the ethermine server whenever a worker goes offline.

Procedure:
The tasks done by this server are as follows: 
After receiving the offline worker name the server checks for the worker's info (ip address, etc.) inside the database.
After receiving the info it passes a request to the support server to launch and start mining on the server. Both launching and installation is handled by the support server.

Exceptions:
The support server needs certain scripts and configuration to be made which can get a tedious task, thus 3.0 automates this process too.
The start_install.py script checks in database if the support server is ready or not and makes all configurations automatically is the server is not ready(2vcpu_setup.py).


Launcher:
This script launches a instance in aws.

Config:
This file contains database credentials which stores worker name, ip, pem file name, worker's support server ip and state, worker state, etc.

Communication:
This script enables communication between servers via port 5000.