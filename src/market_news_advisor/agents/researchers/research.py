import os
import dotenv
from openai import OpenAI

dotenv.load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("OPENAI_MODEL_NAME")

client = OpenAI(api_key=OPENAI_API_KEY)

def research(prompt: str) -> str:
    response = client.responses.create(
        model=MODEL_NAME,
        tools=[
            {"type": "web_search"}
        ],
        input=prompt,
    )
    return response.output_text 
