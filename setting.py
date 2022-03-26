# Importing Libs
import discord
import os
from dotenv import load_dotenv
from random import *
from datetime import datetime
from discord.ext import commands

# Defining variables
prefix = os.getenv("PREFIX")
token = os.getenv("TOKEN")
status = discord.Status.dnd
activity = discord.Game("with discord servers 😈")
client = commands.Bot(command_prefix=commands.when_mentioned_or(prefix), help_command=None)

# File locations
event_path ="./events/"
command_path ="./commands/"
filelist = []