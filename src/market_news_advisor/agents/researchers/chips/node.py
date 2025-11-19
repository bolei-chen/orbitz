"""Execution logic for the AI chips deep-research agent using OpenAI web search."""

from market_news_advisor.agents.state import State
from market_news_advisor.agents.researchers.research import research
from .prompt import amd_chips_researcher_system, nvidia_chips_researcher_system, major_chips_researcher_system
from langchain_core.messages import AIMessage
from logging import Logger

def amd_researcher(state: State, logger: Logger) -> State:
    logger.info("researching AMD computer chips...")
    research_log = research(amd_chips_researcher_system)
    state["researches"]["chips"]["amd"] = research_log
    state["messages"].append(AIMessage(content=research_log))
    return state 

def nvidia_researcher(state: State, logger: Logger) -> State:
    logger.info("researching NVIDIA computer chips...")
    research_log = research(nvidia_chips_researcher_system)
    state["researches"]["chips"]["nvidia"] = research_log
    state["messages"].append(AIMessage(content=research_log))
    return state

def major_chips_researcher(state: State, logger: Logger) -> State:
    logger.info("researching major computer chips...")
    research_log = research(major_chips_researcher_system)
    state["researches"]["chips"]["majors"] = research_log
    state["messages"].append(AIMessage(content=research_log))
    return state