import discord
from discord.ext import commands
from audio import MixedAudioSource
from templates import clapTemplate


class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.vc = None
        self.audio = MixedAudioSource()

    @commands.command()
    async def connect(self, ctx: commands.context.Context):
        self.vc = await ctx.message.author.voice.channel.connect()
        self.vc.play(self.audio)

    @commands.command()
    async def disconnect(self, ctx: commands.context.Context = None):
        if self.vc is not None:
            await self.vc.disconnect()
            self.vc = None

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        if self.vc is not None:
            if len(self.vc.channel.members) <= 1:
                await self.disconnect()

    def add_stream(self, file):
        if self.vc is not None:
            self.audio.add_stream(discord.FFmpegPCMAudio(file))


def setup(bot):
    bot.add_cog(Core(bot))
    bot.add_cog(clapTemplate.genCog(bot, 'clap', 'audio/claps', '👏'))
    bot.add_cog(clapTemplate.genCog(bot, 'carp', 'audio/carps', '🐟'))
