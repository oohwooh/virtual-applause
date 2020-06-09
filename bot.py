import os
import random
import logging
import discord
import queue
import asyncio
import threading
import time

from discord.ext import commands

files = ['./claps/'+f for f in os.listdir('./claps')]

claps = queue.Queue()
loop = asyncio.get_event_loop()

bot = commands.Bot(command_prefix='cl!')
proxy1 = commands.Bot(command_prefix='cl!')
proxy2 = commands.Bot(command_prefix='cl!')
logging.basicConfig(level=logging.INFO)
#discord.opus.load_opus()


def clap_worker(vc, queue):
    print('creating worker')

    # vc = message.guild.voice_client
    # clap = discord.FFmpegPCMAudio(random.choice(files))
    while vc:
        time.sleep(1)
        if not vc.is_playing() and not queue.empty():
            try:
                print('clap')
                clap = queue.get_nowait()
                vc.play(clap, after=queue.task_done())
            except:
                pass
    print('worker destroyed')


@bot.command()
async def connect(ctx):
    print('connecting')
    vc = await ctx.message.author.voice.channel.connect()

    threading.Thread(target=clap_worker, args=(vc,claps)).start()

@proxy1.command()
async def connect(ctx):
    print('connecting1')
    vc = await ctx.message.author.voice.channel.connect()

    threading.Thread(target=clap_worker, args=(vc,claps)).start()

@proxy2.command()
async def connect(ctx):
    print('connecting2')
    vc = await ctx.message.author.voice.channel.connect()
    threading.Thread(target=clap_worker, args=(vc,claps)).start()

@bot.event
async def on_message(message):
    triggers = ['clap',':clap:','👏']
    if any(trigger in message.content.lower() for trigger in triggers):
        claps.put_nowait(discord.FFmpegPCMAudio(random.choice(files)))
        await message.add_reaction('👏')

    triggers = ['carp',':fish:','🐟']
    if any(trigger in message.content.lower() for trigger in triggers):
        claps.put_nowait(discord.FFmpegPCMAudio(random.choice(files)))
        await message.add_reaction('🐟')
    await bot.process_commands(message)


@bot.event
async def on_raw_reaction_add(payload):
    if str(payload.emoji) == '👏':
        for i in range(random.randint(1,5)):
            claps.put_nowait(discord.FFmpegPCMAudio(random.choice(files)))


@bot.event
async def on_raw_reaction_remove(payload):
    if str(payload.emoji) == '👏':
        claps.put_nowait(discord.FFmpegPCMAudio(random.choice(files)))

task1 = loop.create_task(bot.start(os.getenv('TOKEN_1')))
task2 = loop.create_task(proxy1.start(os.getenv('TOKEN_2')))
task3 = loop.create_task(proxy2.start(os.getenv('TOKEN_3')))
gathered = asyncio.gather(task1, task2, task3, loop=loop)
loop.run_until_complete(gathered)