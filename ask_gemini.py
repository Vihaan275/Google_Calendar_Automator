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
or something else. Then, you will see if 
"""



def get_ai_response(api = gemini_api,question,)