import discord
import random

from dice_commands.roll_functions import roll_functions
from dice_commands.classic_roll import classic_roll

from discord.ext import commands


client = commands.Bot(command_prefix='.')


def my_latency():
    return round(client.latency * 1000)


def latency_commented(latency):
    if latency > 120:
        return ', I am very laggy..'
    else:
        return ', quite responsive'


@client.event
async def on_ready():
    print("The bot is ready to go.")


@client.command(aliases=['.rd', 'rd', 'rdam', 'r_damage', 'r_dano'])
async def roll_damage(ctx, *, dice_pars):

    messages = classic_roll.roll_damage(dice_pars, roll_functions)
    
    retStr = str("""```diff\n""") + messages + """ ```"""
    embed = discord.Embed(title="Dice rolls")
    embed.add_field(name="results", value=retStr)

    await ctx.send(embed=embed)


@client.command(aliases=['.r', 'r', './r', 'r_acerto', 'r_hit'])
async def roll(ctx, *, dice_pars):

    message = classic_roll.roll_dices(dice_pars, roll_functions)

    retStr = str("""```diff\n""") + message + """ ```"""
    embed = discord.Embed(title="Dice rolls")
    embed.add_field(name="results", value=retStr)

    await ctx.send(embed=embed)


@client.command(aliases=['.rs', 'rs', './rs', 'rolagem_atributo', 'stats_roll'])
async def roll_without_least(ctx, *, dice_pars):

    latency = my_latency()
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

    latency = my_latency()
    number_dices, type_dice, fix = roll_functions.interpre_plus_fix(
        dice_pars).values()
    dices = roll_functions.roll_n_dices(number_dices, type_dice)

    await ctx.send(f"here is your dice roll results! {dices} + {fix} => {sum(dices)+fix}")


async def basic_dice_roll_print(ctx, latency, all_dices):
    await ctx.send(f'ok! {latency}ms {latency_commented(latency)}')
    await ctx.send(f"here is your dice roll results! {all_dices}")


with open('my_key.txt', 'r') as file:
    data = file.read().replace('\n', '')
    client.run(data)
