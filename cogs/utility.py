import discord
import wikipedia
import textwrap
import asyncio
import psutil
import random
import os
import io
from discord.ext import commands

'''This is a sample cog (class) file'''


class Utility:  # Replace "Sample" with the name of the module here and at bottom as well

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['wikipedia'], pass_context=True)
    async def wiki(self, ctx, *, search: str = None):
        '''Addictive Wikipedia results
        Input a word or a combination of words
        to get proper result. Courtesy of xaos'''
        if search == None:
            await ctx.channel.send(f'Usage: `{ctx.prefix}wiki [search terms]`')
            return

        results = wikipedia.search(search)
        if not len(results):
            no_results = await ctx.channel.send("Sorry, didn't find any result.")
            await asyncio.sleep(5)
            await ctx.message.delete(no_results)
            return

        newSearch = results[0]
        try:
            wik = wikipedia.page(newSearch)
        except wikipedia.DisambiguationError:
            more_details = await ctx.channel.send('Please input more details.')
            await asyncio.sleep(5)
            await ctx.message.delete(more_details)
            return

        emb = discord.Embed()
        emb.title = wik.title
        emb.url = wik.url
        textList = textwrap.wrap(wik.content, 500, break_long_words=True, replace_whitespace=False)
        emb.add_field(name="Wikipedia Results", value=textList[0] + "...")
        await ctx.send(embed=emb)

    @commands.command(aliases=['av'])
    async def avatar(self, ctx, *, member: discord.Member = None):
        '''Returns someone's avatar url
        courtesy of verixx'''
        member = member or ctx.author
        av = member.avatar_url
        if ".gif" in av:
            av += "&f=.gif"
        em = discord.Embed(url=av)
        em.set_author(name=str(member), icon_url=av)
        em.set_image(url=av)
        await ctx.send(embed=em)

    @commands.command(pass_context=True)
    async def another(self, ctx):  # Replace "another" with the command name
        """Put the help message for "another" command here"""
        # Code starts on this line, indented 8 spaces.
        pass


def setup(bot):
    bot.add_cog(Utility(bot))
