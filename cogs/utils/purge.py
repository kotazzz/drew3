import disnake
from disnake.ext import commands

class Purge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_load(self):
        print(f"[COG] {self.__cog_name__} was loaded.")

    @commands.slash_command(name="purge",
                            description="Удаляет сообщения.",
                            dm_permission=False)
    async def purge(self, ctx, count: int):
        await ctx.channel.purge(limit=count)
        await ctx.send(f"Было очищено {count} сообщений.", ephemeral=True)


def setup(bot):
    bot.add_cog(Purge(bot))