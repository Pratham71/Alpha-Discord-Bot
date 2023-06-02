import discord
import time
import platform
import colorama
import asyncio
import os
"___________________________________"
from colorama import Back,Fore,Style
from discord.ext import commands,tasks
from itertools import cycle

c_prefix='.$'
TOKEN=''
client = commands.Bot(command_prefix=f'{c_prefix}',intents=discord.Intents.all())
client.remove_command("help")
bot_status = cycle([f'{c_prefix}help','Goenka Tech Fest','discord.py'])

@client.event
async def on_ready():
    prfx = (Back.BLACK + Fore.GREEN+time.strftime("%H:%M:%S UTC",time.gmtime())+Back.RESET+Fore.WHITE+Style.BRIGHT)
    print(prfx+" logged in as:"+Fore.CYAN+str(client.user))
    print(prfx+" BOT ID:"+Fore.CYAN+str(client.user.id))
    print(prfx+f" On Servers:"+Fore.CYAN+str(len(client.guilds)))
    print(prfx+" Discord.py version:"+Fore.CYAN+discord.__version__)
    print(prfx+" Python version:"+Fore.CYAN+str(platform.python_version()))
    print(prfx+" Client Ready:"+Fore.CYAN+str(client.is_ready()))
    print(prfx+' Cogs loading ↓'+Fore.WHITE)
    change_status.start()

@tasks.loop(seconds=15)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))

async def load():
    for filename in os.listdir("cogs_folder_path"):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')

async def main():
    async with client:
        await load()
        await client.start(TOKEN)

asyncio.run(main())
