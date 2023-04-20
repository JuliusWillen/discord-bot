import discord
from discord.ext import commands
import triggers
import responses
import random
import reactions
import os
import message_helpers as mh
from ai_response import AiResponse

token = os.getenv("DISCORD_TOKEN")
openai_key = os.getenv("OPENAI_KEY")

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)
responded_messages = []

AI = AiResponse(openai_key)


@bot.event
async def on_ready():
    print('Bot is ready...')


@bot.event
async def on_message(message):
    if not mh.should_respond(message, bot.user):
        return
    print(message.content.lower())
    if message.content.lower() == "invite":
        await message.channel.send("https://discord.com/api/oauth2/authorize?client_id=503592450061762565&permissions=39582455643712&scope=bot")
    # hello!
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
    # turtle
    elif mh.message_contains(message.content.lower(), triggers.turtle) and message.id not in responded_messages:
        await react(message, random.choice(reactions.turtle))
    # if gpt is the first two letters of the message
    elif message.content.lower()[:2] == "gpt" and message.id not in responded_messages:
        print(
            "Received message with id {message.id}. Message content: {message.content}. Replying with AI response")
        await reply(message, AI.get_response(message.content.lower()[3:]))


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

bot.run(token)
