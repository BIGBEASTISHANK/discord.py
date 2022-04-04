from setting import *

@commands.has_permissions(manage_messages=True)
@client.command(aliases=['purge'])
async def clear(ctx, amount:int):
    await ctx.channel.purge(limit=amount+1)

# Error(s)
@clear.error
async def clear_error(ctx, error):
    
    # Missing Argument(s)
    if isinstance(error, commands.MissingRequiredArgument):
        embed=discord.Embed(title="Missing Argument(s)", description=f"Please enter a number to clear!", color=0x00f2ff)
        embed.add_field(name="Example", value=f"{prefix}clear 5")
        await ctx.send(embed=embed)
        
    # Invalid Number
    elif isinstance(error, commands.BadArgument):
        embed=discord.Embed(title="Invalid Number", description="Please enter a valid number!", color=0x00f2ff)
        embed.add_field(name="Example", value=f"{prefix}clear 5")
        await ctx.send(embed=embed)
        
    # Missing permision
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(embed=discord.Embed(title="Missing Permision", description=f"Your dont have permission to clear, Nub", color=0x00f2ff))
    
    # Unknown error
    else:
        embed = discord.Embed(title="Their is an error executing the command!",
        description=f"```py\n{error} \n```", color=0x00f2ff)

        channel = client.get_channel(960447193087631371)
        await channel.send(embed=embed)
        await ctx.send(embed=embed)