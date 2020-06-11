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

bot = commands.Bot(command_prefix='cl!')
logging.basicConfig(level=logging.INFO)

vc = None
audio = MixedAudioSource()


def clap():
    global audio
    audio.add_stream(discord.FFmpegPCMAudio(random.choice(files)))


@bot.command()
async def connect(ctx):
    global vc
    global audio
    print('connecting')
    vc = await ctx.message.author.voice.channel.connect()
    vc.play(audio)


@bot.event
async def on_message(message):
    triggers = ['clap',':clap:','👏']
    if any(trigger in message.content.lower() for trigger in triggers):
        clap()
        await message.add_reaction('👏')

    triggers = ['carp',':fish:','🐟']
    if any(trigger in message.content.lower() for trigger in triggers):
        clap()
        await message.add_reaction('🐟')

    await bot.process_commands(message)


@bot.event
async def on_raw_reaction_add(payload):
    if str(payload.emoji) == '👏' and payload.user_id != bot.user.id:
        clap()


@bot.event
async def on_raw_reaction_remove(payload):
    if str(payload.emoji) == '👏':
        clap()


bot.run(os.getenv('BOT_TOKEN'))
