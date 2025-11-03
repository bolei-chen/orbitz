"""Foundation model researcher node leveraging shared helper."""

from langchain_core.messages import AIMessage

from market_news_advisor.agents.state import State
from market_news_advisor.agents.researchers.research import research
from .prompt import foundation_model_researcher_system


def foundation_model_researcher(state: State) -> State:
    research_log = research(foundation_model_researcher_system)

    return {"messages": [AIMessage(content=research_log)]}


