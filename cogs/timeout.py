import discord,datetime
from discord.ext import commands

t_error='moderate members'

class TimeOut(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('timeout.py is ready!')
    
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(moderate_members=True)
    @commands.bot_has_permissions(moderate_members=True)
    async def timeout(self,ctx,member:discord.Member,minutes: int=0,reason=None):
        if ctx.author.id == member.id :
            await ctx.reply('**You cannot timeout yourself!**')
        
        duration =  datetime.timedelta(minutes=minutes)
        timeout_embed = discord.Embed(title='**User Timedout!**',color=discord.Color.gold())
        timeout_embed.add_field(name='**Name of the member:**',value=f'{member.mention}',inline=False)
        timeout_embed.add_field(name='**User ID of the member:**',value=f'{member.id}',inline=False)
        timeout_embed.add_field(name='**Duration of the timeout:**',value=f'**{duration}**',inline=False)
        timeout_embed.add_field(name='**Reason of the member:**',value=f'{reason}',inline=False)
        timeout_embed.set_footer(text=f'{ctx.author.mention}')
        
        await member.timeout(duration)
        await ctx.reply(embed=timeout_embed)
        print(f'{ctx.author,ctx.auhtor.id} used timeout in {ctx.channel.name,ctx.channel.id,ctx.guild.name,ctx.guild.id}')

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(moderate_members=True)
    @commands.bot_has_permissions(moderate_members=True)
    async def timedout(self,ctx,member:discord.Member=None):
        print(f'{ctx.author} used timedout in {ctx.channel.name,ctx.channel.id,ctx.guild.name,ctx.guild.id}')

        if member is None:
            member=ctx.author
        elif member is not None:
            member=member
        
        if member.is_timed_out() ==  True:
            await ctx.reply(f'***{member.mention} is timedout __{member.is_timed_out()}__ until __{member.timed_out_until.time()}__***')
        else:
            await ctx.reply(f'***{member.mention} is timedout __{member.is_timed_out()}__***')

    @timeout.error
    async def timeout_error(self,ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.reply(f"Error: Missing Required Arguments!, You must pass a userID or '@' mention to run kick command")
        elif isinstance(error,commands.MissingPermissions):
            await ctx.reply(f"Error: Missing Required Permissions, You must have the required permission(s) assigned to your role(s) \n{t_error}")
        elif isinstance(error,commands.BotMissingPermissions):
            await ctx.reply(f"Error: Missing Required Permissions, You must have the required permission(s) assigned to your role(s) \n{t_error}")

            

async def setup(client):
    await client.add_cog(TimeOut(client))
