import os
import dotenv
from openai import OpenAI
from langchain_core.messages import AIMessage
from market_news_advisor.agents.state import State

dotenv.load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL_NAME = os.getenv("OPENAI_MODEL_NAME")

RESEARCHERS = set(["foundation_model", "faang", "chips", "energy", "fed_macro", "biotech"])

client = OpenAI(api_key=OPENAI_API_KEY)

def research(prompt: str) -> str:
    response = client.responses.create(
        model=MODEL_NAME,
        tools=[
            {"type": "web_search"}
        ],
        reasoning={"effort": "low"},
        max_output_tokens=1200,
        input=prompt,
    )
    return response.output_text

def research_checker(state: State) -> State:
    if set(state["researched"]) >= RESEARCHERS:
        return {"messages": AIMessage(content="All research is complete!!")}
    
    