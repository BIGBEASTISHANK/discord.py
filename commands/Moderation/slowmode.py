from setting import *

###################
# Slowmode command
###################
@client.command(aliases=['sm'])
@commands.has_permissions(manage_messages=True) #checking if a user has permissions
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"Set the slowmode delay in this channel to {seconds} seconds!")

#################
# slowmode error
#################
@slowmode.error
async def slowmode_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Please enter a number (seconds) to slow down the chat")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(f"Your dont have permission to slow down chat, Nub")