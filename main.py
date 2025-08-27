import discord
from discord.ext import commands
from dotenv import load_dotenv
import os


load_dotenv()

disc_tok = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.messages = True  # So bot can read messages
intents.message_content = True  # Required for reading message content

client = discord.Client(intents=intents)