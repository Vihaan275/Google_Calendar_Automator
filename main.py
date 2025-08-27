import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from ask_gemini import get_ai_response


load_dotenv()

disc_tok = os.getenv('DISCORD_TOKEN')
announcements_channel = os.getenv('TARGET_CHANNEL_ID')

intents = discord.Intents.default()
intents.messages = True  # So bot can read messages
intents.message_content = True  # Required for reading message content

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        process = get_ai_response(message.content)

        print(process)

client.run(disc_tok)


    
