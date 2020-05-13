import discord
import random

from dice_commands.roll_functions import roll_functions
from dice_commands.classic_roll import classic_roll

from discord.ext import commands


client = commands.Bot(command_prefix='.')


@client.event
async def on_ready():
    print("The bot is ready to go.")


@client.command(aliases=['.rd', 'rd', 'rdam', 'r_damage', 'r_dano'])
async def roll_damage(ctx, *, dice_pars):

    messages = classic_roll.roll_damage(dice_pars, roll_functions)
    general, success, success_crit = messages.values()

    embed = make_embed_messages_by_type(general=general, sucess=success, crits=success_crit)

    await ctx.send(embed=embed)


@client.command(aliases=['.r', 'r', './r', 'r_acerto', 'r_hit'])
async def roll(ctx, *, dice_pars):

    messages = classic_roll.roll_dices(dice_pars, roll_functions)
    general, success, crits, fails, balance, dificulty = messages.values()
    
    embed = make_embed_messages_by_type(general, success, crits, fails, balance)

    await ctx.send(embed=embed)


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


async def basic_dice_roll_print(ctx, latency, all_dices):
    await ctx.send(f'ok! {latency}ms {latency_commented(latency)}')
    await ctx.send(f"here is your dice roll results! {all_dices}")


def make_embed_zip_messages(messages):
    retStr = str("""```diff\n""") + messages + """ ```"""
    
    embed = create_base_embed()

    embed.add_field(name='general', value='general', inline=False)
    embed.add_field(name='sucesses', value='sss', inline=False)
    embed.add_field(name='failures', value='fff', inline=False)

    embed.add_field(name="results", value=retStr)

    return embed

def make_embed_messages_by_type(general, sucess, crits, crit_failures='', balance='', bot=False):
    
    embed = create_base_embed()

    general_str = str("""```diff\n""") + general + """ ```"""
    embed.add_field(name='general', value=general_str, inline=False)
    
    sucess_str = str("""```diff\n+""") + sucess + """ ```"""
    embed.add_field(name='sucesses', value=sucess_str, inline=False)
    
    crits_str = str("""```diff\n+""") + crits + """ ```"""
    embed.add_field(name='critical', value=crits_str, inline=False)

    if '' != crit_failures:
        crit_failures_str = str("""```diff\n-""") + crit_failures + """ ```"""
        embed.add_field(name='critical failures', value=crit_failures_str, inline=False)

    return embed


def create_base_embed():
    embed = discord.Embed(
        title="Dices results", 
        description='results from rolls',
        colour=discord.Color.dark_blue(),
        type='rich')
    
    embed.set_footer(text='Dice roller footer')
    embed.set_image(url='')
    embed.set_thumbnail(url='')
    embed.set_author(name='Dice Roller bot', icon_url='')
    return embed


with open('my_key.txt', 'r') as file:
    data = file.read().replace('\n', '')
    client.run(data)
