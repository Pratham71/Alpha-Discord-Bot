import discord 
from discord import app_commands
from discord.ext import commands

class EMBEDED(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('embed.py is ready!')
    
    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions(administrator=True)
    async def embed(self,ctx):
       
        embed_message = discord.Embed(title="*Rules!*",description=f'{text}',color=discord.Color.random())

        embed_message.set_author(name=f'Goenka Tech Fest',icon_url=ctx.guild.icon)
        embed_message.set_thumbnail(url=ctx.guild.icon)
        embed_message.set_image(url='https://cdn.discordapp.com/attachments/882474968934412328/1101500661339795566/rules.png')
        embed_message.set_footer(text='GDGPS',icon_url=ctx.guild.icon)

        await ctx.send(embed = embed_message)

async def setup(client):
    await client.add_cog(EMBEDED(client))



text='''**Welcome!**
**Hey!** 

**Rules!**
1. **Follow Discord's TOS**
https://discordapp.com/terms
https://discordapp.com/guidelines

2. **Be respectful with all members**
Be respectful to others, hate speech, racism.

3.**No Advertising**
Includes DM Advertising. We do not allow advertising here of any kind.

4.**Eplicit Content and Misbehaviour**
```Explicit content and behavior by any participant is not condoned and will be investigated promptly. You can share screenshots of such explicit behavior that you encounter in the server to the President or Vice President.```

5.**No spamming in text or VC**
Do not spam messages, soundboards, voice changers.

6.**Do not discuss about sensitive topics**
This isn't a debating server, keep sensitive topics out of here.

7.**No malicious content**
No grabify links, viruses, crash videos, links to viruses, or token grabbers. These will result in an automated ban.

8.**No Self Bots**
Includes all kinds of selfbots: Nitro snipers, selfbots like nighty, auto changing statuses

9.**Do not DM the staff team**
Please open a ticket instead in <#1102451070086676533>

10.**Profile Picture / Banner Rules**
```No NSFW allowed
No racism
No brightly flashing pictures to induce an epileptic attack```


11.**Emoji Rules**
```No NSFW allowed
No racism
No brightly flashing pictures to induce an epileptic attack.```


12.**Any sort of Cheating and use of unfair means would not be tolerated and the participant(s) found guilty will be disqualified.**

13.**It is mandatory to introduce yourself in <#1101492287772577792> in the format mentioned in the pinned comment.**

14.**Defamation of any individual or organization is strictly prohibited.**
'''