from setting import *

################
# Clear command
################
@commands.has_permissions(manage_messages=True)
@client.command(aliases=['purge'])
async def clear(ctx, amount:int):
    await ctx.channel.purge(limit=amount+1)

######################
# Clear command error
######################
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Please enter a number to clear")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(f"Your dont have permission to clear, Nub")