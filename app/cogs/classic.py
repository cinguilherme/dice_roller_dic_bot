
from discord.ext import commands
import time

from dice_commands.classic_roll.classic_roll import roll_dices, roll_damage
from dice_commands.roll_functions import roll_functions
from discord_embed_creator import build_embed_discord_message, \
    build_simple_embed_discord_message

# TODO .mr 2 * 30d4 > 1 BUG

output_configuration = True


def get_embed():
    if output_configuration:
        return build_simple_embed_discord_message
    else:
        return build_embed_discord_message


def roll_dices_ref(regular_input):
    messages = roll_dices(
        regular_input, roll_functions, output_configuration).values()

    embed_function = get_embed()

    embed = embed_function(*messages)
    return embed


def roll_damage_ref(regular_input):
    messages = roll_damage(regular_input, roll_functions).values()

    embed_function = get_embed()
    embed = embed_function(*messages)
    return embed


class Classic(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events for cog ready
    @commands.Cog.listener()
    async def on_ready(self):
        print('Classic cog ready')

    # Event for command NOT FOUND
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Srry, I dont recognize this command. "
                           " Maybe it is on another Cog")
        else:
            print(f'internal error {error}')

    # Commands Roll
    @commands.command(aliases=['.r', 'r', './r', 'r_acerto', 'r_hit'],
                      brief=("Use as 'X d Y' or 'X d Y > z'"
                             "like '4 d10 > 6' "),
                      help=("The roll comand takes  'X d Y > z' format."
                            " eg like '4 d10 > 6' and displays the results"
                            "of the dice rolls with details "),
                      cog="Classic")
    async def roll(self, ctx, *, dice_pars):

        embed = roll_dices_ref(dice_pars)

        await ctx.send(embed=embed)

    # COMMAND MULTIPLE ROLLS
    @commands.command(aliases=['mr'],
                      brief=("Use as 'N * X d Y' or 'N * X d Y > z'"
                             "like '2 * 4 d10 > 6' "),
                      help=("The roll comand takes 'N * (roll)' format."
                            " eg like '2 * 4 d10 > 6' and displays the results"
                            "of the dice rolls with details "),
                      cog="Classic")
    async def mroll(self, ctx, *, dice_pars):

        number_of_rolls = int(dice_pars.split('*')[0])
        regular_input = dice_pars.split('*')[1]

        for n in range(number_of_rolls):

            embed = roll_dices_ref(regular_input)

            await ctx.send(embed=embed)
            time.sleep(0.3)
    # Error handling for the ROLLS command

    @roll.error
    async def roll_error_handler(self, ctx, error):

        form = ("Srry, the roll command requires "
                " something like '10d10 > 5' to work. Try '.help roll' "
                "for more detailed information")

        await ctx.send(form)
    # END OF COMMAND ROLL

    # Command Roll for damage
    @commands.command(aliases=['.rd', 'rd', 'rdam', 'r_damage', 'r_dano'],
                      brief=("Use as 'X d Y' or 'X d Y > z'"
                             "like '2 * 4 d10 > 6' "),
                      help=("The roll comand takes 'N * (roll)' format."
                            " eg like '2 * 4 d10 > 6' and displays the results"
                            "of the dice rolls for damage with details "),
                      cog="Classic")
    async def roll_damage(self, ctx, *, dice_pars):

        embed = roll_damage_ref(dice_pars)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Classic(client))
