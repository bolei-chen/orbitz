"""Foundation model researcher node leveraging shared helper."""

from langchain_core.messages import AIMessage

from market_news_advisor.agents.state import State
from market_news_advisor.agents.researchers.research import research
from .prompt import foundation_model_researcher_system
from logging import Logger


def foundation_model_researcher(state: State, logger: Logger) -> State:
    logger.info("researching foundation model providers...")
    research_log = research(foundation_model_researcher_system)

    return {"messages": [AIMessage(content=research_log)],
            "researched": ["foundation_model"]}


