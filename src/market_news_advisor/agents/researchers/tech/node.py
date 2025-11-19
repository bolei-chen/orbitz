"""FAANG researcher node leveraging the shared research helper."""

from langchain_core.messages import AIMessage

from market_news_advisor.agents.researchers.research import research
from market_news_advisor.agents.state import State

from .prompt import microsoft_tech_researcher_system, google_tech_researcher_system, meta_tech_researcher_system, tesla_tech_researcher_system, palantir_tech_researcher_system, apple_tech_researcher_system, amazon_tech_researcher_system
from logging import Logger


def microsoft_researcher(state: State, logger: Logger) -> State:
    logger.info("researching Microsoft...")
    research_log = research(microsoft_tech_researcher_system)
    state["messages"].append(AIMessage(content=research_log))
    state["researches"]["faang"] = research_log
    return state

def google_researcher(state: State, logger: Logger) -> State:
    logger.info("researching Google...")
    research_log = research(google_tech_researcher_system)
    state["messages"].append(AIMessage(content=research_log))
    state["researches"]["google"] = research_log
    return state

def meta_researcher(state: State, logger: Logger) -> State:
    logger.info("researching Meta...")
    research_log = research(meta_tech_researcher_system)
    state["messages"].append(AIMessage(content=research_log))
    state["researches"]["meta"] = research_log
    return state

def tesla_researcher(state: State, logger: Logger) -> State:
    logger.info("researching Tesla...")
    research_log = research(tesla_tech_researcher_system)
    state["messages"].append(AIMessage(content=research_log))
    state["researches"]["tesla"] = research_log
    return state

def palantir_researcher(state: State, logger: Logger) -> State:
    logger.info("researching Palantir...")
    research_log = research(palantir_tech_researcher_system)
    state["messages"].append(AIMessage(content=research_log))
    state["researches"]["palantir"] = research_log
    return state

def apple_researcher(state: State, logger: Logger) -> State:
    logger.info("researching Apple...")
    research_log = research(apple_tech_researcher_system)
    state["messages"].append(AIMessage(content=research_log))
    state["researches"]["apple"] = research_log
    return state

def amazon_researcher(state: State, logger: Logger) -> State:
    logger.info("researching Amazon...")
    research_log = research(amazon_tech_researcher_system)
    state["messages"].append(AIMessage(content=research_log))
    state["researches"]["amazon"] = research_log
    return state