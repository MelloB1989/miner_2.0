from discord import message
import discord
from discord.ext import commands

#Initializing Bot and Command prefix
bot = commands.Bot(command_prefix='worker!')

#Repeat Command
@bot.command()
async def repeat(ctx, arg):
    await ctx.send(arg)

#Help Command
@bot.command()
async def stat(ctx, rehash, cuhash, avghash, activew, shares, upay):
    print (ctx)
    #ctx = "<discord.ext.commands.context.Context object at 0x000001D6FAB3DAF0>"
	#### Create the initial embed object ####
    embed=discord.Embed(title="Ethermine Stats", url="https://mellob.socify.co.in", description="Ethermine Stats.", color=0x109319)

    # Add author, thumbnail, fields, and footer to the embed
    embed.add_field(name="Reported Hashrate", value="{} MH/s".format(rehash), inline=False) 
    embed.add_field(name="Current Hashrate", value="{} MH/s".format(cuhash), inline=True)
    embed.add_field(name="Average Hashrate", value="{} MH/s".format(avghash), inline=True)
    embed.add_field(name="Workers", value="{} workers".format(activew), inline=True)
    embed.add_field(name="Shares", value="{} shares".format(shares), inline=True)
    embed.add_field(name="Unpaid Balance", value="{} Eth".format(upay), inline=True)

    embed.set_footer(text="Developed and designed by MelloB")

    await ctx.send(embed=embed)
    

bot.run("ODY0MDQxODIwMjY1OTA2MjA2.YOvrpw.BpdB43GA2AUUpVDF9mU3yj32owI")