from market_news_advisor.agents.state import State
from market_news_advisor.agents.advicer.prompt import advicer_system
from langchain_core.language_models import BaseLanguageModel
from langchain_core.messages import SystemMessage


def advicer(state: State, llm: BaseLanguageModel) -> State:
    system_message = SystemMessage(content=advicer_system.strip())
    response = llm.invoke([system_message, *state["messages"]])
    return {"messages": [response]}