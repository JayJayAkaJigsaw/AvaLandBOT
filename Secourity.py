import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time


Client = discord.Client() #Initialise Client 
client = commands.Bot(command_prefix = "?") #Initialise client bot


@client.event 
async def on_ready():
    print("Server is protect") #This will be called when the bot connects to the server

@client.event
async def on_message(message):	
    if message.content == "kurwa":
         await client.send_message(message.channel, ":warning: Break the rules :warning: \n &1 a < at rules \n <@377356614027444227> <@404013708105482242>")
         testmsgueser = message.author
         user = testmsgueser
         role = discord.utils.find(lambda r: r.name == "Member", message.server.roles)        
         await client.remove_roles(user, role)
    if message.content == "fuck":
         await client.send_message(message.channel, ":warning: Break the rules :warning: \n &1 a < at rules \n <@377356614027444227> <@404013708105482242>")
         testmsgueser = message.author
         user = testmsgueser
         role = discord.utils.find(lambda r: r.name == "Member", message.server.roles)        
         await client.remove_roles(user, role)
    if message.content == "debilu":
         await client.send_message(message.channel, ":warning: Break the rules :warning: \n &1 e < at rules \n <@377356614027444227> <@404013708105482242>")
         testmsgueser = message.author
         user = testmsgueser
         role = discord.utils.find(lambda r: r.name == "Member", message.server.roles)        
         await client.remove_roles(user, role)
    if message.content == "bitch":
         await client.send_message(message.channel, ":warning: Break the rules :warning: \n &1 e < at rules \n <@377356614027444227> <@404013708105482242>")
         testmsgueser = message.author
         user = testmsgueser
         role = discord.utils.find(lambda r: r.name == "Member", message.server.roles)        
         await client.remove_roles(user, role)
    if message.content == "chuju":
         await client.send_message(message.channel, ":warning: Break the rules :warning: \n &1 e < at rules \n <@377356614027444227> <@404013708105482242>")
         testmsgueser = message.author
         user = testmsgueser
         role = discord.utils.find(lambda r: r.name == "Member", message.server.roles)        
         await client.remove_roles(user, role)
    if message.content == "chuj":
         await client.send_message(message.channel, ":warning: Break the rules :warning: \n &1 a < at rules \n <@377356614027444227> <@404013708105482242>")      
         testmsgueser = message.author
         user = testmsgueser
         role = discord.utils.find(lambda r: r.name == "Member", message.server.roles)        
         await client.remove_roles(user, role)
    if message.content == "japierdole":
         await client.send_message(message.channel, ":warning: Break the rules :warning: \n &1 a < at rules \n <@377356614027444227> <@404013708105482242>")   
         testmsgueser = message.author
         user = testmsgueser
         role = discord.utils.find(lambda r: r.name == "Member", message.server.roles)        
         await client.remove_roles(user, role)
    if message.content == "jd":
         await client.send_message(message.channel, ":warning: Break the rules :warning: \n &1 e < at rules \n <@377356614027444227> <@404013708105482242>") 
         testmsgueser = message.author
         user = testmsgueser
         role = discord.utils.find(lambda r: r.name == "Member", message.server.roles)        
         await client.remove_roles(user, role)
    if message.content == "frajer":
         await client.send_message(message.channel, ":warning: Break the rules :warning: \n &1 e < at rules \n <@377356614027444227> <@404013708105482242>") 
         testmsgueser = message.author
         user = testmsgueser
         role = discord.utils.find(lambda r: r.name == "Member", message.server.roles)        
         await client.remove_roles(user, role)
    if message.content == "kuhwa":
         await client.send_message(message.channel, ":warning: Break the rules :warning: \n &1 a < at rules \n <@377356614027444227> <@404013708105482242>")
         testmsgueser = message.author
         user = testmsgueser
         role = discord.utils.find(lambda r: r.name == "Member", message.server.roles)        
         await client.remove_roles(user, role)
    if message.content == "kur/wa":
         await client.send_message(message.channel, ":warning: Break the rules :warning: \n &1 a < at rules \n <@377356614027444227> <@404013708105482242>")
         testmsgueser = message.author
         user = testmsgueser
         role = discord.utils.find(lambda r: r.name == "Member", message.server.roles)        
         await client.remove_roles(user, role)
    if message.content == "k/u/r/w/a":
         await client.send_message(message.channel, ":warning: Break the rules :warning: \n &1 a < at rules \n <@377356614027444227> <@404013708105482242>")
         testmsgueser = message.author
         user = testmsgueser
         role = discord.utils.find(lambda r: r.name == "Member", message.server.roles)        
         await client.remove_roles(user, role)
    if message.content == "ku/rwa":
         await client.send_message(message.channel, ":warning: Break the rules :warning: \n &1 a < at rules \n <@377356614027444227> <@404013708105482242>")
         testmsgueser = message.author
         user = testmsgueser
         role = discord.utils.find(lambda r: r.name == "Member", message.server.roles)        
         await client.remove_roles(user, role)
    if message.content == "jebac":
         await client.send_message(message.channel, ":warning: Break the rules :warning: \n &1 a < at rules \n <@377356614027444227> <@404013708105482242>")
         testmsgueser = message.author
         user = testmsgueser
         role = discord.utils.find(lambda r: r.name == "Member", message.server.roles)        
         await client.remove_roles(user, role)
    if message.content == "zjeb":
         await client.send_message(message.channel, ":warning: Break the rules :warning: \n &1 e < at rules \n <@377356614027444227> <@404013708105482242>")
         testmsgueser = message.author
         user = testmsgueser
         role = discord.utils.find(lambda r: r.name == "Member", message.server.roles)        
         await client.remove_roles(user, role)
    if message.content == "pizda":
         await client.send_message(message.channel, ":warning: Break the rules :warning: \n &1 e < at rules \n <@377356614027444227> <@404013708105482242>")
         testmsgueser = message.author
         user = testmsgueser
         role = discord.utils.find(lambda r: r.name == "Member", message.server.roles)        
         await client.remove_roles(user, role)
    if message.content == "jebie":
         await client.send_message(message.channel, ":warning: Break the rules :warning: \n &1 e < at rules \n <@377356614027444227> <@404013708105482242>")
         testmsgueser = message.author
         user = testmsgueser
         role = discord.utils.find(lambda r: r.name == "Member", message.server.roles)        
         await client.remove_roles(user, role)
    if message.content == "jebalem":
         await client.send_message(message.channel, ":warning: Break the rules :warning: \n &1 e < at rules \n <@377356614027444227> <@404013708105482242>")
         testmsgueser = message.author
         user = testmsgueser
         role = discord.utils.find(lambda r: r.name == "Member", message.server.roles)        
         await client.remove_roles(user, role)
    if message.content == "jebałem":
         await client.send_message(message.channel, ":warning: Break the rules :warning: \n &1 a < at rules \n <@377356614027444227> <@404013708105482242>")
         testmsgueser = message.author
         user = testmsgueser
         role = discord.utils.find(lambda r: r.name == "Member", message.server.roles)        
         await client.remove_roles(user, role)
    if message.content == "matkojebca":
         await client.send_message(message.channel, ":warning: Break the rules :warning: \n &1 e < at rules \n <@377356614027444227> <@404013708105482242>")
         testmsgueser = message.author
         user = testmsgueser
         role = discord.utils.find(lambda r: r.name == "Member", message.server.roles)        
         await client.remove_roles(user, role)
    if message.content == "wyjebane":
         await client.send_message(message.channel, ":warning: Break the rules :warning: \n &1 a < at rules \n <@377356614027444227> <@404013708105482242>")
         testmsgueser = message.author
         user = testmsgueser
         role = discord.utils.find(lambda r: r.name == "Member", message.server.roles)        
         await client.remove_roles(user, role)
    if message.content == "jebać":
         await client.send_message(message.channel, ":warning: Break the rules :warning: \n &1 a < at rules \n <@377356614027444227> <@404013708105482242>")
         testmsgueser = message.author
         user = testmsgueser
         role = discord.utils.find(lambda r: r.name == "Member", message.server.roles)        
         await client.remove_roles(user, role)
    if message.content == "KURWA":
         await client.send_message(message.channel, ":warning: Break the rules :warning: \n &1 a < at rules \n <@377356614027444227> <@404013708105482242>")
         testmsgueser = message.author
         user = testmsgueser
         role = discord.utils.find(lambda r: r.name == "Member", message.server.roles)        
         await client.remove_roles(user, role)
    if message.content == "ja pierdole":
         await client.send_message(message.channel, ":warning: Break the rules :warning: \n &1 a < at rules \n <@377356614027444227> <@404013708105482242>")
         testmsgueser = message.author
         user = testmsgueser
         role = discord.utils.find(lambda r: r.name == "Member", message.server.roles)        
         await client.remove_roles(user, role)
    if message.content == "JA PIERDOLE":
         await client.send_message(message.channel, ":warning: Break the rules :warning: \n &1 a < at rules \n <@377356614027444227> <@404013708105482242>")
         testmsgueser = message.author
         user = testmsgueser
         role = discord.utils.find(lambda r: r.name == "Member", message.server.roles)        
         await client.remove_roles(user, role)
    if message.content == "kurwo":
         await client.send_message(message.channel, ":warning: Break the rules :warning: \n &1 e < at rules \n <@377356614027444227> <@404013708105482242>")
         testmsgueser = message.author
         user = testmsgueser
         role = discord.utils.find(lambda r: r.name == "Member", message.server.roles)        
         await client.remove_roles(user, role)



































         
    if message.content == "jaki frajer":
         await client.send_message(message.channel, ":warning: Break the rules :warning: \n &1 e < at rules \n <@377356614027444227> <@404013708105482242>")
         testmsgueser = message.author
         user = testmsgueser
         role = discord.utils.find(lambda r: r.name == "Member", message.server.roles)        
         await client.remove_roles(user, role)
    if message.content == "jaki frajer z ciebie":
         await client.send_message(message.channel, ":warning: Break the rules :warning: \n &1 e < at rules \n <@377356614027444227> <@404013708105482242>")       
         testmsgueser = message.author
         user = testmsgueser
         role = discord.utils.find(lambda r: r.name == "Member", message.server.roles)        
         await client.remove_roles(user, role)
    if message.content == "!Sheriff":
         await client.send_message(message.channel, ":warning: Someone break the rules :warning: \n I called for: \n <@377356614027444227> <@404013708105482242>")   
    if message.content == "!sheriff":
         await client.send_message(message.channel, ":warning: Someone break the rules :warning: \n I called for: \n <@377356614027444227> <@404013708105482242>")   





client.run("NDU0NzA4MTg4NzcyODI3MTU4.DfxXiQ.I-pkNgSDeAc79vnHO-Whx1KhE_0") #Replace token with your bots token
