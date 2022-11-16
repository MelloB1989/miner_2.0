import requests
import json
import sys

mgs = str(sys.argv[1])
worker = str(sys.argv[2])

channelID = "864947430059540480" # enable dev mode on discord, right-click on the channel, copy ID
botToken = "ODY0MDE5ODIxNDUyMDY2ODE2.YOvXKg.Z_6psyC8eR9ZcwQqngb9cD0KTkY"    # get from the bot page. must be a bot, not a discord app

baseURL = "https://discordapp.com/api/channels/{}/messages".format(channelID)
headers = { "Authorization":"Bot {}".format(botToken),
            "User-Agent":"myBotThing (http://some.url, v0.1)",
            "Content-Type":"application/json", }

message = """
###########################################
A Message From The Spectator!
---------------------
Message: {}
From: {}
---------------------

Developed and designed by MelloB
###########################################
""".format(mgs, worker)

POSTedJSON =  json.dumps ( {"content":message} )

r = requests.post(baseURL, headers = headers, data = POSTedJSON)
