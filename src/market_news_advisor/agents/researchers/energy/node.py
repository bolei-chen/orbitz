"""Energy researcher node leveraging the shared deep-research helper."""

from langchain_core.messages import AIMessage

from market_news_advisor.agents.researchers.research import research
from market_news_advisor.agents.state import State

from .prompt import energy_researcher_system
from logging import Logger


def energy_researcher(state: State, logger: Logger) -> State:
    logger.info("researching energy...")
    research_log = research(energy_researcher_system)
    return {"messages": [AIMessage(content=research_log)], 
            "researched": ["energy"]}


