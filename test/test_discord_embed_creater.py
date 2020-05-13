from unittest import TestCase

from app import discord_embed_creator

class EmbedCreatorTest(TestCase):

    def test_basic(self):
        embed = discord_embed_creator.create_base_embed()
        assert(embed != None)