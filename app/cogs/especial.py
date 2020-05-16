
from discord.ext import commands

from dice_commands.roll_functions.roll_functions import \
    build_results, interpret_inp, interpre_plus_fix, roll_n_dices


class Especial(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands rolagem_atributo Roll
    @commands.command(aliases=['.rs', 'rs', './rs',
                               'rolagem_atributo', 'stats_roll'])
    async def roll_without_least(self, ctx, *, dice_pars):

        number_dices, type_dice, dificulty = interpret_inp(
            dice_pars).values()
        all_dices, success, crit_success, crit_failures = build_results(
            number_dices, type_dice, dificulty).values()

        all_dices.sort()

        minus_least = all_dices[1::]

        await ctx.send(f"here is your dice roll results! {all_dices}")
        await ctx.send(f"here is without the least value! {minus_least}")

    # Commands rolagem_fixo Roll
    @commands.command(aliases=['.rfx', 'rfx', './rfx', 'rolagem_fixo'])
    async def roll_plus_fix(self, ctx, *, dice_pars):

        number_dices, type_dice, fix = interpre_plus_fix(
            dice_pars).values()

        dices = roll_n_dices(number_dices, type_dice)
        res = sum(dices)+fix
        await ctx.send(f"dice roll results! {dices} + {fix} => {res}")


def setup(client):
    client.add_cog(Especial(client))
