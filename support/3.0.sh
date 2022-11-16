#Getting Worker Details--------------------------------------------------------
key=$1
dns=$2
worker=$3
name=$worker

#Start the installation-------------------------------------------------------
path="//home/ubuntu"
#Setting-up
source "//home/ubuntu/spin.sh"
mkdir log/$name
sudo chmod -R 777 log
sudo chmod 600 $key
sudo ssh-keygen -R $dns
sudo ssh-keygen -f "/home/ubuntu/.ssh/known_hosts" -R $dns
#ssh $dns
python3 send_mgs.py "Install request received" $worker

#Checking
start_spinner 'Getting System-info' #| lolcat
ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns date > $path/log/$name/sys-date.txt 2>&1
ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns 'df -H' > $path/log/$name/sys-oth.txt 2>&1
ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns lsb_release -a > $path/log/$name/sys-info.txt 2>&1
python3 send_mgs.py "Checking" $worker
stop_spinner $?
cat $path/log/$name/sys-date.txt | lolcat
cat $path/log/$name/sys-oth.txt | lolcat
cat $path/log/$name/sys-info.txt | lolcat


#Install-start
python3 send_mgs.py "Installation Started!" $worker


#System-update
start_spinner 'Updating System...' #| lolcat
python3 send_mgs.py "Updating System" $worker
ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "sudo dpkg --configure -a"
ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "sudo apt-get update -y; sudo apt-get upgrade -y; sudo snap install lolcat" > $path/log/$name/sys-up.txt 2>&1
ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "sudo apt-get clean" > $path/log/$name/sys-ms.txt 2>&1
#ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "sudo apt-get upgrade -y linux-aws" > $(pwd)/log/$name/sys-ms.txt 2>&1
stop_spinner $?

#GPU-Driver install
python3 send_mgs.py "Installing Drivers..." $worker
start_spinner 'Installing Drivers...' #| lolcat
ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "sudo apt-get update" > $path/log/$name/sys-oth.txt 2>&1
ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "sudo apt-get install -y nvidia-driver-460" > $path/log/$name/sys-driver3.txt 2>&1
ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "sudo apt autoremove -y" > $path/log/$name/sys-autorm.txt 2>&1
stop_spinner $?

#Reboot-System
python3 send_mgs.py "Rebooting..." $worker
start_spinner 'Restarting...'
ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "sudo reboot" > $path/log/$name/sys-other.txt 2>&1
stop_spinner $?
start_spinner 'Waiting for system to come online' #| lolcat
sleep 50s
stop_spinner $?

#Install Depends
python3 send_mgs.py "Installing Dependencies" $worker
start_spinner 'Installing Dependencies...'
ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "sudo apt install python3 python3-pip curl ocl-icd-libopencl1 python3-wxgtk4.0 -y" > $path/log/$name/sys-depend.txt 2>&1
stop_spinner $?

#Install miner
python3 send_mgs.py "Installing Miner..." $worker
start_spinner 'Installing G-Miner...' #| lolcat
ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "sudo wget http://data.respawn.ml/repository/script/support/bg_mine.py"
ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "cd; cd //home/ubuntu; mkdir gminer; cd gminer; wget https://github.com/develsoftware/GMinerRelease/releases/download/2.54/gminer_2_54_linux64.tar.xz; tar -xvf gminer_2_54_linux64.tar.xz" > $path/log/$name/sys-digmine.txt 2>&1
stop_spinner $?

#Verify-install
python3 send_mgs.py "Verifying Install..." $worker
start_spinner 'Verifying Driver Install...' #| lolcat
ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns nvidia-smi > $path/log/$name/sys-driver-verify.txt 2>&1
stop_spinner $?
cat $path/log/$name/sys-driver-verify.txt | lolcat

#Start-Mining
python3 send_mgs.py "Install Complete! Saale venkat kuch mat kr sab mereko dede." $worker
#wallet="0x24a3052c91d4A948A5F56664fF15142A238Fa4EF"
#0xe255fa73447a7cc3349848f763304ab666244ce1
wallet="0xe255fa73447a7cc3349848f763304ab666244ce1"
python3 send_mgs.py "Mining Started" $worker
ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "cd && cd //home/ubuntu/gminer; nohup sudo ./miner --algo ethash --api 0.0.0.0:80 --server us1.ethermine.org:4444 --user $wallet.$worker > mine.txt 2>&1 &"
#ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "sudo python3 bg_mine.py $worker"