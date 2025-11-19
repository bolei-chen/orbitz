"""Federal Reserve & macro researcher node using shared helper."""

from langchain_core.messages import AIMessage

from market_news_advisor.agents.researchers.research import research
from market_news_advisor.agents.state import State

from .prompt import fed_macro_researcher_system
from logging import Logger


def fed_macro_researcher(state: State, logger: Logger) -> State:
    logger.info("researching federal reserve and macro...")
    research_log = research(fed_macro_researcher_system)
    state["messages"].append(AIMessage(content=research_log))
    state["researches"]["fed_macro"]["fed_macro"] = research_log
    return state


