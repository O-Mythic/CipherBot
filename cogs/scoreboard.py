import discord
from discord.ext import commands
from data import db
from operator import itemgetter

class Scoreboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def scoreboard(self,ctx):
        leaderboard = '```'
        scores = sorted(db.readallscores(), key = itemgetter(1), reverse = True)[:5]
        server = ctx.message.guild

        if(len(scores) > 0):
                for index, score in enumerate(scores):
                    try:
                        leaderboard += f'\n{index + 1}. {server.get_member(int(scores[index][0])).display_name}'
                    except AttributeError:
                        pass
                leaderboard += '\n```'
                await ctx.send(leaderboard)
        else:
            await ctx.send("It doesn't look like anyone has played yet")

def setup(bot):
    bot.add_cog(Scoreboard(bot))
