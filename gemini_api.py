import dotenv
import os
from google import genai

def get_gemini_response(gemini_input):
    dotenv.load_dotenv()
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=gemini_input
    )

    return response.text
