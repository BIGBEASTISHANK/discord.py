# Importing Libs
import discord
import os
from random import *
from datetime import datetime
from discord.ext import commands

# Defining variables
prefix = "'"
token = "NzkxNTg1NTM0NTk0MTIxNzU4.X-RTeg.a8gRZjlBA8qmp5i04XRxXjtDjIA"
status = discord.Status.dnd
activity = discord.Game("with discord servers 😈")
client = commands.Bot(command_prefix=commands.when_mentioned_or(prefix), help_command=None)

# File locations
event_path ="./events/"
command_path ="./commands/"
filelist = []