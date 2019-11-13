import discord
from discord.ext import commands

if __name__ == '__main__':
    bot = commands.Bot(command_prefix=['c!', 'c.', 'c#', "c! ", "c. ", "c# "], case_insensitive=True, description="CipherBot")

    @bot.event
    async def on_ready():
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('------')
        
        await bot.change_presence(activity=discord.Activity(type=3, name="c!help"))
    
    for extension in ('cogs.affine', 'cogs.atbash', 'cogs.caesar', 'cogs.morse', 'cogs.substitution', 'cogs.check', 'cogs.scoreboard', 'cogs.help', 'cogs.quotes'):
        bot.load_extension(extension)
    
    @bot.check
    def bot_has_permissions(ctx):
        if ctx.guild is not None:
            perms = {"send_messages": True, "embed_links": True, "attach_files": True}
            guild = ctx.guild
            me = guild.me if guild is not None else ctx.bot.user
            permissions = ctx.channel.permissions_for(me)
            
            missing = [perm for perm, value in perms.items() if getattr(permissions, perm, None) != value]
            
            if not missing:
                return True
            
            raise commands.BotMissingPermissions(missing)
        else:
            return True
    
    ######
    # GLOBAL ERROR CHECKING
    ######
    @bot.event
    async def on_command_error(ctx, error):
        # don't handle errors with local handlers
        if hasattr(ctx.command, 'on_error'):
            return
        
        if isinstance(error, commands.CommandOnCooldown):  # send cooldown
            await ctx.send("**Cooldown.** Try again after " + str(round(error.retry_after)) + " s.", delete_after=5.0)
        
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send("Sorry, the command was not found.")
        
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("This command requires an argument!")
        
        elif isinstance(error, commands.BadArgument):
            await ctx.send("The argument passed was invalid. Please try again.")
        
        elif isinstance(error, commands.ArgumentParsingError):
            await ctx.send("An invalid character was detected. Please try again.")
        
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(
                f"""**The bot does not have enough permissions to fully function.**
                **Permissions Missing:** `{', '.join(map(str, error.missing_perms))}`
                *Please try again once the correct permissions are set.*"""
            )
        
        elif isinstance(error, commands.NoPrivateMessage):
            await ctx.send("**This command is unavaliable in DMs!**")
        else:
            await ctx.send(
                """**An uncaught non-command error has occurred.**
                *Please DM DeepFried#7054, or try again.*
                **Error:**  """ + str(error)
            )
            raise error
    
    @bot.command()
    @commands.is_owner()
    async def load(ctx,extension):
        bot.load_extension(f'cogs.{extension}')
    
    @bot.command()
    @commands.is_owner()
    async def unload(ctx,extension):
        bot.unload_extension(f'cogs.{extension}')
    
    @bot.command()
    @commands.is_owner()
    async def reload(ctx,extension):
        bot.unload_extension(f'cogs.{extension}')
        bot.load_extension(f'cogs.{extension}')

    token = open("token.txt", "r").read()
    bot.run(token.strip())
