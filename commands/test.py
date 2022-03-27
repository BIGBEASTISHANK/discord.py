from setting import *

@client.command()
async def test(guild):
    await guild.send(guild.name)