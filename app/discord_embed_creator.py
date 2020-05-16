import discord


def build_simple_embed_discord_message(general, simple_output, bot=False):
    print(general, simple_output)
    embed = create_simpler_embed()

    sucess_str = general_information(general)
    embed.add_field(name='general', value=sucess_str, inline=False)

    simple = general_information(simple_output)
    embed.add_field(name='results', value=simple, inline=False)

    return embed


def build_embed_discord_message(general, sucess, crits, crit_failures='',
                                balance='', bot=False):

    embed = create_base_embed()

    general_str = general_information(general)
    embed.add_field(name='general', value=general_str, inline=False)

    # display negative crits if any
    if '' != crit_failures:
        crit_failures_str = negative_crits_information(crit_failures)
        embed.add_field(name='critical failures',
                        value=crit_failures_str, inline=False)

    # either all success or the balanced
    if not bot:
        sucess_str = success_general(sucess)
        embed.add_field(name='success', value=sucess_str, inline=False)

        crits_str = critical_hits_information(crits)
        embed.add_field(name='critical hits', value=crits_str, inline=False)
    else:
        sucess_str = success_general(sucess)
        embed.add_field(name='success', value=sucess_str, inline=False)

        balance_str = balance_success_information(balance)
        embed.add_field(name='balance', value=balance_str, inline=False)

    return embed


def general_information(general):
    return str("""```yaml\n""") + general + """ ```"""


def success_general(success):
    return str("""```diff\n+""") + success + """ ```"""


def balance_success_information(balance):
    return str("""```diff\n+""") + balance + """ ```"""


def negative_crits_information(negative_crits):
    return str("""```diff\n-""") + negative_crits + """ ```"""


def critical_hits_information(crits):
    return str("""```diff\n+""") + crits + """ ```"""


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


def create_simpler_embed():
    embed = discord.Embed(
        title="Dices results",
        type='rich')
    return embed
