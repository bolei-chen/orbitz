"""FAANG researcher node leveraging the shared research helper."""

from langchain_core.messages import AIMessage

from market_news_advisor.agents.researchers.research import research
from market_news_advisor.agents.state import State

from .prompt import faang_researcher_system
from logging import Logger


def faang_researcher(state: State, logger: Logger) -> State:
    logger.info("researching FAANG...")
    research_log = research(faang_researcher_system)
    return {"messages": [AIMessage(content=research_log)],
            "researched": ["faang"]}
