import discord


def build_simple_embed_discord_message(general, simple_output, bot=False):

    embed = create_result_success_embed()

    sucess_str = neutral_text(general)
    embed.add_field(name='general', value=sucess_str, inline=False)

    simple = neutral_text(simple_output)
    embed.add_field(name='results', value=simple, inline=False)

    return embed


def build_embed_discord_message(general, sucess, crits, crit_failures='',
                                balance='', bot=False):

    embed = create_base_embed()

    general_str = neutral_text(general)
    embed.add_field(name='general', value=general_str, inline=False)

    # display negative crits if any
    if '' != crit_failures:
        crit_failures_str = negative_text(crit_failures)
        embed.add_field(name='critical failures',
                        value=crit_failures_str, inline=False)

    # either all success or the balanced
    if not bot:
        sucess_str = positive_text(sucess)
        embed.add_field(name='success', value=sucess_str, inline=False)

        crits_str = positive_text(crits)
        embed.add_field(name='critical hits', value=crits_str, inline=False)
    else:
        sucess_str = positive_text(sucess)
        embed.add_field(name='success', value=sucess_str, inline=False)

        balance_str = positive_text(balance)
        embed.add_field(name='balance', value=balance_str, inline=False)

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


def create_result_success_embed():
    embed = discord.Embed(
        title="Dices results",
        colour=discord.Color.blue(),
        type='rich')
    embed.set_footer(text='Success result')
    return embed


def create_result_failure_embed():
    embed = discord.Embed(
        title="Dices results",
        colour=discord.Color.dark_grey(),
        type='rich')
    embed.set_footer(text='Fail result')
    return embed


def create_critical_failure_embed():
    embed = discord.Embed(
        title="Dices results",
        colour=discord.Color.red(),
        type='rich')
    embed.set_footer(text='Critical Fail result')
    return embed


def neutral_text(general):
    return str("""```yaml\n""") + general + """ ```"""


def positive_text(success):
    return str("""```diff\n+""") + success + """ ```"""


def negative_text(negative_crits):
    return str("""```diff\n-""") + negative_crits + """ ```"""
