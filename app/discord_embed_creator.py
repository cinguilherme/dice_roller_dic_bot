import discord

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
