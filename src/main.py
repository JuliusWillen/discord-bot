import discord
from discord.ext import commands
import os
import message_helpers as mh
from ai_response import AiResponse
import json
import random

token = os.getenv("DISCORD_TOKEN")
openai_key = os.getenv("OPENAI_KEY")
command = os.getenv("COMMAND")

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
    if not mh.should_respond(message, bot.user, command):
        return
    try:
        message_command = message.content.lower()[:len(command)]
        message_content = message.content.lower()[len(command)+1:]

        if message.content.lower() == "invite":
            await message.channel.send("https://discord.com/api/oauth2/authorize?client_id=503592450061762565&permissions=39582455643712&scope=bot")
        if message_command == command and message.id not in responded_messages:

            response = AI.get_JSON_response(message_content)
            response = json.loads(response)
            await reply(message, response["Reply"])
            await react(message, response["Reaction"])
    except:
        response = AI.get_normal_response(
            "Generera ett felmeddelande som handlar om att en Discord-bot har slutat fungera, men att någon jobbar på att försöka få det att fungera så fort som möjligt!")
        await reply(message, response)


async def reply(message, response):
    print(
        f"Received message with id {message.id}. Message content: {message.content}. Replying with {response}")
    await message.channel.send(response)
    responded_messages.append(message.id)


async def react(message, reaction):
    if random.randint(0, 1) == 0:
        return

    print(
        f"Received message with id {message.id}. Message content: {message.content}. Reacting with {reaction}")
    await message.add_reaction(reaction)
    responded_messages.append(message.id)

bot.run(token)
