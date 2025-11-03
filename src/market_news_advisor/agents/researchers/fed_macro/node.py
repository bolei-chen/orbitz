"""Federal Reserve & macro researcher node using shared helper."""

from langchain_core.messages import AIMessage

from market_news_advisor.agents.researchers.research import research
from market_news_advisor.agents.state import State

from .prompt import fed_macro_researcher_system


def fed_macro_researcher(state: State) -> State:
    research_log = research(fed_macro_researcher_system)
    return {"messages": [AIMessage(content=research_log)]}


