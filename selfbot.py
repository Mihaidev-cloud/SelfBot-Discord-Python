from http import client
import discord
from discord.ext import commands
 
client = commands.Bot(command_prefix=".", self_bot=True, help_Command=None) # here you change if you want to change the command prefix or not

token="" # This is a token where you are add the token of account!


@client.event
async def on_ready():
    print("The self-bot is Online!") # This is indicate if self-bot is working or not

@client.command()
async def startup(ctx): # This the startup message you can delete it after
    await ctx.send("```Welcome To the self-bot This the startup of self-bot, How to get started? First open the selfbot.py and edit and add your own commands of course you will have a example one! Mihaidev-Cloud 2020-2022 , Free to use https://github.com/Mihaidev-cloud/SelfBot-Discord-Python```")
 


@client.command()
async def Ping(ctx): # Exemple command for presentation!
    await ctx.send("Pong!")


client.run(token, bot=False)