sudo rm -r mails cryptomine
mongodump --db cryptomine --out /home/ubuntu
mongodump --db mails --out /home/ubuntu/mails
sudo zip -r bot.zip *
sudo mv bot.zip /var/www/html/db.zip