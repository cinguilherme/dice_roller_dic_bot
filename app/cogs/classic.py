
from discord.ext import commands

from dice_commands.classic_roll import classic_roll
from dice_commands.roll_functions import roll_functions
from discord_embed_creator import build_embed_discord_message


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

    # Commands Roll
    @commands.command(aliases=['.r', 'r', './r', 'r_acerto', 'r_hit'],
                      brief=("Use as 'X d Y' or 'X d Y > z'"
                             "like '4 d10 > 6' "),
                      help=("The roll comand takes  'X d Y > z' format."
                            " eg like '4 d10 > 6' and displays the results"
                            "of the dice rolls with details "))
    async def roll(self, ctx, *, dice_pars):

        messages = classic_roll.roll_dices(dice_pars, roll_functions)

        embed = build_embed_discord_message(*messages.values())

        await ctx.send(embed=embed)

    # Error handling for the ROLL command
    @roll.error
    async def roll_error_handler(self, ctx, error):

        form = ("Srry, the roll command requires "
                " something like '10d10 > 5' to work. Try '.help roll' "
                "for more detailed information")

        await ctx.send(form)

    # Command Roll for damage
    @commands.command(aliases=['.rd', 'rd', 'rdam', 'r_damage', 'r_dano'])
    async def roll_damage(self, ctx, *, dice_pars):

        general, success, crits, dif = classic_roll.roll_damage(
            dice_pars, roll_functions).values()

        embed = build_embed_discord_message(
            general=general, sucess=success, crits=crits, bot=False)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Classic(client))
