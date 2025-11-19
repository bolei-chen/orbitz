"""Biotech researcher node leveraging the shared deep-research helper."""

from langchain_core.messages import AIMessage

from market_news_advisor.agents.researchers.research import research
from market_news_advisor.agents.state import State

from .prompt import amgen_biotech_researcher_system, vertex_biotech_researcher_system, gilead_biotech_researcher_system
from logging import Logger

def amgen_researcher(state: State, logger: Logger) -> State:
    logger.info("researching Amgen biotech...")
    research_log = research(amgen_biotech_researcher_system)
    state["researches"]["biotech"]["amgen"] = research_log
    state["messages"].append(AIMessage(content=research_log))
    return state 

def vertex_researcher(state: State, logger: Logger) -> State:
    logger.info("researching Vertex biotech...")
    research_log = research(vertex_biotech_researcher_system)
    state["researches"]["biotech"]["vertex"] = research_log
    state["messages"].append(AIMessage(content=research_log))
    return state

def gilead_researcher(state: State, logger: Logger) -> State:
    logger.info("researching Gilead biotech...")
    research_log = research(gilead_biotech_researcher_system)
    state["researches"]["biotech"]["gilead"] = research_log
    state["messages"].append(AIMessage(content=research_log))
    return state


