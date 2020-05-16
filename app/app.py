import os

from discord.ext import commands
from discord.ext.commands import has_permissions


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


@client.command(pass_context=True, aliases=['cls'],
                help=("clear N to clear the last N messages from this bot, \
                        this command will not be able to delete messages that \
                        are old into this channel"),
                brief='clear N to clear the last N messages from this bot')
async def clear(ctx, ammount=100):
    channel = ctx.message.channel
    messages = []
    count = 0
    async for message in channel.history(limit=100):
        if message.author.name.find('Dice Roller') != -1:
            if count == ammount:
                break
            print(f'message to be deleted {message}')
            count += 1
            messages.append(message)

    await channel.delete_messages(messages)


@client.command(pass_context=True, aliases=['clsc'],
                help=("clear N to clear the last N messages commandfs for this bot, \
                        this command will not be able to delete messages that \
                        are old into this channel"),
                brief='clear N to clear the last N commands sent for this bot')
@has_permissions(administrator=True, manage_messages=True, manage_roles=True)
async def clear_commands_messages(ctx, ammount=100):
    channel = ctx.message.channel

    commands_list = client.all_commands.keys()

    def check_command(y): return len(list(filter(
        lambda x: y.startswith(f'.{x}'), commands_list)))

    print(commands_list)
    messages = []

    async for message in channel.history(limit=100):
        if message.content.startswith('.'):
            if check_command(message.content) > 0:
                messages.append(message)

    await channel.delete_messages(messages)


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
