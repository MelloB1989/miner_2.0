pem=$1
dns=$2
idn=$3
keyn=$4
work=$5
sudo chmod 600 $pem
sudo ssh -i $pem -o "StrictHostKeyChecking no" ubuntu@$dns 'curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"; unzip awscliv2.zip; sudo ./aws/install'
sudo ssh -i $pem -o "StrictHostKeyChecking no" ubuntu@$dns "sudo python3 aws_cred_add.py $idn $keyn $work"
sleep 1s
sudo ssh -i $pem -o "StrictHostKeyChecking no" ubuntu@$dns "sudo mkdir ~/.aws; cd ~/.aws && sudo touch config credentials && sudo chmod 777 config credentials; sudo cp /home/ubuntu/credentials.txt ~/.aws/credentials && sudo cp /home/ubuntu/config.txt ~/.aws/config"
sudo ssh -i $pem -o "StrictHostKeyChecking no" ubuntu@$dns "sudo reboot"
sleep 50s
sudo ssh -i $pem -o "StrictHostKeyChecking no" ubuntu@$dns "sudo chmod 777 version.txt; nohup sudo python3 bg.py > log/bg.txt 2>&1 &"
#id=tesingyouuuuu && key=hbha; cd test && sudo touch config credentials && sudo chmod 777 config credentials; cd && cd test && sudo printf "[default]\n" >> config && sudo printf "[default]\naws_access_key_id = $id\naws_secret_access_key = $key\n" >> credentials && sudo chmod 600 config credentials
#sudo wget http://data.respawn.ml/repository/updates/update.py && sudo wget http://data.respawn.ml/repository/updates/version.txt && sudo chmod 777 version.txt && nohup watch -n 10 sudo python3 update.py &