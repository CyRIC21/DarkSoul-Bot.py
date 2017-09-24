import discord
import os
import traceback
import textwrap
import io
from discord.ext import commands
from contextlib import redirect_stdout
bot = commands.Bot(command_prefix='?',description="DarkSoul-Bot\nOwner: Free TNT#5796\n\nHelp Commands",owner_id=292690616285134850)
bot.load_extension("cogs.utility")
bot.load_extension("cogs.misc")
bot.load_extension("cogs.mod")


def cleanup_code(content):
    """Automatically removes code blocks from the code."""
    # remove ```py\n```
    if content.startswith('```') and content.endswith('```'):
        return '\n'.join(content.split('\n')[1:-1])

    return content.strip('` \n')

@bot.event
async def on_ready():
  print('Bot is online!')
  
@bot.command(name='presence')
@commands.is_owner()
async def _set(ctx, Type=None,*,thing=None):
  """Change the bot's discord game/stream!"""
  if Type is None:
    await ctx.send('Usage: `.presence [game/stream] [message]`')
  else:
    if Type.lower() == 'stream':
      await bot.change_presence(game=discord.Game(name=thing,type=1,url='https://www.twitch.tv/a'),status='online')
      await ctx.send(f'Set presence to. `Streaming {thing}`')
    elif Type.lower() == 'game':
      await bot.change_presence(game=discord.Game(name=thing))
      await ctx.send(f'Set presence to `Playing {thing}`')
    elif Type.lower() == 'clear':
      await bot.change_presence(game=None)
      await ctx.send('Cleared Presence')
    else:
      await ctx.send('Usage: `.presence [game/stream] [message]`')
  
@bot.command()
async def ping(ctx):
    """Pong! Returns your websocket latency."""
    em = discord.Embed()
    em.title ='Pong! Websocket Latency:'
    em.description = f"{bot.ws.latency * 1000:.4f} ms"
    await ctx.send(embed=em)
    

@bot.command()
async def invite(ctx):
    await ctx.send('https://discordapp.com/oauth2/authorize?client_id=358300617665544194&scope=bot&permissions=66186303')
    


@bot.command(pass_context=True, hidden=True, name='eval')
@commands.is_owner()
async def _eval(ctx, *, body: str):
        """Evaluates a code"""

        env = {
            'bot': bot,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message,
        }

        env.update(globals())

        body = cleanup_code(body)
        stdout = io.StringIO()

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        try:
            exec(to_compile, env)
        except Exception as e:
            return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()
            try:
                await ctx.message.add_reaction('\u2705')
            except:
                pass

            if ret is None:
                if value:
                    await ctx.send(f'```py\n{value}\n```')
            else:
                await ctx.send(f'```py\n{value}{ret}\n```')




if not os.environ.get('TOKEN'):
  print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('\"'))
 
