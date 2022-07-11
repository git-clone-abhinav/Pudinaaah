"""
This module contains the Meme related functions.
"""

import discord
from discord.ext import commands

# insert a function here that returns a json object of posts.json file.


class memes(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command(aliases=['memes'])
    async def meme(self, ctx):
        print("Ponged !")
        await ctx.send(f":eyes: Ping = {round(self.client.latency * 1000)}ms")

def setup(client):
    client.add_cog(memes(client))