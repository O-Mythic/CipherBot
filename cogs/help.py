import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        bot.remove_command('help')
    
    @commands.command()
    async def help(self,ctx):
        await ctx.send(
        "So you want to be a codebuster? Alright.\n```Command format: c![command]\nCipher types: Affine, Atbash, Caesar, Pollux, Aristocrat, Patistocrat\nUse c!check to check your decryption and c!scoreboard to check the server scoreboard```\nGood luck!"
        )

def setup(bot):
    bot.add_cog(Help(bot))