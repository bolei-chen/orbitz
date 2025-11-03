"""Biotech researcher node leveraging the shared deep-research helper."""

from langchain_core.messages import AIMessage

from market_news_advisor.agents.researchers.research import research
from market_news_advisor.agents.state import State

from .prompt import biotech_researcher_system


def biotech_researcher(state: State) -> State:
    research_log = research(biotech_researcher_system)
    return {"messages": [AIMessage(content=research_log)]}


