import requests
import json
import sys

mgs = str(sys.argv[1])
worker = str(sys.argv[2])

channelID = "864151408580493312" # enable dev mode on discord, right-click on the channel, copy ID
botToken = "ODY0MTUxODYyODczMTYxNzYw.YOxSIw.y_TjxcF_82niUYWppKBt1l4R9Ig"    # get from the bot page. must be a bot, not a discord app

baseURL = "https://discordapp.com/api/channels/{}/messages".format(channelID)
headers = { "Authorization":"Bot {}".format(botToken),
            "User-Agent":"myBotThing (http://socify.co.in, v0.1)",
            "Content-Type":"application/json", }

message = """

▁ ▂ ▄ ▅ ▆ ▇ █   🎀  𝑀𝑒𝓈𝓈𝒶𝑔𝑒  🎀   █ ▇ ▆ ▅ ▄ ▂ ▁

𝔸 𝕄𝕖𝕤𝕤𝕒𝕘𝕖 𝔽𝕣𝕠𝕞 𝕋𝕙𝕖 𝕀𝕟𝕤𝕥𝕒𝕟𝕔𝕖 𝕃𝕒𝕦𝕟𝕔𝕙𝕚𝕟𝕘 𝕊𝕪𝕤𝕥𝕖𝕞!
-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷
𝙈𝙚𝙨𝙨𝙖𝙜𝙚: {}
𝙁𝙧𝙤𝙢: http://{}
-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷-̷

▁ ▂ ▄ ▅ ▆ ▇ █   🎀  𝑀𝑒𝓈𝓈𝒶𝑔𝑒  🎀   █ ▇ ▆ ▅ ▄ ▂ ▁

𝕯𝖊𝖛𝖊𝖑𝖔𝖕𝖊𝖉 𝖆𝖓𝖉 𝖉𝖊𝖘𝖎𝖌𝖓𝖊𝖉 𝖇𝖞 𝕸𝖊𝖑𝖑𝖔𝕭

""".format(mgs, worker)

#𝔸 𝕄𝕖𝕤𝕤𝕒𝕘𝕖 𝔽𝕣𝕠𝕞 𝕋𝕙𝕖 𝕄𝕒𝕤𝕥𝕖𝕣 𝕊𝕖𝕣𝕧𝕖𝕣!
#𝔸 𝕄𝕖𝕤𝕤𝕒𝕘𝕖 𝔽𝕣𝕠𝕞 𝕋𝕙𝕖 𝕀𝕟𝕧𝕚𝕘𝕚𝕝𝕒𝕥𝕠𝕣 𝕊𝕖𝕣𝕧𝕖𝕣!
#𝔸 𝕄𝕖𝕤𝕤𝕒𝕘𝕖 𝔽𝕣𝕠𝕞 𝕋𝕙𝕖 𝕀𝕟𝕤𝕥𝕒𝕟𝕔𝕖 𝕃𝕒𝕦𝕟𝕔𝕙𝕚𝕟𝕘 𝕊𝕪𝕤𝕥𝕖𝕞!


POSTedJSON =  json.dumps ( {"content":message} )

r = requests.post(baseURL, headers = headers, data = POSTedJSON)
