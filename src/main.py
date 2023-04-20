import discord
from discord.ext import commands
import triggers
import responses
import random
import reactions
import os
import message_helpers as mh

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
responded_messages = []


@bot.event
async def on_ready():
    print('Bot is ready...')


@bot.event
async def on_message(message):
    if not mh.should_respond(message, bot.user):
        return
    # hello
    if mh.message_contains(message.content.lower(), triggers.hello) and message.id not in responded_messages:
        await reply(message, random.choice(responses.hello))
    # bye
    elif mh.message_contains(message.content.lower(), triggers.bye) and message.id not in responded_messages:
        await reply(message, random.choice(responses.bye))
    # haha
    elif mh.message_contains(message.content.lower(), triggers.haha) and message.id not in responded_messages:
        await react(message, random.choice(reactions.haha))
    # cool
    elif mh.message_contains(message.content.lower(), triggers.cool) and message.id not in responded_messages:
        await react(message, random.choice(reactions.cool))
    # sausage
    elif mh.message_contains(message.content.lower(), triggers.sausage) and message.id not in responded_messages:
        await react(message, random.choice(reactions.sausage))


async def reply(message, response):
    print(
        f"Received message with id {message.id}. Message content: {message.content}. Replying with {response}")
    await message.channel.send(response)
    responded_messages.append(message.id)


async def react(message, reaction):
    print(
        f"Received message with id {message.id}. Message content: {message.content}. Reacting with {reaction}")
    await message.add_reaction(reaction)
    responded_messages.append(message.id)

bot.run(os.getenv("DISCORD_TOKEN"))
