from pydoc import describe
from setting import *

###############
# Help command
###############


@client.command(aliases=['h'])
async def help(ctx, command_help: str):

    # Ping
    if command_help == 'ping':
        embed = discord.Embed(title=f"Ping help command",
                              description=f"This will tell you the ping of bot!", color=0x00f2ff)
        await ctx.send(embed=embed)

    # Kick
    elif command_help == 'kick':
        embed = discord.Embed(title=f"kick help command",
                              description=f"This will kick user", color=0x00f2ff)
        embed.add_field(
            name=f"Example", value=f"{prefix}kick @Example For example", inline=False)
        await ctx.send(embed=embed)

    # Ban
    elif command_help == 'ban':
        embed = discord.Embed(title=f"Ban help command",
                              description=f"This will ban user", color=0x00f2ff)
        embed.add_field(
            name=f"Example", value=f"{prefix}ban @Example For example", inline=False)
        await ctx.send(embed=embed)

    # Unban
    elif command_help == 'unban':
        embed = discord.Embed(title=f"Unban help command",
                              description=f"This will unban user", color=0x00f2ff)
        embed.add_field(name=f"Example",
                        value=f"{prefix}unban Example#1234", inline=False)
        await ctx.send(embed=embed)

    # Confess
    elif command_help == 'confess':
        embed = discord.Embed(title=f"Confess help command",
                              description=f"You can write anything then your message will be displayed as this bot and your original message will be deleted!", color=0x00f2ff)
        embed.add_field(name=f"Example",
                        value=f"{prefix}confess example", inline=False)
        await ctx.send(embed=embed)

    # Clear
    elif command_help == 'clear':
        embed = discord.Embed(title=f"Clear help command",
                              description=f"This will clear the message in the channe", color=0x00f2ff)
        embed.add_field(name=f"Example",
                        value=f"{prefix}clear 5", inline=False)
        embed.add_field(name=f"Aliases", value=f"`purge`", inline=False)
        await ctx.send(embed=embed)

    # PP
    elif command_help == 'pp':
        await ctx.send(embed=discord.Embed(title=f"PP command",
                                           description=f"This will tell you your (or the person you mention) pp size", color=0x00f2ff))

    # Slowmode
    elif command_help == 'slowmode':
        embed = discord.Embed(title=f"Slowmode help command",
                              description=f"This slow down the chat!", color=0x00f2ff)
        embed.add_field(name=f"Example",
                        value=f"{prefix}slowmode 5", inline=False)
        embed.add_field(name=f"Aliases", value=f"`sm`", inline=False)
        await ctx.send(embed=embed)

    # Calculate
    elif command_help == 'calculate':
        embed = discord.Embed(title=f"Calculate help command",
                              description=f"This slow down the chat!", color=0x00f2ff)
        embed.add_field(name=f"Example",
                        value=f"{prefix}calc 5 + 5", inline=False)
        embed.add_field(name=f"Aliases", value=f"`calc`", inline=False)
        await ctx.send(embed=embed)

    # Info
    elif command_help == "info":
        embed = discord.Embed(title=f"Info help command",
                              description=f"This shows the server info!", color=0x00f2ff)
        await ctx.send(embed=embed)

    # None
    else:
        embed = discord.Embed(title=f"Command does not exist",
                              description=f"Help for this command dosent exist, please check if the command is right or not.", color=0x00f2ff)
        await ctx.send(embed=embed)

#####################
# Help command error
#####################


@help.error
async def help_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):

        # Variable
        description = '**<:invite:822410792804417567> [ Invite](https://top.gg/bot/709984874924081174/)** | **<:support:822410788773691392> [ Support Server](https://discord.gg/XfngbaaG2r)** |  **<:sourecode:822410789122080768> [ Source Code](https://github.com/BIGBEASTISHANK/discord.py-sourcecode)** | **<:vote:826728613663342642> [ Vote](https://top.gg/bot/709984874924081174/vote)**'

        # Header
        embed = discord.Embed(
            title=f"Guild Prefix: `{prefix}`", color=0x00f2ff, description=description, timestamp=datetime.utcnow())
        embed.set_author(name='BIG Beast Help', url='',
                         icon_url="https://images.discordapp.net/avatars/709984874924081174/dcb255eea70abcc9d6014aac2564e7a0.png?size=128")
        embed.set_thumbnail(
            url="https://images.discordapp.net/avatars/709984874924081174/dcb255eea70abcc9d6014aac2564e7a0.png?size=128")

        # Commands
        embed.add_field(name='❯ General',
                        value='`confess`', inline=False)
        embed.add_field(
            name='❯ Moderation', value='`kick` | `ban` | `unban` | `clear` | `slowmode`', inline=False)
        embed.add_field(name='❯ Fun', value='`pp` | `calculate`', inline=False)
        embed.add_field(name='❯ Utility', value='`ping` | `info`', inline=False)

        # Footer
        embed.set_footer(
            text=f"Help for specific command use {prefix}help [command]")

        await ctx.send(embed=embed)
        return
