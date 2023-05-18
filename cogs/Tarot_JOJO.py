import discord,random,pickle
from discord.ext import commands
from discord import app_commands

class TarotCog(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Tarot_JOJO.py is ready!')
    
    @app_commands.command(name='tarot_card',description='Sends a tarot card from JOJO\'s Bizzare Adventure.')
    @app_commands.guild_only()
    async def tarot_card(self,interaction:discord.Interaction):
        file_name='tarot_card'
        f=open(f"{file_name}.dat",'rb')
        tarot_dict=pickle.load(f)
        tarot_random=random.choice(tarot_dict)
        f.close()

        tarot_embed = discord.Embed(title='**Your Tarot Card!**',color=discord.Color.random())
        tarot_embed.set_image(url=f'{tarot_random}')
        tarot_embed.set_footer(text='The above images have been taken from https://jojowiki.com/JoJo_Wiki')

        await interaction.response.send_message(embed=tarot_embed)

async def setup(client):
    await client.add_cog(TarotCog(client))   
