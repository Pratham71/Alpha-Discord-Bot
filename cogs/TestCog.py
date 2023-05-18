import discord,random,pickle
from discord.ext import commands

class TestCogs(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('TestCog.py is ready!')
    
    @commands.command()
    @commands.guild_only()
    async def tarot(self,ctx):
        file_name='tarot_card'
        f=open(f"{file_name}.dat",'rb')
        tarot_dict=pickle.load(f)
        tarot_random=random.choice(tarot_dict)
        f.close()

        tarot_embed = discord.Embed(title='**Your Tarot Card!**',color=discord.Color.random())
        tarot_embed.set_image(url=f'{tarot_random}')

        await ctx.reply(embed=tarot_embed)

async def setup(client):
    await client.add_cog(TestCogs(client))

