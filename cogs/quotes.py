from discord.ext import commands
from quote import reload

class Quotes(commands.Cog):
    @commands.command()
    @commands.is_owner()
    async def reload_quotes(self, ctx):
        reload()
        ctx.send("Reloaded quotes.")


def setup(bot):
    bot.add_cog(Quotes())