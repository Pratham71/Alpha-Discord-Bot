import discord,random
from discord import app_commands
from discord.ext import commands

class AppCommands(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.tree.sync()
        print('AppCommands.py is ready!')
    
    @app_commands.command(name='avatar',description='Sends the user\'s avatar in a embed (sends own if user is left none)')
    @app_commands.guild_only()
    async def avatar(self,interaction:discord.Interaction,member:discord.Member=None):
        if member is None:
            member = interaction.user
        elif member is not None:
            member = member
        
        avatar_embed = discord.Embed(title=f'{member.name}\'s Avatar',color=discord.Color.random())

        avatar_embed.set_image(url=member.avatar)
        avatar_embed.set_footer(text=f'Requested by {interaction.user.name}',icon_url=interaction.user.avatar)

        await interaction.response.send_message(embed=avatar_embed)

    @app_commands.command(name='ping',description='replies with pong!')
    @app_commands.guild_only()
    async def ping(self,interaction:discord.Interaction):
        bot_latency = round(self.client.latency * 1000)
        await interaction.response.send_message(f'Pong! {bot_latency}ms.')
    
    @app_commands.command(name='userinfo',description='Sends the user\'s information in a embed (sends own if user if left none!)')
    @app_commands.guild_only()
    async def userinfo(self,interaction:discord.Interaction,member: discord.Member=None,):
        if member is None:
            member = interaction.user
        elif member is not None:
            member=member
        
        info_embed=discord.Embed(title=f'{member.name}\'s User Info',description=f'All of information about {member.name}',color=discord.Color.random())
        info_embed.set_thumbnail(url=member.avatar)
        info_embed.add_field(name='Name:',value=member.name,inline=False)
        info_embed.add_field(name='Nick Name:',value=member.display_name,inline=False)
        info_embed.add_field(name='Disciminator:',value=member.discriminator,inline=False)
        info_embed.add_field(name='Top role:',value=member.top_role,inline=False)
        info_embed.add_field(name='Bot user:',value=member.bot,inline=False)
        info_embed.add_field(name='Timed Out?:',value=member.is_timed_out(),inline=False)
        info_embed.add_field(name='Creation Date:',value=member.created_at.__format__('%A,%d. %B %Y @ %H:%M:%S'),inline=False)

        await interaction.response.send_message(embed=info_embed)

    @app_commands.command(name='random_number_generator',description='Generates a Random number b/w 0 and 1000')
    @app_commands.guild_only()
    async def RNG(self,interaction:discord.Interaction):
        start,end=0,1000
        result = random.randint(start,end)
        response=f'The random number from {start} to {end} is {result}'
        await interaction.response.send_message(f'{response}')
    
    @app_commands.command(name='rock_paper_scissors',description='...')
    @app_commands.guild_only()
    async def RPS(self,interaction:discord.Interaction):
        rps_list=['rock :rock:','paper :roll_of_paper:','scissors :scissors:']
        result = random.choice(rps_list)
        await interaction.response.send_message(f'The result is: {result}')
    
    @app_commands.command(name='flip_a_coin',description='Sends the user\'s information in a embed (sends own if user if left none!)')
    @app_commands.guild_only()
    async def flip_a_coin(self,interaction:discord.Interaction):
        flip=['heads','tails']
        result = random.choice(flip)
        await interaction.response.send_message(f'It\'s {result}!')
    

async def setup(client):
    await client.add_cog(AppCommands(client))
