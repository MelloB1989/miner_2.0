from flask import Flask, request, render_template, send_file
#from flask import send_file
import sys
import os
import pymongo
import time
import json
import requests
from config import mongodb_config

#DATABASE CLIENT----------------------------------------------
myclient = pymongo.MongoClient(mongodb_config.client)
db = myclient[mongodb_config.database_name]
doc = db[mongodb_config.collection]

#Ethermine
site_stats = 'https://api.ethermine.org/miner/0x30417986cce49e005744f27ad7f13a88ea73d0f7/currentStats'
workers = 'https://api.ethermine.org/miner/0x30417986cce49e005744f27ad7f13a88ea73d0f7/workers'
site_settings = 'https://api.ethermine.org/miner/0x30417986cce49e005744f27ad7f13a88ea73d0f7/settings'


#API KEY------------------------------------------------------
api_key = "Vaishnavi!s143@mellob1989@cryptomine_app@socify.co.in#0180349fsghgsjdi34SDGSW$GFSAW#QRWEDSF$T"
app = Flask(__name__, template_folder='web')
'''
#CDN---------------------
@app.route('/images/icons/favicon.ico')
def favicon():
    return send_file('web/images/icons/favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/vendor/bootstrap/css/bootstrap.min.css')
def bootstrap():
    return send_file('web/vendor/bootstrap/css/bootstrap.min.css', mimetype='text/css')

@app.route('fonts/font-awesome-4.7.0/css/font-awesome.min.css')
def font_awesome():
    return send_file('web/fonts/font-awesome-4.7.0/css/font-awesome.min.css', mimetype='text/css')

@app.route('/vendor/animate/animate.css')
def animate():
    return send_file('web/vendor/animate/animate.css', mimetype='text/css')

@app.route('/vendor/css-hamburgers/hamburgers.min.css')
def css_hamburgers():
    return send_file('web/vendor/css-hamburgers/hamburgers.min.css', mimetype='text/css')

@app.route('/vendor/select2/select2.min.css')
def select2():
    return send_file('web/vendor/select2/select2.min.css', mimetype='text/css')

@app.route('/css/util.css')
def util():
    return send_file('web/css/util.css', mimetype='text/css')

@app.route('/css/main.css')
def main():
    return send_file('web/css/main.css', mimetype='text/css')

@app.route('/js/main.js')
def main_js():
    return send_file('web/js/main.js', mimetype='text/javascript')

@app.route('/js/jquery-3.2.1.min.js')
def jquery():
    return send_file('web/js/jquery-3.2.1.min.js', mimetype='text/javascript')

@app.route('/vendor/select2/select2.min.js')
def select2_js():
    return send_file('web/vendor/select2/select2.min.js', mimetype='text/javascript')

@app.route('/vendor/popper/popper.min.js')
def popper_js():
    return send_file('web/vendor/popper/popper.min.js', mimetype='text/javascript')

@app.route('/vendor/bootstrap/js/bootstrap.min.js')
def bootstrap_js():
    return send_file('web/vendor/bootstrap/js/bootstrap.min.js', mimetype='text/javascript')

@app.route('/vendor/jquery/jquery-3.2.1.min.js')
def jquery_js():
    return send_file('web/vendor/jquery/jquery-3.2.1.min.js', mimetype='text/javascript')

@app.route('/vendor/css-hamburgers/hamburgers.min.js')
def css_hamburgers_js():
    return send_file('web/vendor/css-hamburgers/hamburgers.min.js', mimetype='text/javascript')

@app.route('/vendor/select2/select2.min.js')
def select2_min_js():
    return send_file('web/vendor/select2/select2.min.js', mimetype='text/javascript')

@app.route('/vendor/jquery/jquery-3.2.1.min.js')
def jquery_min_js():
    return send_file('web/vendor/jquery/jquery-3.2.1.min.js', mimetype='text/javascript')

@app.route('/vendor/bootstrap/js/popper.js')
def popper_js_min():
    return send_file('web/vendor/bootstrap/js/popper.js', mimetype='text/javascript')

@app.route('/vendor/bootstrap/js/bootstrap.min.js')
def bootstrap_min_js():
    return send_file('web/vendor/bootstrap/js/bootstrap.min.js', mimetype='text/javascript')

@app.route('/vendor/jquery/jquery-3.2.1.min.js')
def jquery_min_js():
    return send_file('web/vendor/jquery/jquery-3.2.1.min.js', mimetype='text/javascript')

@app.route('/vendor/bootstrap/js/bootstrap.min.js')
def bootstrap_min_js():
    return send_file('web/vendor/bootstrap/js/bootstrap.min.js', mimetype='text/javascript')

@app.route('/vendor/tilt/tilt.jquery.min.js')
def tilt_js():
    return send_file('web/vendor/tilt/tilt.jquery.min.js', mimetype='text/javascript')

#------------------------------------------------------
'''
@app.route('/')
def index():
  return render_template('home.html', name=None)
  
@app.route('/about')
def say_hello():
  return 'Cryptomine Server'

@app.route('/setup_master', methods=['POST'])
def master():
    ip = request.form['ip']
    mas = os.system("cd installers && nohup sudo bash master_install.sh master.pem {} &".format(ip))
    return render_template('done.html', name=None)

@app.route('/setup_database', methods=['POST'])
def dbr():
    ip = request.form['ip']
    mas = os.system("cd installers && nohup sudo bash database_setup.sh db.pem {} &".format(ip))
    return render_template('done.html', name=None)

@app.route('/install.html', methods=['GET'])
def dbri():
    #ip = request.form['ip']
    #mas = os.system("cd installers && nohup sudo bash database_setup.sh db.pem {} &".format(ip))
    return render_template('install.html', name=None)
    
@app.route('/timer.html', methods=['GET'])
def dbrt():
    #ip = request.form['ip']
    #mas = os.system("cd installers && nohup sudo bash database_setup.sh db.pem {} &".format(ip))
    return render_template('timer.html', name=None)
    
@app.route('/setup_bot', methods=['POST'])
def botr():
    ip = request.form['ip']
    mas = os.system("cd installers && nohup sudo bash bot_setup.sh bot.pem {} &".format(ip))
    return render_template('done.html', name=None)


@app.route('/get_data', methods=['POST'])
def get_data():
    apkey = request.form['key']
    if api_key == apkey:
        work = request.form['worker']
        data = doc.find_one({'instance' : str(work)})
        return(str(data))
    else:
      return("Invalid API Key!")

@app.route('/put_aws_credentials', methods=['POST'])
def put_aws_cred():
    apkey = request.form['key']
    if api_key == apkey:
        aws_id = request.form['aws_id']
        aws_secret = request.form['aws_secret']
        work = request.form['worker']
        work_db = doc.find_one({'instance' : str(work)})
        up = doc.update_one({'instance' : work}, {"$set": {'aws_id' : aws_id}})
        up1 = doc.update_one({'instance' : work}, {"$set": {'aws_key' : aws_secret}})
    else:
      return("Invalid API Key!")

@app.route('/get_master_log', methods=['POST'])
def get_master_log():
    apkey = request.form['key']
    if api_key == apkey:
        return("Coming Soon!")
    else:
      return("Invalid API Key!")


@app.route('/start_install', methods=['POST'])
def start_install():
    apkey = request.form['key']
    if api_key == apkey:
        #aws_id = request.form['aws_id']
        #work = request.form['worker']
        work = request.form['worker']
        work_db = doc.find_one({'instance' : str(work)})
        #up = doc.update_one({'instance' : work}, {"$set": {'aws_id' : aws_id}})
        #up1 = doc.update_one({'instance' : work}, {"$set": {'aws_key' : aws_secret}})
        start = os.system("nohup sudo python3 start_install.py {} &".format(work))
        return render_template('done.html', name=None)
    else:
      return("Invalid API Key!")

@app.route('/sleep_n_install', methods=['POST'])
def sleepinstall():
    apkey = request.form['key']
    if api_key == apkey:
        work = request.form['worker']
        time_number = request.form['time_number']
        unit = request.form['unit']
        #time.sleep(1)
        notify = os.system('nohup sudo python3 send_mgs.py "Installation will start in {}{}" {} &'.format(time_number, unit, work))
        start_installation = os.system("nohup sleep {}{} && sudo python3 start_install.py {} &".format(time_number, unit, work))
        return render_template('done.html', name="Timer Set")
    else:
        return("Invalid API Key!")

@app.route('/ethermine_stats', methods=['POST'])
def stats():
    apkey = request.form['key']
    if api_key == apkey:
        #Json To String
        set_json = requests.get(site_settings)
        mine_json = requests.get(site_stats)
        worker_json = requests.get(workers)
#
        result_stats = json.loads(mine_json.text)
        set_stats = json.loads(set_json.text)
        worker_stats = json.loads(worker_json.text)

#Collecting data
        payout = set_stats['data']['minPayout']
        report_hash = result_stats['data']['reportedHashrate']
        current_hash = result_stats['data']['currentHashrate']
        average_hash = result_stats['data']['averageHashrate']
        valid_shares = result_stats['data']['validShares']
        invalid_shares = result_stats['data']['invalidShares']
        stale_shares = result_stats['data']['staleShares']
        active_workers = result_stats['data']['activeWorkers']
        unpaid_balance = result_stats['data']['unpaid']
        #worker_data = worker_stats['data'][0]

#Cleaning the data
        rhash = str(report_hash / 1000000 )[0:-5]
        chash = str(current_hash / 1000000 )[0:-13]
        ahash = str(average_hash / 1000000 )[0:-13]
        unpaid = str(unpaid_balance / 1000000000000000000)[0:-12]
        active_workers = int(active_workers)

        stat_send = {"rehash" : rhash, "cuhash" : chash, "avghash" : ahash, "activew" : active_workers, "shares" : valid_shares, "upay" : unpaid}

        return(stat_send)
    else:
      return("Invalid API Key!")


@app.route('/add_worker', methods=['POST'])
def add_worker():
    apkey = request.form['key']
    if api_key == apkey:
        dns = ""
        aws_id = request.form['aws_id']
        aws_key = request.form['aws_secret']
        instance = request.form['worker']
        support = request.form['support_ip']
        pem = request.form['pem_name']
        myclient1 = pymongo.MongoClient("mongodb://myUserAdmin:Vaishnavi%21s143%40mellob1989%40database-db.socify.cf@db.respawn.ml:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")
        db1 = myclient1['constants']
        doc1 = db1['update']
        up = doc1.find_one()
        update = up['command']
        ver = up['version']
        ch = up['change_log']
        data = { "instance" : instance, "status" : "offline", "dns" : dns, "support_status" : "down", "support" : support, "pem" : pem, "aws_id" : aws_id, "aws_key" : aws_key, "launch_state" : "", "version" : ver, "change_log" : ch}
        x = doc.insert_one(data)
        return render_template('fileupload.html', name=None)
        '''
        work_db = doc.find_one({'instance' : str(work)})
        up = doc.update_one({'instance' : work}, {"$set": {'aws_id' : aws_id}})
        up1 = doc.update_one({'instance' : work}, {"$set": {'aws_key' : aws_secret}})
        '''
    else:
      return("Invalid API Key!")


@app.route('/upload_pem', methods=['POST'])
def upload_pem():
    apkey = request.form['key']
    if api_key == apkey:
        static_file = request.files['file']
        file_name = request.form['file_name']
        # here you can send this static_file to a storage service
        # or save it permanently to the file system
        print(str(static_file))
        static_file.save('./{}'.format(str(file_name)))
        return("200 OK")
    else:
      return("Invalid API Key!")

@app.route('/upload_json', methods=['POST'])
def upload_json():
    apkey = request.form['key']
    if api_key == apkey:
        json_file = request.files['file']
        file_name = request.form['file_name']
        # here you can send this static_file to a storage service
        # or save it permanently to the file system
        print(str(json_file))
        json_file.save('./json/{}'.format(str(file_name)))
        return("200 OK")
    else:
      return("Invalid API Key!")

@app.route('/upload_from_html_static', methods=['POST'])
def upload():
    json_file = request.files['json']
    pem_file = request.files['pem']
    file_name = request.form['file_name']
        # here you can send this static_file to a storage service
        # or save it permanently to the file system
    print(str(json_file))
    json_file.save('./json/{}.json'.format(str(file_name)))
    pem_file.save('./{}.pem'.format(str(file_name)))
    pem_file.save('./pem/{}.pem'.format(str(file_name)))
    #Upload to Network
    upl = os.system("nohup sudo python3 upload.py {} &".format(file_name))
    return render_template('final_steps.html', name=None)

if __name__ == '__main__':
    app.run(debug=True)