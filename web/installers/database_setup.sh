pem=$1
dns=$2
key=$pem
sudo chmod 600 $key
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "sudo apt update && sudo apt upgrade -y"
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "sudo apt install apache2 -y"
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "wget -qO - https://www.mongodb.org/static/pgp/server-5.0.asc | sudo apt-key add -"
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns 'echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/5.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-5.0.list'
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "sudo apt-get update"
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "sudo apt-get install -y mongodb-org"
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "sudo systemctl daemon-reload"
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "sudo systemctl stop mongod"
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "cd /etc && sudo rm mongod.conf && sudo wget http://data.respawn.ml/repository/extra/mongod.conf"
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "sudo systemctl enable mongod"
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "echo 'Man!!! Frustrated!'"
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns '
use admin
db.createUser(
  {
    user: "myUserAdmin",
    pwd: "Vaishnavi!s143@mellob1989@database-db.socify.cf", // or cleartext password
    roles: [
      { role: "userAdminAnyDatabase", db: "admin" },
      { role: "readWriteAnyDatabase", db: "admin" }
    ]
  }
)
'
sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "sudo systemctl start mongod"
#sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "
#sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "
#sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "
#sudo ssh -i $key -o "StrictHostKeyChecking no" ubuntu@$dns "
