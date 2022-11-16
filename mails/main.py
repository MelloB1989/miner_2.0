'''
***************************************************
Code Author:- MelloB(https://github.com/MelloB1989)
***************************************************
'''
import os
import sys
import pymongo
import discord
from discord.ext import commands
import time

#DATABASE CLIENT----------------------------------------------
myclient = pymongo.MongoClient("mongodb://myUserAdmin:Vaishnavi%21s143%40mellob1989%40database-db.socify.cf@db.respawn.ml:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false")
db = myclient["mails"]

#Initializing Bot and Command prefix
bot = commands.Bot(command_prefix='mailer!')
notice = """
Calling database....

Please don't send any message while I do my work.

Thankyou!
"""
@bot.command()
async def list(ctx, batch):
    doc = db[batch]
    embed=discord.Embed(title="Mailer", url="http://socify.co.in", description = notice, color=0xFF5733)
    await ctx.send(embed=embed)
    mail_list = doc.find()
    #lists = mail_list['mail']
    #print("aksjasjkdjkasjk"+mail_list)
    for m in mail_list:
        data_mail = m['mail']
        data_req_date = m['req_date']
        data_acc_made = m['acc_made_on']
        data_free_tier = m['free_tier']
        data_free_tier_date = m['free_tier_date']
        data_limit_region1 = m['limit_region1']
        data_limit_region2 = m['limit_region2']
        data_region1 = m['region1']
        data_region2 = m['region2']
        data_hold = m['hold']
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
        data = """
        Mail: {}

        𝕯𝖆𝖙𝖊𝖘-----------
        Account made on: {}
        Free tier opened on: {}
        Limits requested on: {}

        𝕽𝖊𝖌𝖎𝖔𝖓𝖘---------
        Region 1: {}
        Region 1: {}

        𝕺𝖙𝖍𝖊𝖗 𝖎𝖓𝖋𝖔-------
        Is free tier opened: {}
        Region 1 limit state: {}
        Region 2 limit state: {}
        Is the acc on hold: {}

        𝔻𝕖𝕧𝕖𝕝𝕠𝕡𝕖𝕕 𝕓𝕪 𝕄𝕖𝕝𝕝𝕠𝔹
        """.format(data_mail, data_acc_made, data_free_tier_date, data_req_date, data_region1, data_region2, free_state, reg1_state, reg2_state, hold)
        embed=discord.Embed(title = data_mail, url="http://socify.co.in", description = data , color=0xFF5733)
        await ctx.send(embed=embed)

    embed=discord.Embed(title="Mailer Bot", url="http://socify.co.in", description = "All Done!" , color=0xFF5733)
    await ctx.send(embed=embed)

@bot.command()
async def addmail(ctx, batch, mail):
    doc = db[batch]
    data = { "mail" : mail, "acc_made_on" : "null", "free_tier" : "null", "free_tier_date" : "null", "limit_region1" : "null", "limit_region2" : "null", "region1" : "null", "region2" : "null", "req_date" : "null", "hold" : "null" }
    x = doc.insert_one(data)
    embed=discord.Embed(title="Mailer", url="http://socify.co.in", description = "Mail Added!", color=0xFF5733)
    await ctx.send(embed=embed)

@bot.command()
async def show(ctx, batch, mail):
    doc = db[batch]
    m = doc.find_one({'mail' : mail})
    data_mail = m['mail']
    data_req_date = m['req_date']
    data_acc_made = m['acc_made_on']
    data_free_tier = m['free_tier']
    data_free_tier_date = m['free_tier_date']
    data_limit_region1 = m['limit_region1']
    data_limit_region2 = m['limit_region2']
    data_region1 = m['region1']
    data_region2 = m['region2']
    data_hold = m['hold']
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
    data = """
    Mail: {}

    𝕯𝖆𝖙𝖊𝖘-----------
    Account made on: {}
    Free tier opened on: {}
    Limits requested on: {}

    𝕽𝖊𝖌𝖎𝖔𝖓𝖘---------
    Region 1: {}
    Region 1: {}

    𝕺𝖙𝖍𝖊𝖗 𝖎𝖓𝖋𝖔-------
    Is free tier opened: {}
    Region 1 limit state: {}
    Region 2 limit state: {}
    Is the acc on hold: {}

    𝔻𝕖𝕧𝕖𝕝𝕠𝕡𝕖𝕕 𝕓𝕪 𝕄𝕖𝕝𝕝𝕠𝔹
        """.format(data_mail, data_acc_made, data_free_tier_date, data_req_date, data_region1, data_region2, free_state, reg1_state, reg2_state, hold)
    embed=discord.Embed(title = data_mail, url="http://socify.co.in", description = data , color=0xFF5733)
    await ctx.send(embed=embed)

@bot.command()
async def listm(ctx, batch):
    embed=discord.Embed(title="Mailer", url="http://socify.co.in", description = "Hello, I will now list all mails so that you select which one to update.", color=0xFF5733)
    await ctx.send(embed=embed)
    doc = db[batch]
    ml = doc.find()
    for m in ml:
        mai = m['mail']
        embed=discord.Embed(title=mai, url="http://socify.co.in", description = "", color=0xFF5733)
        await ctx.send(embed=embed)
    embed=discord.Embed(title="Mailer Bot", url="http://socify.co.in", description = "All Done!" , color=0xFF5733)
    await ctx.send(embed=embed)
    #time.sleep(1)

'''
@bot.command()
async def addmail(ctx, batch, mail, accd, fd, ld, r1, r2, f, r1s, r2s):
    break
'''

@bot.command()
async def r1(ctx, batch, mail, r1):
    doc = db[batch]
    current_mail = doc.find_one({ 'mail' : mail})
    update_this = doc.update_one({ 'mail' : mail}, {"$set": {'region1' : r1}})
    embed=discord.Embed(title="Mailer", url="http://socify.co.in", description = "Changes Applied.", color=0xFF5733)
    await ctx.send(embed=embed)

@bot.command()
async def r2(ctx, batch, mail, r2):
    doc = db[batch]
    current_mail = doc.find_one({ 'mail' : mail})
    update_this = doc.update_one({ 'mail' : mail}, {"$set": {'region2' : r2}})
    embed=discord.Embed(title="Mailer", url="http://socify.co.in", description = "Changes Applied.", color=0xFF5733)
    await ctx.send(embed=embed)

@bot.command()
async def hold(ctx, batch, mail, h):
    doc = db[batch]
    current_mail = doc.find_one({ 'mail' : mail})
    update_this = doc.update_one({ 'mail' : mail}, {"$set": {'hold' : h}})
    embed=discord.Embed(title="Mailer", url="http://socify.co.in", description = "Changes Applied.", color=0xFF5733)
    await ctx.send(embed=embed)


@bot.command()
async def accdup(ctx, batch, mail, accd):
    doc = db[batch]
    current_mail = doc.find_one({ 'mail' : mail})
    update_this = doc.update_one({ 'mail' : mail}, {"$set": {'acc_made_on' : accd}})
    embed=discord.Embed(title="Mailer", url="http://socify.co.in", description = "Changes Applied.", color=0xFF5733)
    await ctx.send(embed=embed)


@bot.command()
async def fdup(ctx, batch, mail, fd):
    doc = db[batch]
    current_mail = doc.find_one({ 'mail' : mail})
    update_this = doc.update_one({ 'mail' : mail}, {"$set": {'free_tier_date' : fd}})
    embed=discord.Embed(title="Mailer", url="http://socify.co.in", description = "Changes Applied.", color=0xFF5733)
    await ctx.send(embed=embed)

@bot.command()
async def ldup(ctx, batch, mail, ld):
    doc = db[batch]
    current_mail = doc.find_one({ 'mail' : mail})
    update_this = doc.update_one({ 'mail' : mail}, {"$set": {'req_date' : ld}})
    embed=discord.Embed(title="Mailer", url="http://socify.co.in", description = "Changes Applied.", color=0xFF5733)
    await ctx.send(embed=embed)

@bot.command()
async def r1sup(ctx, batch, mail, r1s):
    doc = db[batch]
    current_mail = doc.find_one({ 'mail' : mail})
    update_this = doc.update_one({ 'mail' : mail}, {"$set": {'limit_region1' : r1s}})
    embed=discord.Embed(title="Mailer", url="http://socify.co.in", description = "Changes Applied.", color=0xFF5733)
    await ctx.send(embed=embed)

@bot.command()
async def r2sup(ctx, batch, mail, r2s):
    doc = db[batch]
    current_mail = doc.find_one({ 'mail' : mail})
    update_this = doc.update_one({ 'mail' : mail}, {"$set": {'limit_region2' : r2s}})
    embed=discord.Embed(title="Mailer", url="http://socify.co.in", description = "Changes Applied.", color=0xFF5733)
    await ctx.send(embed=embed)

@bot.command()
async def fup(ctx, batch, mail, f):
    doc = db[batch]
    current_mail = doc.find_one({ 'mail' : mail})
    update_this = doc.update_one({ 'mail' : mail}, {"$set": {'free_tier' : f}})
    embed=discord.Embed(title="Mailer", url="http://socify.co.in", description = "Changes Applied.", color=0xFF5733)
    await ctx.send(embed=embed)

#Run Bot
bot.run('ODc3NDE4ODQ0MzcxNjgxMzAw.YRyV-g.tdB5SBHb-3qY1qnbpwJBAUyS9mw')