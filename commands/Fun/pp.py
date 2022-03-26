from setting import *

#############
# PP command
#############
@client.command()
async def pp(ctx, member:discord.Member=None):
    random_number = randint(1, 50)
    alphabet = '='
    ppsize = alphabet * random_number
    member = member or ctx.author
    embed = discord.Embed(title='PP size machine', description=f"{member.mention}'s pp \n 8{ppsize}D", color=0x00f2ff)
    embed.set_footer(text='Yes, I stole this machine from Mito')

    await ctx.send(embed=embed)
