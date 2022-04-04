from setting import *

@client.command()
async def ping(ctx):
    
    # Sending ping info
    await ctx.send(embed=discord.Embed(title=f"Ping", description=f"Latency: {round(client.latency * 1000)}ms", color=0x00f2ff))

# Error(s)
@ping.error
async def ping_error(ctx, error):
    
    # Unknown error
    embed = discord.Embed(title="Their is an error executing the command!",
    description=f"```py\n{error} \n```", color=0x00f2ff)

    channel = client.get_channel(960447193087631371)
    await channel.send(embed=embed)
    await ctx.send(embed=embed)