from setting import *

##################
# Confess command
##################
@client.command()
async def confess(ctx, *,words:str):
    await ctx.channel.purge(limit=1)

    embed=discord.Embed(title="Anonymous Confession", description=f"{words}", color=0x00f2ff)
    await ctx.send(embed=embed)

########################
# Confess command error
########################
@confess.error
async def confess_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Please type something to confess")
        time.sleep(5)
        await ctx.channel.purge(limit=2)