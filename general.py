import discord
from discord.ext import commands

class general(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Commands
    @commands.command(aliases=['speed','connection'])
    async def ping(self, ctx):
        print("Ponged !")
        await ctx.send(f":eyes: Ping = {round(self.client.latency * 1000)}ms")

def setup(client):
    client.add_cog(general(client))