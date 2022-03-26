from setting import *

###############
# Unban a user
###############
@commands.has_permissions(ban_members=True) #checking if a user has permissions
@client.command()
async def unban(ctx, *, member):
    banned_user = await ctx.guild.bans()
    member_name, member_discriminator= member.split('#')

    for ban_entry in banned_user:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(embed=discord.Embed(title="Unbened a user", description=f"{user.mention} has been unbaned", color=0x00f2ff))
            return

######################
# Unban command error
######################
@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Please mention user to unban")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(f"Your dont have permission to unban, Nub")