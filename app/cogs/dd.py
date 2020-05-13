import discord

from discord.ext import commands

class DandDCog(commands.Cog):

    def __init__(self, client):
        self.client = client
        
    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print('dd cog is ready')

    # Commands
    @commands.command()
    async def check(self, ctx):
        await ctx.send('cog dd is ready')
        

def setup(client):
    client.add_cog(DandDCog(client))