#from upload import API_KEY
from flask import Flask, request, render_template
import sys
import os
#import pymongo
#import time
#import json
#import requests
app = Flask(__name__, template_folder='web')
API_KEY = "1989"

@app.route('/')
def index():
  return '200 OK'
  
@app.route('/about')
def say_hello():
  return 'Cryptomine Server'

@app.route('/uploads', methods=['POST'])
def upload():
    file_name = request.form['file_name']
    apkey = request.form['key']
        # here you can send this static_file to a storage service
        # or save it permanently to the file system
    #print(str(json_file))
    if API_KEY == apkey:
        #json_file.save('./json')
        #pem_file.save()
        create = os.system("sudo touch {}.pem json/{}.json".format(file_name, file_name))
        js = open('./json/{}'.format(file_name), 'w')
        js.write(json_file)
        js.close
        pem = open('{}.pem'.format(file_name), 'w')
        pem.write(pem_file)
        pem.close
    #Upload to Data-Server
    #upl = os.system("python3 upload.py {} {}".format(json_file, pem_file))
    #return render_template('done.html', name=None)
        return ("200 OK")
    else:
        return ("HTTP 403 Forbidden")