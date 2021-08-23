############################
# Importing Module required
############################
from setting import *

#############################
# Defining client and prefix
#############################
client = commands.Bot(command_prefix=commands.when_mentioned_or(prefix), help_command=None)

####################
# When bot is ready
####################
@client.event
async def on_ready():
    print("Bot started")

    await client.change_presence(status=status, activity=activity)

#####################
# Gloabl error check
#####################
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f"Command not found!")

################
# Checking user
################
def owner(ctx):
    return ctx.author.id == 599883476522631178

###############
# Help command
###############
@client.command(aliases=['h'])
async def help(ctx, command_help:str):
    if command_help == 'ping':
        await ctx.send(embed=discord.Embed(title=f"Ping help command", description=f"This will tell you the ping of bot!", color=0x00f2ff))
    elif command_help == 'kick':
        embed=discord.Embed(title=f"Kick help command", description=f"This will kick user", color=0x00f2ff)
        embed.add_field(name=f"Example", value=f"{prefix}kick @Example For example", inline=False)
        await ctx.send(embed=embed)
    elif command_help == 'ban':
        embed=discord.Embed(title=f"ban help command", description=f"This will ban user", color=0x00f2ff)
        embed.add_field(name=f"Example", value=f"{prefix}ban @Example For example", inline=False)
        await ctx.send(embed=embed)
    elif command_help == 'unban':
        embed=discord.Embed(title=f"unban help command", description=f"This will unban user", color=0x00f2ff)
        embed.add_field(name=f"Example", value=f"{prefix}unban Example#1234", inline=False)
        await ctx.send(embed=embed)
    elif command_help == 'confess':
        embed=discord.Embed(title=f"confess help command", description=f"You can write anything then your message will be displayed as this bot and your original message will be deleted!", color=0x00f2ff)
        embed.add_field(name=f"Example", value=f"{prefix}confess example", inline=False)
        await ctx.send(embed=embed)
    elif command_help == 'clear':
        embed=discord.Embed(title=f"clear help command", description=f"This will clear the message in the channe", color=0x00f2ff)
        embed.add_field(name=f"Example", value=f"{prefix}clear 5", inline=False)
        embed.add_field(name=f"Aliases", value=f"`purge`", inline=False)
        await ctx.send(embed=embed)
    elif command_help == 'eval':
        await ctx.send(embed=discord.Embed(title=f"Owner command", description=f"This command is only for `owner`", color=0x00f2ff))
    elif command_help == 'slowmode':
        embed=discord.Embed(title=f"Slowmode help command", description=f"This slow down the chat!", color=0x00f2ff)
        embed.add_field(name=f"Example", value=f"{prefix}slowmode 5", inline=False)
        embed.add_field(name=f"Aliases", value=f"`sm`", inline=False)
        await ctx.send(embed=embed)
    else:
        await ctx.send(embed=discord.Embed(title=f"Command does not exist", description=f"Help for this command dosent exist, please check if the command is right or not.", color=0x00f2ff))

# Help command error
@help.error
async def help_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(title=f"Guild Prefix: `{prefix}`", color=0x00f2ff, description='**<:invite:822410792804417567> [ Invite](https://top.gg/bot/709984874924081174/)** | **<:support:822410788773691392> [ Support Server](https://discord.gg/XfngbaaG2r)** |  **<:sourecode:822410789122080768> [ Source Code](https://github.com/BIGBEASTISHANK/discord.py-sourcecode)** | **<:vote:826728613663342642> [ Vote](https://top.gg/bot/709984874924081174/vote)**', timestamp=datetime.utcnow())
        embed.set_author(name='BIG Beast Help', url='', icon_url="https://images.discordapp.net/avatars/709984874924081174/dcb255eea70abcc9d6014aac2564e7a0.png?size=128")
        embed.set_thumbnail(url="https://images.discordapp.net/avatars/709984874924081174/dcb255eea70abcc9d6014aac2564e7a0.png?size=128")
        embed.add_field(name='❯ General', value='`confess`', inline=False)
        embed.add_field(name='❯ Moderation', value='`kick` | `ban` | `unban` | `clear` | `slowmode`', inline=False)
        embed.add_field(name='❯ Utility', value='`ping`', inline=False)
        embed.set_footer(text=f"Help for specific command use {prefix}help [command]")
        await ctx.send(embed=embed)
        return

#########################################
# Ping command will show the ping of bot
#########################################
@client.command()
async def ping(ctx):
    await ctx.send(embed=discord.Embed(title=f"Ping", description=f"Latency: {round(client.latency * 1000)}ms", color=0x00f2ff))

##############
# Kick a user
##############
@commands.has_permissions(kick_members=True) #checking if a user has permissions
@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):

    await member.kick(reason=reason)
    await ctx.send(embed=discord.Embed(title="Kicked a user", description=f"{member.mention} has been kick for `{reason}`", color=0x00f2ff))

# Kick command error
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Please mention user to kick")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(f"Your dont have permission to kick, Nub")

#############
# Ban a user
#############
@client.command()
@commands.has_permissions(ban_members=True) #checking if a user has permissions
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(embed=discord.Embed(title="Banned a user", description=f"{member.mention} has been banned for `{reason}`", color=0x00f2ff))

#Ban command error
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Please mention user to ban")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(f"Your dont have permission to ban, Nub")

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

# Unban command error
@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Please mention user to unban")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(f"Your dont have permission to unban, Nub")

################
# Clear command
################
@commands.has_permissions(manage_messages=True)
@client.command(aliases=['purge'])
async def clear(ctx, amount:int):
    await ctx.channel.purge(limit=amount+1)

# Clear command error
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Please enter a number to clear")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(f"Your dont have permission to clear, Nub")

##################
# Confess command
##################
@client.command()
async def confess(ctx, *,word:str):
    await ctx.channel.purge(limit=1)
    await ctx.send(f"{word}")

# Confess command error
@confess.error
async def confess_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Please type something to confess")
        time.sleep(5)
        await ctx.channel.purge(limit=2)

####################
# Calcultor command
####################
@client.command(aliases=['calc'])
async def calculate(ctx, num1:int, opprator:str, num2:int):
    if opprator == "+":
        embed=discord.Embed(title="Calculator", color=0x00f2ff)
        embed.add_field(name="Question", value=f"```css\n{num1} {opprator} {num2}```", inline=False)
        embed.add_field(name="Answer", value=f"```css\n{num1 + num2}```", inline=False)
        await ctx.send(embed=embed)
    elif opprator == "-":
        embed=discord.Embed(title="Calculator", color=0x00f2ff)
        embed.add_field(name="Question", value=f"```css\n{num1} {opprator} {num2}```", inline=False)
        embed.add_field(name="Answer", value=f"```css\n{num1 - num2}```", inline=False)
        await ctx.send(embed=embed)
    elif opprator == "*":
        embed=discord.Embed(title="Calculator", color=0x00f2ff)
        embed.add_field(name="Question", value=f"```css\n{num1} {opprator} {num2}```", inline=False)
        embed.add_field(name="Answer", value=f"```css\n{num1 * num2}```", inline=False)
        await ctx.send(embed=embed)
    elif opprator == "/":
        embed=discord.Embed(title="Calculator", color=0x00f2ff)
        embed.add_field(name="Question", value=f"```css\n{num1} {opprator} {num2}```", inline=False)
        embed.add_field(name="Answer", value=f"```css\n{num1 / num2}```", inline=False)
        await ctx.send(embed=embed)
    else:
        await ctx.send(f"lease enter the valid opprator: + : - : * : /")

# Calculator error
@calculate.error
async def calculate_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed=discord.Embed(title="Opprator error", description=f"Please give opprator and number", color=0x00f2ff)
        embed.add_field(name=f"Example", value=f"{prefix}calculate 5 + 5")
        await ctx.send(embed=embed)
    elif isinstance(error, commands.BadArgument):
        embed=discord.Embed(title="Number error", description=f"Please give a valid number", color=0x00f2ff)
        embed.add_field(name=f"Example", value=f"{prefix}calculate 5 + 5")
        await ctx.send(embed=embed)

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

###################
# Slowmode command
###################
@client.command(aliases=['sm'])
@commands.has_permissions(manage_messages=True) #checking if a user has permissions
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"Set the slowmode delay in this channel to {seconds} seconds!")

# slowmode error
@slowmode.error
async def slowmode_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f"Please enter a number (seconds) to slow down the chat")
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(f"Your dont have permission to slow down chat, Nub")

################################
# Running the bot with commands
################################
client.run(token)
