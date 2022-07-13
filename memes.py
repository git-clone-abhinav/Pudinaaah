"""
This module contains the Meme related functions.
"""

import discord
from discord.ext import commands

# insert a function here that returns a json object of posts.json file.
import json
import random
def getmeme():
    """
    This function returns a json object of posts.json file.
    """
    random_choice = random.randint(1, 10)
    with open("reddit\posts.json", "r") as f:
        posts = json.load(f)
        temp = {}
        post = posts[random_choice]
        temp['title'] = post['title'][0]
        temp['author'] = post['user'][0]
        temp['ups'] = post['upvotes'][0]
        temp['comments'] = post['comments'][0]
        temp['created'] = post['time'][0]
        if "http" in post['content_link'][0]:
            temp['url'] = post['content_link']
        else:
            temp['url'] = "https://reddit.com" + post['content_link'][0]

        return temp
