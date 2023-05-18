import discord
from discord.ext import commands

your_user_id=

class Get_Client_Guilds(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.tree.sync()
        print('Get_Client_Guilds.py is ready!\n========(Cmd logging starts form here)========')
    
    @commands.command()
    @commands.is_owner()
    async def Get_Client_Guilds(self,ctx):
        await ctx.reply('This may take some time!')
        guilds=[]
        guilds = [guild async for guild in self.client.fetch_guilds(limit=150)]
        return_list=[]
        for x in guilds:
            return_list.append(f'{x}')
        await ctx.reply(f'the guilds are: {return_list}')


    @Get_Client_Guilds.error
    async def Get_Client_Guilds_Error(self,ctx,error):
        if ctx.author.id != your_user_id:
            await ctx.reply(f'**Error: Your are forbiddened from using this command!!** \n __only the owner of this bot can use it__ ')
            
async def setup(client):
    await client.add_cog(Get_Client_Guilds(client))