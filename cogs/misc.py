import asyncio
import aiohttp
import random as rng
import discord
from discord.ext import commands


class Misc:
    """Misc commands"""

    def __init__(self,bot):
        self.bot = bot
        #self.loop = asyncio.AbstractEventLoop.run_until_complete(future)
        self.session = aiohttp.ClientSession()
    @commands.command()
    async def urban(self, ctx, *, search_terms : str):
        '''Searches Up a Term in Urban Dictionary'''
        search_terms = search_terms.split()
        definition_number = terms = None
        try:
            definition_number = int(search_terms[-1]) - 1
            search_terms.remove(search_terms[-1])
        except ValueError:
            definition_number = 0
        if definition_number not in range(0, 11):
            pos = 0
        search_terms = "+".join(search_terms)
        url = "http://api.urbandictionary.com/v0/define?term=" + search_terms
        async with self.session.get(url) as r:
            result = await r.json()
        emb = discord.Embed()
        emb.color = discord.Colour(value=0xBADA55)
        if result.get('list'):
            definition = result['list'][definition_number]['definition']
            example = result['list'][definition_number]['example']
            defs = len(result['list'])
            search_terms = search_terms.split("+")
            emb.title = "{}  ({}/{})".format(" ".join(search_terms), definition_number+1, defs)
            emb.description = definition
            emb.add_field(name='Example', value=example)
        else:
            emb.title = "Search term not found."
        await ctx.send(embed=emb)

    @commands.command()
    async def choose(self, ctx, *choices: commands.clean_content):
        """Chooses between multiple choices.
        To denote multiple choices, you should use double quotes.
        """
        if len(choices) < 2:
            return await ctx.send('Not enough choices to pick from.')

        await ctx.send(rng.choice(choices))

def setup(bot):
	bot.add_cog(Misc(bot))
