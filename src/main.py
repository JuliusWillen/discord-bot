import discord
from discord.ext import commands
import triggers
import responses
import random
import reactions
import os
import datetime

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
    if not should_respond(message):
        return
    # hello
    if message_contains(message.content.lower(), triggers.hello) and message.id not in responded_messages:
        await reply(message, random.choice(responses.hello))
    # bye
    elif message_contains(message.content.lower(), triggers.bye) and message.id not in responded_messages:
        await reply(message, random.choice(responses.bye))
    # haha
    elif message_contains(message.content.lower(), triggers.haha) and message.id not in responded_messages:
        await react(message, random.choice(reactions.haha))
    # cool
    elif message_contains(message.content.lower(), triggers.cool) and message.id not in responded_messages:
        await react(message, random.choice(reactions.cool))

async def reply(message, response):
    print(f"Received message with id {message.id}. Message content: {message.content}. Replying with {response}")
    await message.channel.send(response)
    responded_messages.append(message.id)

async def react(message, reaction):
    print(f"Received message with id {message.id}. Message content: {message.content}. Reacting with {reaction}")
    await message.add_reaction(reaction)
    responded_messages.append(message.id)

def message_contains(message, triggers):
    # check if message contains any of the triggers
    for trigger in triggers:
        if trigger in message:
            return True
        
def should_respond(message):
    # check if bot should respond to message
    if message.author == bot.user:
        return False
    elif message.author.bot:
        return False
    else:
        timestamp = message.created_at        
        now = datetime.datetime.now(datetime.timezone.utc)
        time_diff = (now - timestamp).total_seconds()
        if time_diff > 2:
            return False
        return True

bot.run(os.getenv("DISCORD_TOKEN"))
