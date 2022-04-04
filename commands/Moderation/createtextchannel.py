from setting import *

@commands.has_permissions(manage_channels=True)
@client.command(aliases=["ctc"])
async def createtextchannel(ctx, *,name: str):
    
    # Basic task
    name = name.replace(" ", "-")

    # Creating channel
    await ctx.guild.create_text_channel(name, category=ctx.channel.category)
    channel = get(ctx.guild.text_channels, name=name)

    embed=discord.Embed(title="Create Text Channel", description=f"{channel.mention} channel created sucessfully", color=0x00f2ff)
    await ctx.send(embed=embed)

# Error(s)
@createtextchannel.error
async def createtextchannel_error(ctx, error):
    
    # Unknown error
    embed = discord.Embed(title="Their is an error executing the command!",
    description=f"```py\n{error} \n```", color=0x00f2ff)

    channel = client.get_channel(960447193087631371)
    await channel.send(embed=embed)
    await ctx.send(embed=embed)