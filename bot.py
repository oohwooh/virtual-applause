import os
import random
import logging
import discord
from audio import MixedAudioSource
from discord.ext import commands

carps = ['./carps/'+f for f in os.listdir('./carps')]
claps = ['./claps/'+f for f in os.listdir('./claps')]

bot = commands.Bot(command_prefix='cl!')
logging.basicConfig(level=logging.INFO)

vc = None
audio = MixedAudioSource()


def clap():
    global audio
    audio.add_stream(discord.FFmpegPCMAudio(random.choice(claps)))


def carp():
    global audio





@bot.event
async def on_message(message):
    triggers = ['clap',':clap:','👏']
    if any(trigger in message.content.lower() for trigger in triggers):
        global vc
        if vc is not None:
            clap()
            await message.add_reaction('👏')

    triggers = ['carp',':fish:','🐟']
    if any(trigger in message.content.lower() for trigger in triggers):
        global vc
        if vc is not None:
            carp()
            await message.add_reaction('🐟')
    await bot.process_commands(message)



bot.run(os.getenv('BOT_TOKEN'))
