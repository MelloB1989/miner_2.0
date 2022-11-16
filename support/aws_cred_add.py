import os
import sys

id = sys.argv[1]
key = sys.argv[2]
work = sys.argv[3]

content = ["[default]\n", "aws_access_key_id = "+str(id)+"\n", "aws_secret_access_key = "+str(key)]
cred = open("./credentials.txt", "r+")
cred.writelines(content)
cred.close()

w = open("./work.txt", "r+")
w.write(str(work))
w.close()