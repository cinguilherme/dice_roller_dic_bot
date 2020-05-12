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


@client.command(aliases=['.ra', 'ra', 'ratack', './r_atack'])
async def roll_atack(ctx, *, dice_pars):

    latency = my_latency()

    number_dices, type_dice, dificulty = roll_functions.interpret_inp(dice_pars).values()

    all_dices,success, crit_success, crit_failures = roll_functions.build_results(number_dices, type_dice, dificulty).values()
    
    await basic_dice_roll_print(ctx, latency, all_dices)

    await ctx.send(f'for the dificulty of {dificulty}, you had {len(success)} success {success}')
    await ctx.send(f'your final results of success is {len(success)}')
    await ctx.send(f'your final results of successwith expecialization {len(success)+len(crit_success)} ')


@client.command(aliases=['.r', 'r', './r'])
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


async def basic_dice_roll_print(ctx, latency, all_dices):
    await ctx.send(f'ok! {latency}ms {latency_commented(latency)}')
    await ctx.send(f"here is your dice roll results! {all_dices}")
    

with open('my_key.txt', 'r') as file:
    data = file.read().replace('\n', '')
    client.run(data)

