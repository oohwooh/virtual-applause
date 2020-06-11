import os
import random
import logging
import discord
import queue
import asyncio
from audio import MixedAudioSource
from discord.ext import commands

crabs = ['./crabs/'+f for f in os.listdir('./crabs')]
files = ['./claps/'+f for f in os.listdir('./claps')]

claps = queue.Queue()
loop = asyncio.get_event_loop()

bot = commands.Bot(command_prefix='cl!')
logging.basicConfig(level=logging.INFO)

vc = None
@bot.command()
async def connect(ctx):
    global vc
    print('connecting')
    vc = await ctx.message.author.voice.channel.connect()


@bot.command()
async def test_mixing(ctx):
    vc.play(MixedAudioSource(discord.FFmpegPCMAudio(random.choice(files)), discord.FFmpegPCMAudio(random.choice(files))))
bot.run(os.getenv('BOT_TOKEN'))