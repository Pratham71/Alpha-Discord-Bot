import discord 
from discord import app_commands
from discord.ext import commands
import sys

class KILL(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('kill.py is ready!')
    
    @commands.command()
    @commands.is_owner()
    async def kill(self,ctx):
        response = '```The bot processes have been killed```'
        await ctx.reply(response)
        print(f'{ctx.author} used kill in {ctx.channel.name,ctx.channel.id,ctx.guild.name,ctx.guild.id}')
        print('=================\nBot loop cycle has ended')
        await self.client.close()

    @kill.error
    async def kill_error(self,ctx,error):
        if ctx.author.id != 397679536818487296:
            await ctx.reply(f'**Error: Your are forbiddened from using this command!!** \n __only the owner of this bot can use it__ ')
        
async def setup(client):
    await client.add_cog(KILL(client))