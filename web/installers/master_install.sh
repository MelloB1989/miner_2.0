pem=$1
dns=$2
key=$pem
sudo chmod 600 $key
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "sudo apt update && sudo snap install lolcat"
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "sudo apt install python3-pip apache2 zip unzip -y"
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "pip3 install discord.py pymongo flask"
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "export FLASK_ENV=development"
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "export FLASK_APP=app.py"
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "sudo wget http://data.respawn.ml/repository/script/master.zip"
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "sudo unzip master.zip"
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "sudo chmod -R 777 *"
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "nohup sudo python3 main.py > log/master-bot.txt 2>&1 &"
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "nohup watch -n 10 sudo python3 main.py > log/backs.txt 2>&1 &"
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "nohup sudo python3 offline_worker_get.py > log/offline-worker.txt 2>&1 &"
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "nohup watch -n 10 sudo python3 offline_worker_get.py > log/fucks.txt 2>&1 &"
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "nohup sudo python3 -m flask run --host 0.0.0.0 --port 5555 > log/srv.txt 2>&1 &"