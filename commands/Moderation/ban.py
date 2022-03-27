from setting import *

##############
# Ban a user
##############
@commands.has_permissions(ban_members=True) #checking if a user has permissions
@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):

    await member.ban(reason=reason)
    await ctx.send(embed=discord.Embed(title="banned a user", description=f"{member.mention} has been banned for `{reason}`", color=0x00f2ff))

#####################
# Ban command error
#####################
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Please mention user to ban")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(f"Your dont have permission to ban, Nub")