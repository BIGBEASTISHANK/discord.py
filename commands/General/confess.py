from setting import *

##################
# Confess command
##################
@client.command()
async def confess(ctx, *,word:str):
    await ctx.channel.purge(limit=1)
    await ctx.send(f"{word}")

########################
# Confess command error
########################
@confess.error
async def confess_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Please type something to confess")
        time.sleep(5)
        await ctx.channel.purge(limit=2)