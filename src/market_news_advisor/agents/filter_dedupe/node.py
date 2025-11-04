from market_news_advisor.agents.state import State
from market_news_advisor.agents.filter_dedupe.prompt import filter_dedupe_system
from langchain_core.language_models import BaseLanguageModel
from langchain_core.messages import SystemMessage


def filter_dedupe(state: State, llm: BaseLanguageModel) -> State:
    system_message = SystemMessage(content=filter_dedupe_system.strip())
    response = llm.invoke([system_message, *state["messages"]])
    return {"messages": [response]}

