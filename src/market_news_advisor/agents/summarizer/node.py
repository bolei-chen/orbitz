from market_news_advisor.agents.state import State
from langchain_core.language_models import BaseLanguageModel
from langchain_core.messages import SystemMessage
from market_news_advisor.agents.summarizer.prompt import summarizer_system
from logging import Logger

def summarizer(state: State, llm: BaseLanguageModel, logger: Logger) -> State:
    logger.info("summarizing...")
    system_message = SystemMessage(content=summarizer_system.strip())
    response = llm.invoke([system_message, *state["messages"]])
    return {"messages": [response], "summary": response.content}

