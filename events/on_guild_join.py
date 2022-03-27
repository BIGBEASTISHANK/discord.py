from setting import *

@client.event
async def on_guild_join(guild):
    channel = client.get_channel(826738618486751242)
    
    embed = discord.Embed(title="Joined A New server!", color=0x00f2ff)
    embed.add_field(name="Name:", value=f"`{guild.name}`", inline=True)
    embed.add_field(name="Members:", value=f"`{guild.member_count}`", inline=True)

    embed.set_footer(text=f"{datetime.utcnow().strftime('%B %d, %y | %I:%M')}")

    await channel.send(embed=embed)
    return