import os
import random

import discord
from discord.ext import commands

from dice_commands.classic_roll import classic_roll
from dice_commands.roll_functions import roll_functions
from discord_embed_creator import build_embed_discord_message

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


@client.command(aliases=['.rs', 'rs', './rs', 'rolagem_atributo', 'stats_roll'])
async def roll_without_least(ctx, *, dice_pars):

    number_dices, type_dice, dificulty = roll_functions.interpret_inp(
        dice_pars).values()
    all_dices, success, crit_success, crit_failures = roll_functions.build_results(
        number_dices, type_dice, dificulty).values()

    all_dices.sort()
    minus_least = all_dices[1::]

    await ctx.send(f"here is your dice roll results! {all_dices}")
    await ctx.send(f"here is without the least value! {minus_least}")


@client.command(aliases=['.rfx', 'rfx', './rfx', 'rolagem_fixo'])
async def roll_plus_fix(ctx, *, dice_pars):

    number_dices, type_dice, fix = roll_functions.interpre_plus_fix(
        dice_pars).values()
    dices = roll_functions.roll_n_dices(number_dices, type_dice)

    await ctx.send(f"here is your dice roll results! {dices} + {fix} => {sum(dices)+fix}")


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
