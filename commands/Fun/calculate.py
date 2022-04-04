from setting import *

@client.command(aliases=['calc'])
async def calculate(ctx, maths: str):

    # Embeding
    embed = discord.Embed(title="Calculator", color=0x00f2ff)
    embed.add_field(name="Question",
                    value=f"```css\n{maths}```", inline=False)
    
    # Answer
    embed.add_field(
        name="Answer", value=f"```css\n{str(eval(maths))}```", inline=False)
    await ctx.send(embed=embed)

# Error(s)
@calculate.error
async def calculate_error(ctx, error):
    
    # Missing Argument(s)
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="Opprator error", description=f"Please give opprator and number", color=0x00f2ff)
        embed.add_field(name=f"Example", value=f"{prefix}calculate 5 + 5")
        await ctx.send(embed=embed)
    
    # Number error
    elif isinstance(error, commands.CommandInvokeError):
        embed = discord.Embed(
            title="Number error", description=f"Please give a valid number", color=0x00f2ff)
        embed.add_field(name=f"Example", value=f"{prefix}calculate 5 + 5")
        await ctx.send(embed=embed)
        
    # Unknown error
    else:
        embed = discord.Embed(title="Their is an error executing the command!", description=f"```py\n{error} \n```", color=0x00f2ff)

        channel = client.get_channel(960447193087631371)
        await channel.send(embed=embed)
        await ctx.send(embed=embed)

