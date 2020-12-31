import discord
from discord.ext import commands, tasks
from discord.voice_client import VoiceClient
import youtube_dl
import ffmpeg

from random import choice

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': False,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

client = commands.Bot(command_prefix='-')

status = ['Age of Empires 2: Definitive Edition']
queue = []

@client.event
async def on_ready():
    change_status.start()
    print('Bot is online!')

@client.command(name='ping')
async def ping(ctx):
    await ctx.send(f'**Pong!** Latency: {round(client.latency * 1000)}ms')

@client.command(name='rip')
async def die(ctx):
    responses = ['Thou art human, with soul and wit. I am naught but clockwork! No wonder thou wert victorious! I shalt abdicate', 'A graceless hillock rose too near mine town center. No wonder thou wert victorious! I shalt abdicate', 'My sheep perished when I sought to use them as food. No wonder thou wert victorious! I shalt abdicate.', 'When I sent my villager to hunt wild boar, it slew him. No wonder thou wert victorious! I shalt abdicate.', 'Zounds! I accidentally resigned by mistake! No wonder thou wert victorious! I shalt abdicate.', 'My folks couldst not replant the berries! No wonder thou wert victorious!', 'The nearby boars grunted too loudly and frequently! No wonder thou wert victorious! I shall abdicate', 'I couldst not comprehend mine folks speech! No wonder thou wert victorious! I shalt abdicate']
    await ctx.send(choice(responses))

@client.command(name='join')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("Thou aren't connected. No wonder I couldst not connect.")
        return    
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()

@client.command(name='1', help='Yes')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('1.mp3'))

@client.command(name='2', help='No')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('2.mp3'))

@client.command(name='3', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('3.mp3'))

@client.command(name='4', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('4.mp3'))

@client.command(name='5', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('5.mp3'))

@client.command(name='6', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('6.mp3'))

@client.command(name='7', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('7.mp3'))

@client.command(name='8', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('8.mp3'))

@client.command(name='9', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('10.mp3'))

@client.command(name='10', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('10.mp3'))

@client.command(name='11', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('11.mp3'))

@client.command(name='12', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('12.mp3'))

@client.command(name='13', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('13.mp3'))

@client.command(name='14', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('14.mp3'))

@client.command(name='15', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('15.mp3'))

@client.command(name='16', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('16.mp3'))

@client.command(name='17', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('17.mp3'))

@client.command(name='18', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('18.mp3'))

@client.command(name='19', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('19.mp3'))

@client.command(name='20', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('20.mp3'))

@client.command(name='21', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('21.mp3'))

@client.command(name='22', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('22.mp3'))

@client.command(name='23', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('23.mp3'))

@client.command(name='24', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('24.mp3'))

@client.command(name='25', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('25.mp3'))

@client.command(name='26', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('26.mp3'))

@client.command(name='27', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('27.mp3'))

@client.command(name='28', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('28.mp3'))

@client.command(name='29', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('29.mp3'))

@client.command(name='30', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('30.mp3'))

@client.command(name='31', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('31.mp3'))

@client.command(name='32', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('32.mp3'))

@client.command(name='33', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('33.mp3'))

@client.command(name='34', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('34.mp3'))

@client.command(name='35', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('35.mp3'))
@client.command(name='36', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('36.mp3'))

@client.command(name='37', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('37.mp3'))

@client.command(name='38', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('38.mp3'))

@client.command(name='39', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('39.mp3'))

@client.command(name='40', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('40.mp3'))

@client.command(name='41', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('41.mp3'))

@client.command(name='42', help='')
async def one(ctx):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    voice.play(discord.FFmpegPCMAudio('42.mp3'))

@client.command(name='dc')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))

client.run('randomthings')