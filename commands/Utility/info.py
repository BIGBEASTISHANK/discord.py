from setting import *


@client.command()
async def info(ctx):
    embed = discord.Embed(
        title=f"Info", description=f"Here is the info of this server!", color=0x00f2ff)

    embed.add_field(
        name="Server Name:", value=f"`{ctx.message.guild.name}`", inline=False)
    
    embed.add_field(
        name="Owner:", value=f"<@{ctx.message.guild.owner_id}>", inline=False)
    
    embed.add_field(
        name="Premium User:", value=f"`{ctx.message.guild.premium_subscription_count}`", inline=False)
    
    embed.add_field(
        name="Members:", value=f"`{ctx.message.guild.member_count}`", inline=False)
    
    embed.add_field(
        name="Region:", value=f"`{ctx.message.guild.region}`", inline=False)
    await ctx.send(embed=embed)
