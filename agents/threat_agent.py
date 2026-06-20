import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-1.5-flash")


def detect_threats(logs):

    prompt = f"""
    Analyze these security logs.

    Detect:
    - Brute Force Attacks
    - SQL Injection
    - Port Scanning
    - Malware Activity

    Logs:
    {logs}

    Return:
    Threat Name
    Severity
    Explanation
    """

    response = model.generate_content(prompt)

    return response.text