import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.0-flash")


def generate_recommendations(vulnerabilities):

    prompt = f"""
    Vulnerabilities Found:

    {vulnerabilities}

    Generate security recommendations.
    """

    response = model.generate_content(prompt)

    return response.text