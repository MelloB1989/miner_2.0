pem=$1
dns=$2
key=$3
json=$4
sudo chmod 600 $key
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "sudo apt update && sudo snap install lolcat"
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "sudo apt install lolcat apache2 python3-pip zip unzip -y"
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "cd //var/www && sudo chmod -R 777 *"
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "wget http://data.respawn.ml/repository/script/mellob_support.zip && sudo unzip mellob_support.zip && sudo chmod -R 777 *"
#sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "wget http://data.socify.cf/repository/3.0/2vcpu/spin.sh"
#sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "wget http://data.socify.cf/repository/3.0/su/send_mgs.py"
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "mkdir log"
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "sudo chmod -R 777 log"
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "wget http://data.respawn.ml/repository/$key"
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "wget http://data.respawn.ml/repository/json/$json"
#sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "sudo unzip pem.zip"
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "sudo chmod 777 *"
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "sudo rm /var/www/html/index.html"
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "cd /var/www/html && sudo wget http://data.respawn.ml/repository/extra/index.html"
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "pip3 install pymongo discord.py requests"
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "nohup sudo python3 bg.py &"