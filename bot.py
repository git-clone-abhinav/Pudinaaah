import discord
import random
import os
from discord.ext import commands, tasks
import constants, memes

from dotenv import load_dotenv

# Getting Token from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


client = commands.Bot(command_prefix=constants.EXT)


# Bot's Ready
@client.event
async def on_ready():
    auto_meme.start()
    print("Bot is ready.")
    print(f"Logged in as: {client.user.name} ID: {client.user.id}")
    print(f"Online in Guilds:")
    for server in client.guilds:
        print(f"Guild name: {server.name}")
        print(f"Guild ID: {server.id}")


if __name__ == "__main__":
    extensions = {"general"}
    for extension in extensions:
        try:
            client.load_extension(extension)
            print(f"Loaded Cog {extension} successfully")
        except Exception as error:
            print(f"Failed to load Cog {extension}. Reason: {error}")


@tasks.loop(seconds=constants.delay)
async def auto_meme():
    channel = client.get_channel(int(constants.MEME_CHANNEL_ID))
    meme = memes.getmeme()
    embed = discord.Embed(title=meme['title'], url=meme['url'],description="r/FingMemes", color=0x00ff00)
    embed.set_author(name=meme['author'], url=f"https://reddit.com/u/{meme['author']}")
    embed.set_image(url = meme['url'])
    embed.set_footer(text=f"Upvotes: {meme['ups']} | Comments: {meme['comments']}")
    await channel.send(embed=embed)


@client.command(name="load")
@commands.has_role(constants.ADMIN_ROLE)
async def load(ctx, extension):
    if extension == "":
        await ctx.send("Please enter a valid cog.")
    try:
        client.load_extension(extension)
        await ctx.send(f"Loaded {extension}!")
    except Exception as error:
        await ctx.send(f"Failed to load Cog {extension}. Reason: {error}")


@client.command(name="unload")
@commands.has_role(constants.ADMIN_ROLE)
async def unload(ctx, extension):
    if extension == "":
        await ctx.send("Please enter a valid cog.")
    try:
        client.unload_extension(extension)
        await ctx.send(f"Unloaded {extension}!")
    except Exception as error:
        await ctx.send(f"Failed to unload Cog {extension}. Reason: {error}")


@client.command(name="reload")
@commands.has_role(constants.ADMIN_ROLE)
async def reload(ctx, extension):
    if extension == "":
        await ctx.send("Please enter a valid cog.")
    try:
        client.unload_extension(extension)
        client.load_extension(extension)
        await ctx.send(f"Reloaded {extension}!")
    except Exception as error:
        await ctx.send(f"Failed to reload Cog {extension}. Reason: {error}")


@client.command(name="logout")
@commands.has_role(constants.ADMIN_ROLE)
async def logout(ctx):
    auto_meme.stop()
    await ctx.send("<a:jnl:856740626170904606> Logging Out")
    await client.logout()


@logout.error
async def logout_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send(f"You do not have permission to run this command!")
    else:
        raise error


client.run(TOKEN)