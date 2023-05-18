import discord 
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Events.py is ready!')
    
    @commands.Cog.listener()
    async def on_guild_join(self,guild):
        check_channel = discord.utils.get(guild.channels,name='log-channel')
        if check_channel is None:
            channel = await guild.create_text_channel('log-channel')
            await channel.send('```This Channel has been set for Auto Logging.```')
            await channel.send('```Use .$Setup```')
            print('Channel Created!')
        else:
            print('Channel Already Exists!')
            return

        guilds=[]
        guilds = [guild async for guild in self.client.fetch_guilds(limit=150,)]
        z=guilds
        file_name='Guilds_list'
        with open(f'{file_name}.txt','a') as f:
            f.write(f'{z}\n')
        
        print(f'{guild.name} joined!')
        print(f'{file_name} updated!')

    

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        
        log_channel = discord.utils.get(message.guild.channels, name='log-channel')

        
        event_embed = discord.Embed(title='Message Logged',description='Message\'s content and origin',color=discord.Color.dark_blue())
        event_embed.add_field(name='Message Author:',value=message.author.mention,inline=False)
        event_embed.add_field(name='Channel Origin:',value=message.channel.mention,inline=False)
        event_embed.add_field(name='Message Content:',value=message.content,inline=False)

        await log_channel.send(embed=event_embed)
    
    @commands.Cog.listener()
    async def on_message_delete(self, messages):
        log_channel = discord.utils.get(messages.guild.channels, name='log-channel')

        event_embed = discord.Embed(title='**Message Deleted**',color=discord.Color.green())
        event_embed.add_field(name='Channel:',value=messages.channel.mention,inline=False)

        await log_channel.send(embed=event_embed)

    @commands.Cog.listener()
    async def on_member_join(self, member):
        log_channel = discord.utils.get(member.guilds.channels,name='log-channel')

        event_embed =  discord.Embed(title='Arrival Logged',description='**This user landed in the server!**',color=discord.Color.dark_purple())
        event_embed.add_field(name='User Joined:',value=member.mention,inline=False)
        await log_channel.send(embed=event_embed)
    
    @commands.Cog.listener()
    async def on_member_remove(self,member):
        log_channel =  discord.utils.get(member.guild.channels,name='log-channel')

        event_embed = discord.Embed(title='Departure Logged',description='**This user has left the server!**',color=discord.Color.brand_red())
        event_embed.add_field(name='User Left:',value=member.mention,inline=False)
        await log_channel.send(embed=event_embed)
    
    @commands.Cog.listener()
    async def on_guild_channel_create(self,channel):
        log_channel =  discord.utils.get(channel.guild.channels,name='log-channel')

        event_embed = discord.Embed(title='New Channel Created!',color=discord.Color.random())
        event_embed.add_field(name='**Channel Name:**',value=f'<#{channel.id}>',inline=False)
        event_embed.add_field(name='**Channel ID:**',value=channel.id,inline=False)
        await log_channel.send(embed=event_embed)

    @commands.Cog.listener()
    async def on_guild_channel_delete(self,channel):
        log_channel = discord.utils.get(channel.guild.channels,name='log-channel')

        event_embed = discord.Embed(title='Channel Deleted!',color=discord.Color.dark_red())
        event_embed.add_field(name='**Channel Name**',value=f'{channel}',inline=False)
        event_embed.add_field(name='**Channel ID**',value=channel.id,inline=False)
        await log_channel.send(embed=event_embed)
    
    @commands.Cog.listener()
    async def on_guild_role_create(self,role):
        log_channel = discord.utils.get(role.guild.channels,name='log-channel')

        event_embed= discord.Embed(title='New Role Created!',color=discord.Color.yellow())
        event_embed.add_field(name='**Role Name:**',value=f'@{role}',inline=False)
        event_embed.add_field(name='**Role ID:**',value=f'{role.id}',inline=False)
        await log_channel.send(embed=event_embed)
    
async def setup(client):
    await client.add_cog(Events(client))
