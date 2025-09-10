import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
from ask_gemini import get_ai_response
import gcsa
from gcsa.google_calendar import GoogleCalendar
import ast
from gcsa.event import Event
from datetime import datetime
from keep_alive import keep_alive



load_dotenv()

calendar = GoogleCalendar(
    os.getenv('GOOGLE_CALENDAR_EMAIL'),
    credentials_path='credentials.json'
)

disc_tok = os.getenv('DISCORD_TOKEN')
announcements_channel = int(os.getenv('TARGET_CHANNEL_ID'))

intents = discord.Intents.default()
intents.messages = True  # So bot can read messages
intents.message_content = True  # Required for reading message content

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    

    # elif message.channel.id == announcements_channel:
    else:
        process = get_ai_response(your_question=message.content,author=message.author.name)
        print(process)

        if process != 'No Club Meeting':
            main_contents = ast.literal_eval(process)
            name,event_type, year, month, date,start_hour,start_min,end_hour,end_min,place,action = main_contents
            
            if action == 'add':
                event = Event(
                    name+' '+event_type,
                    start=datetime(year,month,date,start_hour,start_min),
                    end=datetime(year,month,date,end_hour,end_min),
                    location=place,
                    minutes_before_popup_reminder=30
                )

                calendar.add_event(event)

                print('added event')
            
            elif action == 'update':
                pass

            elif action == 'remove':
                pass

        
        
client.run(disc_tok)


    


