import discord
from discord.ext import commands

from dice_commands.classic_roll import classic_roll
from dice_commands.roll_functions import roll_functions
from discord_embed_creator import build_embed_discord_message


class Classic(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('Classic cog ready')

    # Commands

    @commands.command(aliases=['.r', 'r', './r', 'r_acerto', 'r_hit'])
    async def roll(self, ctx, *, dice_pars):

        messages = classic_roll.roll_dices(dice_pars, roll_functions)

        embed = build_embed_discord_message(*messages.values())

        await ctx.send(embed=embed)

    @commands.command(aliases=['.rd', 'rd', 'rdam', 'r_damage', 'r_dano'])
    async def roll_damage(self, ctx, *, dice_pars):

        general, success, crits, dif = classic_roll.roll_damage(
            dice_pars, roll_functions).values()

        embed = build_embed_discord_message(
            general=general, sucess=success, crits=crits, bot=False)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Classic(client))
