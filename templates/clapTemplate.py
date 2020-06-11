import os
import random
from discord.ext import commands


def genCog(bot, name, dirname, emoji):
    class ClapTemplate(commands.Cog, name=name):
        def __init__(self, bot, name, dirname, emoji):
            self.bot = bot
            self.core = self.bot.get_cog('Core')
            self.name = name
            self.files = [f'./{dirname}/'+f for f in os.listdir(f'./{dirname}')]
            self.emoji = emoji

        def play(self):
            if self.core.vc is not None:
                self.core.add_stream(random.choice(self.files))
                return True
            return False

        @commands.Cog.listener()
        async def on_raw_reaction_add(self, payload):
            if str(payload.emoji) == self.emoji and payload.user_id != self.bot.user.id:
                self.play()

        @commands.Cog.listener()
        async def on_raw_reaction_remove(self, payload):
            if str(payload.emoji) == self.emoji:
                self.play()

        @commands.Cog.listener()
        async def on_message(self, message):
            triggers = [name, self.emoji]
            if any(trigger in message.content.lower() for trigger in triggers):
                if self.play():
                    await message.add_reaction(self.emoji)
    return ClapTemplate(bot, name, dirname, emoji)
