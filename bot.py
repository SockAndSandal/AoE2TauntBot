import discord
from discord.ext import commands, tasks
from discord.voice_client import VoiceClient
import ffmpeg

from random import choice

ffmpeg_options = {
    'options': '-vn'
}

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

@client.command(name='v', help='')
async def one(ctx, num):
    server = ctx.message.guild
    voice_channel = ctx.author.voice.channel
    voice = ctx.channel.guild.voice_client
    if voice is None:
        voice = await voice_channel.connect()
    elif voice != voice_channel:
        voice.move_to(voice_channel)
    elif voice==voice_channel:
        pass
    if num == 'abhiroop':
        voice.play(discord.FFmpegPCMAudio('24.mp3'))
    else:
        voice.play(discord.FFmpegPCMAudio(num+'.mp3'))
        
@client.command(name='dc')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    await voice_client.disconnect()

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(choice(status)))

client.run('insertcodehere')