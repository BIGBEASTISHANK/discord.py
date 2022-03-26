from setting import *

##############
# Kick a user
##############
@commands.has_permissions(kick_members=True) #checking if a user has permissions
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):

    await member.kick(reason=reason)
    await ctx.send(embed=discord.Embed(title="Kicked a user", description=f"{member.mention} has been kick for `{reason}`", color=0x00f2ff))

#####################
# Kick command error
#####################
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Please mention user to kick")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(f"Your dont have permission to kick, Nub")