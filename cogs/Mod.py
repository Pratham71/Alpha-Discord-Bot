import discord 
from discord.ext import commands
c_error='Manage Messages'
K_error='Kick Members'
b_error='Ban/Unban Members'

class Mods(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('Mods.py is ready!')
    
    @commands.command()
    @commands.guild_only()
    @commands.is_owner()
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    async def clear(self,ctx,msgcount:int):
        await ctx.channel.purge(limit=msgcount)
        await ctx.send(f'{msgcount} message(s) have been cleaned!')
        print(f'{ctx.author} used clear in {ctx.channel.name,ctx.channel.id,ctx.guild.name,ctx.guild.id}')

    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    @commands.bot_has_permissions(kick_members=True)
    async def kick(self,ctx,member:discord.Member,*,modreason=None):
        if ctx.author.id == member.id:
            await ctx.reply(f'**You cannot kick your self!**')
        
        conf_embed = discord.Embed(title='Success!',color=discord.Color.green())
        conf_embed.add_field(name='Kicked:',value=f'{member.mention} has been kicked from the server by {ctx.author.mention}',inline=False)
        conf_embed.add_field(name='Reason:',value=modreason,inline=False)

        print(f'{ctx.author} used kick in {ctx.channel.name,ctx.channel.id,ctx.guild.name,ctx.guild.id}')
        await ctx.send(embed=conf_embed)
        await ctx.guild.kick(member)


    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def ban(self,ctx,member:discord.Member,*,modreason=None):
        if ctx.author.id == member.id:
            await ctx.reply(f'**You cannot ban your self!**')

        conf_embed = discord.Embed(title='Success!',color=discord.Color.green())
        conf_embed.add_field(name='Banned:',value=f'{member.mention} has been banned from the server by {ctx.author.mention}',inline=False)
        conf_embed.add_field(name='Reason:',value=modreason,inline=False)

        print(f'{ctx.author} used ban in {ctx.channel.name,ctx.channel.id,ctx.guild.name,ctx.guild.id}')
        await ctx.send(embed=conf_embed)
        await ctx.guild.ban(member)


    @commands.command(name='unban')
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    @commands.bot_has_permissions(ban_members=True)
    async def unban(self,ctx,userId):
        user = discord.Object(id=userId)
        if ctx.author.id == userId:
            await ctx.reply(f'**Bruh**')

        conf_embed = discord.Embed(title='Success!',color=discord.Color.green())
        conf_embed.add_field(name='UNBanned:',value=f'<@{userId}> has been unbanned from the server by {ctx.author.mention}',inline=False)

        print(f'{ctx.author} used unban in {ctx.channel.name,ctx.channel.id,ctx.guild.name,ctx.guild.id}')
        await ctx.send(embed=conf_embed)
        await ctx.guild.unban(user)

    
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def UserInfo(self,ctx,member: discord.Member=None):
        if member is None:
            member = ctx.author
        elif member is not None:
            member=member
        
        info_embed=discord.Embed(title=f'{member.name}\'s User Info',description=f'All of information about {member.name}',color=discord.Color.random())
        info_embed.set_thumbnail(url=member.avatar)
        info_embed.add_field(name='Name:',value=member.name,inline=False)
        info_embed.add_field(name='Nick Name:',value=member.display_name,inline=False)
        info_embed.add_field(name='Disciminator:',value=member.discriminator,inline=False)
        info_embed.add_field(name='ID:',value=member.id,inline=False)
        info_embed.add_field(name='Top role:',value=member.top_role,inline=False)
        info_embed.add_field(name='Bot user:',value=member.bot,inline=False)
        info_embed.add_field(name='Timed Out?:',value=member.is_timed_out(),inline=False)
        info_embed.add_field(name='Joined this server at:',value=member.joined_at.date(),inline=False)
        info_embed.add_field(name='Creation Date:',value=member.created_at.__format__('%A,%d. %B %Y @ %H:%M:%S'),inline=False)

        print(f'{ctx.author} used UserInfo in {ctx.channel.name,ctx.channel.id,ctx.guild.name,ctx.guild.id}')
        await ctx.send(embed=info_embed)

    
    'ERROR HANDLING'
    @clear.error
    async def clear_error(self,ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.reply(f"Error: Missing Required Arguments!, You must pass a whole number!")
        elif isinstance(error,commands.MissingPermissions):
            await ctx.reply(f"Error: Missing Required Permissions, You must have the required permission(s) assigned to your role(s) \n{c_error}")
        elif isinstance(error,commands.BotMissingPermissions):
            await ctx.reply(f'Error: Bot Missing Required Permissions, The bot must have the required permission(s) assigend to its role(s) \n{c_error}')
    @ban.error
    async def ban_error(self,ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.reply(f"Error: Missing Required Arguments!, You must pass a userID or '@' mention to run ban command")
        elif isinstance(error,commands.MissingPermissions):
            await ctx.reply(f"Error: Missing Required Permissions, You must have the required permission(s) assigned to your role(s) \n{b_error}")
        elif isinstance(error,commands.BotMissingPermissions):
            await ctx.reply(f'Error: Bot Missing Required Permissions, The bot must have the required permission(s) assigend to its role(s) \n{b_error}')

    @unban.error
    async def unban_error(self,ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.reply(f"Error: Missing Required Arguments!, You must pass a userID to run unban command")
        elif isinstance(error,commands.MissingPermissions):
            await ctx.reply(f"Error: Missing Required Permissions, You must have the required permission(s) assigned to your role(s) \n{b_error}")
        elif isinstance(error,commands.BotMissingPermissions):
            await ctx.reply(f'Error: Bot Missing Required Permissions, The bot must have the required permission(s) assigend to its role(s) \n{b_error}')
    
    @kick.error
    async def kick_error(self,ctx,error):
        if isinstance(error,commands.MissingRequiredArgument):
            await ctx.reply(f"Error: Missing Required Arguments!, You must pass a userID or '@' mention to run kick command")
        elif isinstance(error,commands.MissingPermissions):
            await ctx.reply(f"Error: Missing Required Permissions, You must have the required permission(s) assigned to your role(s) \n{K_error}")
        elif isinstance(error,commands.BotMissingPermissions):
            await ctx.reply(f'Error: Bot Missing Required Permissions, The bot must have the required permission(s) assigend to its role(s) \n{K_error}')

async def setup(client):
    await client.add_cog(Mods(client))
