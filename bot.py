import os
import traceback
import logging
from discord.ext import commands
from templates import clapTemplate

bot = commands.Bot(command_prefix='cl!')
logging.basicConfig(level=logging.INFO)

bot.load_extension('cogs.core')
bot.run(os.getenv('BOT_TOKEN'))
