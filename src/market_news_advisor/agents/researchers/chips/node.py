"""Execution logic for the AI chips deep-research agent using OpenAI web search."""

from market_news_advisor.agents.state import State
from market_news_advisor.agents.researchers.research import research
from .prompt import chips_researcher_system
from langchain_core.messages import AIMessage


def chips_researcher(state: State) -> State:
    research_log = research(chips_researcher_system)
    return {"messages": [AIMessage(content=research_log)]}