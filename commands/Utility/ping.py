from setting import *

###############
# Ping Command
###############
@client.command()
async def ping(ctx):
    await ctx.send(embed=discord.Embed(title=f"Ping", description=f"Latency: {round(client.latency * 1000)}ms", color=0x00f2ff))