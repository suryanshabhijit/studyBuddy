import requests
import os
from dotenv import load_dotenv

load_dotenv()  # load TOGETHER_API_KEY from .env

TOGETHER_API_KEY = os.getenv("API_KEY")

def generate_answer(prompt, model="mistralai/Mistral-7B-Instruct-v0.1"):
    url = "https://api.together.xyz/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {TOGETHER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        print("Together API Error:", response.text)
        raise Exception("Failed to get response from Together.ai")

    return response.json()['choices'][0]['message']['content']
