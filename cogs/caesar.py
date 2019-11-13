import quote
import random
from data import db
import discord
from discord.ext import commands

punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~ '''

class Caesar(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command()
    async def caesar(self,ctx):
        plaintext = quote.getQuote()
        ciphertext = ""
        shift = random.randint(1,25)

        for l in list(plaintext):
            if ('a' <= l <= 'z'):
                ciphertext += chr((((ord(l) - 97) + shift) % 26)+97)

            if('A' <= l <= 'Z'):
                ciphertext += chr((((ord(l) - 65) + shift) % 26)+65)

            if(l in punctuations):
                ciphertext += l
        
        await ctx.send(f'Ciphertext: {ciphertext}')
        db.writeplaintext(ctx.message.author.id, plaintext)
        return [plaintext,ciphertext]

def setup(bot):
    bot.add_cog(Caesar(bot))

if __name__ == '__main__':
    print(Caesar.caesar())