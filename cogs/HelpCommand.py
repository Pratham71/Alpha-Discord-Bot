import discord 
from discord.ext import commands
command_prefix = '.$'

class HelpCommand(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('HelpCommand.py is ready!')
        
    
    @commands.command()
    async def help(self,ctx):

        help_embed =  discord.Embed(title=f'Help desk for {self.client.user}',description='All commands for the bot.',color=discord.Color.random())

        help_embed.set_author(name='Goenka Tech Fest')
        help_embed.add_field(name=f'**{command_prefix}Leave sever_name:**',value='Leaves the server as per the name entered (user carefully,only for the bot owner)!',inline=False)
        help_embed.add_field(name=f'**{command_prefix}clear msg_count:**',value='Deletes a specified amount of messages.',inline=False)
        help_embed.add_field(name=f'**{command_prefix}kick id/@ reason=(if any):**',value='Kicks a user from guild/server.',inline=False)
        help_embed.add_field(name=f'**{command_prefix}ban id/@ reason=(if any):**',value='Bans a user from guild/server.',inline=False)
        help_embed.add_field(name=f'**{command_prefix}unban id/@ reason=(if any):**',value='Unbans a user from guild/sever.',inline=False)
        help_embed.add_field(name=f'**{command_prefix}timeout id/@ duration(in minutes) reason=(if any):**',value=f'Times Out a user from guild/server.',inline=False)
        help_embed.add_field(name=f'**{command_prefix}timedout id/@:**',value=f'Checks if the user is timed or not (returns True if the user is timedout otherwise False).',inline=False)
        help_embed.add_field(name=f'**{command_prefix}UserInfo id/@:**',value='returns the information of a user wiht user ID (if left none returns the command author info.).',inline=False)
        help_embed.add_field(name=f'**{command_prefix}kill:**',value='Ends the loop cycle of the bot (only for the bot owner).',inline=False)
        help_embed.add_field(name=f'**{command_prefix}time:**',value=f'returns the uptime of {self.client.user}.',inline=False)
        help_embed.add_field(name='**Auto Logging**',value='setup a channel named log-channel for auto logging to work!',inline=False)
        help_embed.add_field(name='**embed:**',value='to be updated.',inline=False)
        help_embed.add_field(name='**Do\'nt Dm the bot**',value='**you will be disapointed!**',inline=False)
        await ctx.send('Check your direct messages for a list of commands!')
        await ctx.author.send(embed=help_embed)
        print(f'{ctx.author} used help in {ctx.channel.name,ctx.channel.id,ctx.guild.name,ctx.guild.id}')


async def setup(client):
    await client.add_cog(HelpCommand(client))
