# Importing Libsimport discord
import os
import discord
from random import *
from dotenv import load_dotenv
from datetime import datetime
from discord.ext import commands

# Inalizing
load_dotenv()

# Defining variables
prefix = os.getenv("PREFIX")
token = os.getenv("TOKEN")

status = discord.Status.dnd
activity = discord.Game("with discord servers 😈")

client = commands.Bot(
    command_prefix=commands.when_mentioned_or(prefix), help_command=None)

# File locations
event_path = "./events/"
command_path = "./commands/"
filelist = []
