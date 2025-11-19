"""Energy researcher node leveraging the shared deep-research helper."""

from langchain_core.messages import AIMessage

from market_news_advisor.agents.researchers.research import research
from market_news_advisor.agents.state import State

from .prompt import exxon_energy_researcher_system, chevron_energy_researcher_system, nextera_energy_researcher_system
from logging import Logger


def exxon_researcher(state: State, logger: Logger) -> State:
    logger.info("researching Exxon Mobil energy...")
    research_log = research(exxon_energy_researcher_system)
    state["researches"]["energy"]["exxon"] = research_log
    state["messages"].append(AIMessage(content=research_log))
    return state

def chevron_researcher(state: State, logger: Logger) -> State:
    logger.info("researching Chevron energy...")
    research_log = research(chevron_energy_researcher_system)
    state["researches"]["energy"]["chevron"] = research_log
    state["messages"].append(AIMessage(content=research_log))
    return state

def nextera_researcher(state: State, logger: Logger) -> State:
    logger.info("researching Nextera energy...")
    research_log = research(nextera_energy_researcher_system)
    state["researches"]["energy"]["nextera"] = research_log
    state["messages"].append(AIMessage(content=research_log))
    return state
