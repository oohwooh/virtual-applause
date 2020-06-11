import os
import random
from discord.ext import commands


class Clap(commands.Cog):
    def __init__(self, bot, audio):
        self.bot = bot
        self.core = self.bot.get_cog('Core')
        self.files = ['./claps/'+f for f in os.listdir('./claps')]
        self.emoji = '👏'

    def play(self, message=None):
        if self.core.vc is not None:
            self.core.add_stream(random.choice(self.files))
            return True
        return False

    @commands.Cog.listener
    async def on_raw_reaction_add(self, payload):
        if str(payload.emoji) == self.emoji and payload.user_id != self.bot.user.id:
            self.play()

    @commands.Cog.listener
    async def on_raw_reaction_remove(self, payload):
        if str(payload.emoji) == self.emoji:
            self.play()

    @commands.Cog.listener
    async def on_message(self, message):
        triggers = ['clap', self.emoji]
        if any(trigger in message.content.lower() for trigger in triggers):
            if self.play():
                await message.add_reaction(self.emoji)


def setup(bot):
    bot.add_cog(Clap(bot))
