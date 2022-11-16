import discord
from discord.ext import commands
from config import mongodb_config
import pymongo
import os
import sys
#from master import send_log

#DATABASE CLIENT----------------------------------------------
myclient = pymongo.MongoClient(mongodb_config.client)
db = myclient[mongodb_config.database_name]
doc = db[mongodb_config.collection]

#Changing DNS

def dns_change_client(ip, dns):
    change = os.system("sudo bash change_dns.sh {} {}".format(ip, dns))

def dns_change(worker, ip):
	change = os.system("python3 change_dns.py {} {}".format(worker, ip))	

#Installation
def ins(worker, client):
    if client == 1:
       	install_start = os.system("python3 start_install.py {}".format(str(worker)))

    else:
        ip = "0.0.0.0"
        dns_change(worker, ip)
        install_start = os.system("python3 start_install.py {}".format(str(worker)))

#Initializing Bot and Command prefix
bot = commands.Bot(command_prefix='venkat!')

#Repeat Command
@bot.command()
async def repeat(ctx, arg):
    await ctx.send(arg)

#Command to send log
@bot.command()
async def sendlog(ctx, arg):
    embed=discord.Embed(title="Logs", url="http://socify.co.in", description="Requesting...", color=0xFF5733)
    #embed=discord.Embed(title="Logs", url="http://socify.co.in", description= send_log.log , color=0xFF5733)
    await ctx.send(embed=embed)
#Help Command
@bot.command()
async def helpme(ctx, arg):
	embed=discord.Embed(title="Help Me!", url="https://github.com/MelloB1989/miner-bot", description="Type master!menu to show menu of the instances to install, you can also manually start any installation my typing master!install <instance-name>. Waiting for your command.", color=0xFF5733)
	await ctx.send(embed=embed)



@bot.command()
async def show(ctx, work):
    #doc = db[batch]
    m = doc.find_one({'instance' : work})
    work_name = m['instance']
    work_status = m['status']
    work_dns = m['dns']
    work_su_status = m['support_status']
    work_su = m['support']
    work_pem = m['pem']
    work_aws_id = m['aws_id']
    work_aws_key = m['aws_key']
    work_lu_state = m['launch_state']
    #data_hold = m['hold']
    '''
    if data_hold == "1":
        hold = "Yes"
    else:
        hold = "No"
    if data_limit_region1 == "1":
        reg1_state = "Given"
    else:
        reg1_state = "Not Given"
    if data_limit_region2 == "1":
        reg2_state = "Given"
    else:
        reg2_state = "Not Given"
    if data_free_tier == "1":
        free_state = "Yes"
    else:
        free_state = "No"
    '''
    data = """
    Instance: {}

    *DNS*-----------
    Worker DNS: http://{}
    Support DNS: http://{}

    *Status*---------
    Worker Status: {}
    Support Status: {}
    Launch State: {}

    𝕺𝖙𝖍𝖊𝖗 𝖎𝖓𝖋𝖔-------
    PEM: http://data.respawn.ml/repository/{}
    AWS ID: {}
    AWS KEY: {}
    
    𝔻𝕖𝕧𝕖𝕝𝕠𝕡𝕖𝕕 𝕓𝕪 𝕄𝕖𝕝𝕝𝕠𝔹
        """.format(work, work_dns, work_su, work_status, work_su_status, work_lu_state, work_pem, work_aws_id, work_aws_key)
    embed=discord.Embed(title = work, url="http://"+str(work_dns), description = data , color=0xFF5733)
    await ctx.send(embed=embed)


#Install Instance
@bot.command()
async def install(ctx, work):
    embed=discord.Embed(title="Install Portal", url="http://socify.co.in", description="Checking...", color=0xFF5733)
    embed.set_footer(text="Developed and designed by MelloB.")
    await ctx.send(embed=embed)
    worker_db = doc.find_one({"instance": work})
    worker_status = worker_db['status']
    print(worker_db)
    worker_dns = worker_db['dns']
    if worker_status == "offline":
        ins(work, 1)
        embed=discord.Embed(title="Install Portal", url="https://mellob.socify.co.in/", description="Installing instance: {}".format(str(work)), color=0xFF5733)
        embed.set_footer(text="Developed and designed by MelloB.")
        await ctx.send(embed=embed)

    else:
        bmbed=discord.Embed(title="Install Portal", url="http://" + worker_dns, description="The Worker is Online. Don't fool me idiot!", color=0xFF5733)
        embed.set_footer(text="Developed and designed by MelloB.")
        await ctx.send(embed=bmbed)

#Change DNS
@bot.command()
async def dnschange(ctx, ip, dns):
    dns_change_client(ip, dns)

#Run Bot
bot.run('ODY0MDE5ODIxNDUyMDY2ODE2.YOvXKg.LDZUZJu6BB-dlOlohT6Vg8M8ly0')
