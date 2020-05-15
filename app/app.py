import os

from discord.ext import commands

client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print("The bot is ready to go.")


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'loading extension {extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'unloading extension {extension}')


@client.command()
async def reload(ctx, ext):
    await unload(ctx, ext)
    await load(ctx, ext)


def load_cogs_startup():
    # preload my cogs at start
    for filename in os.listdir('./app/cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')


load_cogs_startup()

# start the bot with the key in the textfile
with open('my_key.txt', 'r') as file:
    data = file.read().replace('\n', '')
    client.run(data)
