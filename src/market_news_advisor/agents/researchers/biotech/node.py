"""Biotech researcher node leveraging the shared deep-research helper."""

from langchain_core.messages import AIMessage

from market_news_advisor.agents.researchers.research import research
from market_news_advisor.agents.state import State

from .prompt import biotech_researcher_system
from logging import Logger

def biotech_researcher(state: State, logger: Logger) -> State:
    logger.info("researching biotech...")
    research_log = research(biotech_researcher_system)
    return {"messages": [AIMessage(content=research_log)],
            "researched": ["biotech"]}


