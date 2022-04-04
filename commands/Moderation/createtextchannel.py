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
    
    # Missing permision
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(embed=discord.Embed(title="Missing Permision", description=f"Your dont have permission to create a channel, Noob", color=0x00f2ff))
    
    # Unknown error
    else:
        await unknown_error(ctx, error)