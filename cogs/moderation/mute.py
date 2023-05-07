import disnake
from disnake.ext import commands

class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_load(self):
        print(f"[COG] {self.__cog_name__} was loaded.")

    @commands.slash_command(name="mute",
                            description="Мьютит участника.",
                            dm_permission=False)
    async def mute(self, ctx,
                   member: disnake.Member,
                   time: int,
                   reason = "не указано."):
        
        await member.timeout(duration=time, reason=reason)
        await ctx.send(f"Участник {member.mention} получил мьют на {time} секунд, по причине: {reason}")


def setup(bot):
    bot.add_cog(Mute(bot))