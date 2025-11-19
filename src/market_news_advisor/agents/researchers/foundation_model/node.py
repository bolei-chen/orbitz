"""Foundation model researcher node leveraging shared helper."""

from langchain_core.messages import AIMessage

from market_news_advisor.agents.state import State
from market_news_advisor.agents.researchers.research import research
from .prompt import openai_foundation_model_researcher_system, anthropic_foundation_model_researcher_system, deepmind_foundation_model_researcher_system
from logging import Logger


def openai_researcher(state: State, logger: Logger) -> State:
    logger.info("researching OpenAI foundation model...")
    research_log = research(openai_foundation_model_researcher_system)
    state["messages"].append(AIMessage(content=research_log))
    state["researches"]["foundation_model"]["openai"] = research_log
    return state


def anthropic_researcher(state: State, logger: Logger) -> State:
    logger.info("researching Anthropic foundation model...")
    research_log = research(anthropic_foundation_model_researcher_system)
    state["messages"].append(AIMessage(content=research_log))
    state["researches"]["foundation_model"]["anthropic"] = research_log
    return state

def deepmind_researcher(state: State, logger: Logger) -> State:
    logger.info("researching DeepMind foundation model...")
    research_log = research(deepmind_foundation_model_researcher_system)
    state["messages"].append(AIMessage(content=research_log))
    state["researches"]["foundation_model"]["deepmind"] = research_log
    return state