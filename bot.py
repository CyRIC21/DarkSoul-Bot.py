# _________                                          /\        __________        __   
# \_   ___ \_______   ____   ____ ______   __________)/ ______ \______   \ _____/  |_ 
# /    \  \/\_  __ \_/ __ \_/ __ \\____ \_/ __ \_  __ \/  ___/  |    |  _//  _ \   __\
# \     \____|  | \/\  ___/\  ___/|  |_> >  ___/|  | \/\___ \   |    |   (  <_> )  |  
#  \______  /|__|    \___  >\___  >   __/ \___  >__|  /____  >  |______  /\____/|__|  
#         \/             \/     \/|__|        \/           \/          \/             

# (some made by umbresp)

try:
    import discord
    import os
    import traceback
    import textwrap
    import io
    from discord.ext import commands
    from contextlib import redirect_stdout
except:
    print("You do not have one of the required dependencies.")
    exit(0) # Exit code 0 = error

# The 4 lines below are a mess, will rewrite
bot = commands.Bot(command_prefix='?',description="Creeper's Bot\nOwner: CreeperSlayer11#7929\n\nHelp Commands",owner_id=311970805342928896)
bot.load_extension("cogs.utility")
bot.load_extension("cogs.misc")
bot.load_extension("cogs.mod")

# useless method but idk why it's here
def cleanup_code(content):
    """Automatically removes code blocks from the code."""
    # remove ```py\n```
    if content.startswith('```') and content.endswith('```'):
        return '\n'.join(content.split('\n')[1:-1])

    return content.strip('` \n')

# Print to console once bot is online
@bot.event
async def on_ready():
  print("Login successful.") # Add ascii art?
  
@bot.command(name='say')
async def say(ctx, message:str):
    """Say Something As The Bot"""
    if not message: # if the message is blank
        return
    else:
        await ctx.send(message)
        
# Since you seem to have copied the next cmd, I'll rewrite it besides this is horrible anyways lol
# also I renamed it to setpresence
# oh the horror of single quotes
        
@bot.command(name="setpresence")
@commands.is_owner()
async def presence(ctx, Type=None, *, msg=None):
  """Change the bot's discord game/stream!"""
  if Type is None and thing is None: # latter should never happen without first also happening but we want to be safe
    await ctx.send('You need to specify something to play/stream.')
  else:
    Type.lower() = Type # saves us the extra work
    if Type == 'stream':
      await bot.change_presence(game=discord.Game(name=msg,type=1,url="https://www.twitch.tv/iwouldputmytwitchchannelherebutidonthaveone"),status='online')
      await ctx.send(f'Set presence to. `Streaming {thing}`')
    elif Type == 'game':
      await bot.change_presence(game=discord.Game(name=thing))
      await ctx.send(f'Set presence to `Playing {thing}`')
    elif Type == 'clear':
      await bot.change_presence(game=None)
      await ctx.send('Cleared Presence')
    else:
      await ctx.send('Usage: `.presence [game/stream] [message]`')
  
@bot.command()
async def ping(ctx):
    """return websocket latency."""
    await ctx.send("Websocket Latency:")
    await ctx.send(f"{bot.ws.latency * 1000:.4f} ms")
    

@bot.command()
async def invite(ctx):
    await ctx.send("**Invite me to your server!**"
#     await ctx.send('https://discordapp.com/oauth2/authorize?client_id=364372021422981120&scope=bot&permissions=66186303')
    


      #  env.update(globals())

       # body = cleanup_code(body)
      #  stdout = io.StringIO()

      #  to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

       # try:
   
        # exec(to_compile, env)
      #  except Exception as e:
         #   return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')

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


# run as "main" method
if __name__ == "__main__":
    print("_________                                          /\        __________        __   ")
    print("\_   ___ \_______   ____   ____ ______   __________)/ ______ \______   \ _____/  |_ ")
    print("/    \  \/\_  __ \_/ __ \_/ __ \\____ \_/ __ \_  __ \/  ___/  |    |  _//  _ \   __\")
    print("\     \____|  | \/\  ___/\  ___/|  |_> >  ___/|  | \/\___ \   |    |   (  <_> )  |  ")
    print(" \______  /|__|    \___  >\___  >   __/ \___  >__|  /____  >  |______  /\____/|__|  ")
    print("        \/             \/     \/|__|        \/           \/          \/             ")
    # laziness
          
    print("Logging in to Discord...")
                
if not os.environ.get('TOKEN'):
  print("no token found REEEE!")
bot.run(os.environ.get('TOKEN').strip('\"'))
 
