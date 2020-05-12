import discord
import random

import roll_functions

from discord.ext import commands


client = commands.Bot(command_prefix = '.')

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

    latency = my_latency()
    number_dices, type_dice, dificulty = roll_functions.interpret_inp(dice_pars).values()
    all_dices,success, crit_success, crit_failures = roll_functions.build_results(number_dices, type_dice, dificulty).values()
    
    await basic_dice_roll_print(ctx, latency, all_dices)

    await ctx.send(f'for the dificulty of {dificulty}, you had {len(success)} success {success}')
    await ctx.send(f'your final results of success is {len(success)}')
    await ctx.send(f'your final results of successwith expecialization {len(success)+len(crit_success)} ')


@client.command(aliases=['.r', 'r', './r', 'r_acerto', 'r_hit'])
async def roll(ctx, *, dice_pars):

    latency = my_latency()
    number_dices, type_dice, dificulty = roll_functions.interpret_inp(dice_pars).values()
    all_dices,success, crit_success, crit_failures = roll_functions.build_results(number_dices, type_dice, dificulty).values()

    await basic_dice_roll_print(ctx, latency, all_dices)

    await ctx.send(f'for the dificulty of {dificulty}, you had {len(success)} success {success}')
    await ctx.send(f'you had {len(crit_failures)} critical failures {crit_failures}')
    await ctx.send(f'you had {len(crit_success)} critical success {crit_success}')
       
    success_calc = roll_functions.critical_balance(success, crit_success, crit_failures)

    await ctx.send(f'your final results of success is {len(success) - len(crit_failures)}')
    await ctx.send(f'your final results of successwith expecialization {success_calc}')

@client.command(aliases=['.rs', 'rs', './rs', 'rolagem_atributo', 'stats_roll'])
async def roll_without_least(ctx, *, dice_pars):

    latency = my_latency()
    number_dices, type_dice, dificulty = roll_functions.interpret_inp(dice_pars).values()
    all_dices,success, crit_success, crit_failures = roll_functions.build_results(number_dices, type_dice, dificulty).values()

    all_dices.sort()
    minus_least = all_dices[1::]
    
    await ctx.send(f"here is your dice roll results! {all_dices}")
    await ctx.send(f"here is without the least value! {minus_least}")

@client.command(aliases=['.rfx', 'rfx', './rfx', 'rolagem_fixo'])
async def roll_plus_fix(ctx, *, dice_pars):

    latency = my_latency()
    number_dices, type_dice, fix = roll_functions.interpre_plus_fix(dice_pars).values()
    dices = roll_functions.roll_n_dices(number_dices, type_dice)
    
    await ctx.send(f"here is your dice roll results! {dices} + {fix} => {sum(dices)+fix}")

async def basic_dice_roll_print(ctx, latency, all_dices):
    await ctx.send(f'ok! {latency}ms {latency_commented(latency)}')
    await ctx.send(f"here is your dice roll results! {all_dices}")
    

with open('my_key.txt', 'r') as file:
    data = file.read().replace('\n', '')
    client.run(data)

