import discord
from discord.ext import commands
from audio import MixedAudioSource


class Core(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.vc = None
        self.audio = MixedAudioSource()

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = member.guild.system_channel
        if channel is not None:
            await channel.send('Welcome {0.mention}.'.format(member))

    @commands.command()
    async def connect(self, ctx: commands.context.Context):
        self.vc = await ctx.message.author.voice.channel.connect()
        self.vc.play(self.audio)

    @commands.command()
    async def disconnect(self, ctx: commands.context.Context = None):
        if self.vc is not None:
            await self.vc.disconnect()
            vc = None

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
