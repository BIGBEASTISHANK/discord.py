from setting import *

####################
# Calcultor command
####################


@client.command(aliases=['calc'])
async def calculate(ctx, maths: str):

    embed = discord.Embed(title="Calculator", color=0x00f2ff)
    embed.add_field(name="Question",
                    value=f"```css\n{maths}```", inline=False)
    embed.add_field(
        name="Answer", value=f"```css\n{str(eval(maths))}```", inline=False)
    await ctx.send(embed=embed)

###################
# Calculator error
###################


@calculate.error
async def calculate_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            title="Opprator error", description=f"Please give opprator and number", color=0x00f2ff)
        embed.add_field(name=f"Example", value=f"{prefix}calculate 5 + 5")
        await ctx.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
        embed = discord.Embed(
            title="Number error", description=f"Please give a valid number", color=0x00f2ff)
        embed.add_field(name=f"Example", value=f"{prefix}calculate 5 + 5")
        await ctx.send(embed=embed)
