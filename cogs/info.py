'''
MIT License
Copyright (c) 2017 Grok
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import discord
from discord.ext import commands
from urllib.parse import urlparse
# from ext import embedtobox
from PIL import Image
import datetime
import asyncio
import psutil
import random
import pip
import os
import io


class Information:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["ri","role"], no_pm=True)
    @commands.guild_only()
    async def roleinfo(self, ctx, *, role: discord.Role):
        '''Shows information about a role'''
        guild = ctx.guild

        since_created = (ctx.message.created_at - role.created_at).days
        role_created = role.created_at.strftime("%d %b %Y %H:%M")
        created_on = "{} ({} days ago!)".format(role_created, since_created)

        users = len([x for x in guild.members if role in x.roles])
        if str(role.colour) == "#000000":
            colour = "default"
            color = ("#%06x" % random.randint(0, 0xFFFFFF))
            color = int(colour[1:], 16)
        else:
            colour = str(role.colour).upper()
            color = role.colour

        em = discord.Embed(colour=color)
        em.set_author(name=role.name)
        em.add_field(name="Users", value=users)
        em.add_field(name="Mentionable", value=role.mentionable)
        em.add_field(name="Hoist", value=role.hoist)
        em.add_field(name="Position", value=role.position)
        em.add_field(name="Managed", value=role.managed)
        em.add_field(name="Colour", value=colour)
        em.add_field(name='Creation Date', value=created_on)
        em.set_footer(text=f'Role ID: {role.id}')

        await ctx.send(embed=em)

    @commands.command(aliases=['ui'], no_pm=True)
    async def userinfo(self, ctx, *, member : discord.Member=None):
        '''Get information about a member of a guild'''
        guild = ctx.guild or None
        user = member or ctx.message.author
        avi = user.avatar_url
        time = ctx.message.created_at
        desc = '{0} is chilling in {1} mode.'.format(user.name, user.status)
        em = discord.Embed(description=desc, timestamp=time)

        if guild:
            member_number = sorted(guild.members, key=lambda m: m.joined_at).index(user)+1
            roles = sorted(user.roles, key=lambda c: c.position)
            for role in roles:
                if str(role.color) != "#000000":
                    color = role.color
            rolenames = ', '.join([r.name for r in roles if r.name != "@everyone"]) or 'None'
            em.add_field(name='Nick', value=user.nick, inline=True)
            em.add_field(name='Member No.',value=str(member_number),inline = True)

        if 'color' not in locals():
            color = 0
        em.color = color
        em.add_field(name='Account Created', value=user.created_at.__format__('%A, %d. %B %Y'))

        if guild:
            em.add_field(name='Join Date', value=user.joined_at.__format__('%A, %d. %B %Y'))
            em.add_field(name='Roles', value=rolenames, inline=True)

        em.set_footer(text='User ID: '+str(user.id))
        em.set_thumbnail(url=avi)
        em.set_author(name=user, icon_url=guild.icon_url)

        await ctx.send(embed=em)


    @commands.command(aliases=['bot', 'info'])
    async def about(self, ctx):
        '''See information about the bot.'''

        embed = discord.Embed()
        embed.url = 'https://discord.gg/xAFbcWn'

        embed.set_author(name='Dark$oul Bot', icon_url=ctx.author.avatar_url)

        total_members = sum(1 for _ in self.bot.get_all_members())
        total_online = len({m.id for m in self.bot.get_all_members() if m.status is discord.Status.online})
        total_unique = len(self.bot.users)

        voice_channels = []
        text_channels = []
        for guild in self.bot.guilds:
            voice_channels.extend(guild.voice_channels)
            text_channels.extend(guild.text_channels)

        text = len(text_channels)
        voice = len(voice_channels)
        dm = len(self.bot.private_channels)



        github = '[Click Here](https://github.com/freetnt5852/darksoul-bot/)'
        server = '[Click Here](https://discord.gg/xAFbcWn)'


        embed.add_field(name='Author', value='Free TNT#5796')
        embed.add_field(name='Guilds', value=len(self.bot.guilds))
        embed.add_field(name='Members', value=f'{total_unique} total\n{total_online} online')
        embed.add_field(name='Channels', value=f'{text} text\n{voice} voice\n{dm} direct')
        embed.add_field(name='Github', value=github)
        embed.add_field(name='Discord', value=server)
        embed.add_field(name='Website', value=website)
        embed.set_footer(text=f'Powered by discord.py {discord.__version__}')
        await ctx.send(embed=embed)        

        


def setup(bot):
    return bot.add_cog(Information(bot))
