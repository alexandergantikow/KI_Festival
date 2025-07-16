from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="config.env")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def chat_gpt(user_prompt, system_prompt, model="gpt-4o-mini"):
    client = OpenAI(api_key=OPENAI_API_KEY)
    completion = client.chat.completions.create(
        model=model,
        store=True,
        messages=[
            {"role": "system", "content": f"{system_prompt}"},
            {"role": "user", "content": f"{user_prompt}"}
        ],
        stream=True
    )
    return completion