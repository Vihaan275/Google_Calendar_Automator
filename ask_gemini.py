from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

gemini_api = os.getenv('GEMINI_API_KEY')
default_question = """
You are an AI that will output a list containing the important information 
for club announcements, especailly for meetings. When Given a message, You will first determine if the
announcement is for a club meeting. If no, then just return 'No Club Meeting'.
If yes, you will extract important information. You will first extract the 
basic premise of the event. Wether it be a project discussion, a club meeting (specify club meeting, not just 'meeting'),
or something else. Then, you will return a list with these elements, and always assume american date format with texas timezone: 
['Club Name', 'Club Event type' (like club meeting or some type of project discussion etc),Year (assume it is current year unless we are very close to the end of the year),month(convert word month into numerical month),date,Start hour(convert to military time),start minutes,End hour (default to 1 hour after start time if nothing is specified and make sure to convert to military time),end minutes,Location]

The location will usually be a building name with one or two Capital letters along with a decimal number
marking the room #, just give the entire location that is said within the message. For example: ECSW 1.315

Return the list and the list only, nothing else given that the message is some sort of announcement.
At the end of the list, the final item of the list should describe what to do within the google calendar.
If it is a new event, then say 'add' as the final item.


If the message is a correction for a previous meeting, then you say 'update' as the final item in the list

if the message is a cancellation of a meeting, then you say 'remove' as the final item in the list. 
"""

#[name,event type, year, month, date,start_time,end_time,location]

def get_ai_response(your_question,api = gemini_api,question=default_question):
    
    # Configure the API key
    genai.configure(api_key=api)
    
    # Create a model instance
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    # Generate content
    response = model.generate_content(question + your_question)
    
    return response.text