import discord,random,pickle
from discord.ext import commands
your_user_id=

class GuildHelp(commands.Cog):
  def __init__(self,client):
    self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('guild_leave.py is ready!')
    
    @commands.command()
    @commands.is_owner()
    async def Leave(self,ctx,*,guild_name):
        guild =  discord.utils.get(self.client.guilds,name=guild_name)
        
        if guild is None:
            await ctx.reply('No guild with that name!')
            return
        else:
            await ctx.reply(f'**I have left {guild_name}!**')
            await guild.leave()
            


    @Leave.error
    async def leave_error(self,ctx,error):
        if ctx.author.id != your_user_id:
            await ctx.reply(f'**Error: Your are forbiddened from using this command!! __only the owner of this bot can use it__**')

async def setup(client):
    await client.add_cog(GuildHelp(client)) 