from dotenv import load_dotenv
import os
from google import genai


load_dotenv()

gemini_api = os.getenv('GEMINI_API_KEY')
default_question = """
You are an AI that will output a list containing the important information 
for club announcements, especailly for meetings. When Given a message, You will first determine if the
announcement is for a club meeting. If no, then just return 'No Club Meeting'.
If yes, you will extract important information. You will first extract the 
basic premise of the event. Wether it be a project discussion, a club meeting, 
or something else. Then, you will return a list with these elements: 
[Club Name, Club Event type (like club meeting, some type of project discussion, etc),Date,Time,Location]

The location will usually be a building name with one or two Capital letter along with a decimal number
marking the room #, just give the entire location that is said within the message. For example: ECSW 1.315

Return the list and the list only, nothing else given that the message is some sort of announcement.
"""



def get_ai_response(your_question,api = gemini_api,question=default_question):
    client = genai.Client(api_key = api)
    response = client.models.generate_content(
        model ='gemini-2.5-flash',
        contents =default_question+your_question
    )

    return response.text