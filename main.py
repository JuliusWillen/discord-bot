import discord
from discord.ext import commands
import discord_token as token
import triggers
import responses
import random

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
responded_messages = []

@bot.event
async def on_ready():
    print('Bot is ready.')

@bot.event
async def on_message(message):
    # hello
    if message.content.lower() in triggers.hello and message.id not in responded_messages:
        await reply(message, random.choice(responses.hello))
    # bye
    elif message.content.lower() in triggers.bye and message.id not in responded_messages:
        await reply(message, random.choice(responses.bye))

async def reply(message, response):
    print(f"Received message with id {message.id}. Message content: {message.content}. Replying with {response}")
    await message.channel.send(response)
    responded_messages.append(message.id)

bot.run(token.discord_token)
