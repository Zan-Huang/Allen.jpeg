import os
import discord

from dotenv import load_dotenv
import random
import datetime

from discord.ext import commands


load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print("connected")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    allen_msg = [
                'An Allen.jpeg can be seen currently running silently through the grass',
                'Allen looks at you intently from a distance.',
                'Allen.jpeg is gathering nuts for hibernation',
                'Allen is currently with Jark Mones.'
    ]


    if ('allen' in message.content.lower()):
        allenaction = random.choice(allen_msg)
        await message.channel.send(allenaction)

    if('!bless' in message.content):
        print("run")
        client_name = message.author
        text = "you have been blessed by allen.jpeg %s" %client_name
        await message.channel.send(text)

client.run(TOKEN)
