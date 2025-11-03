from market_news_advisor.agents.state import State
from market_news_advisor.agents.filter_dedupe.prompt import filter_dedupe_system


def filter_dedupe(state: State) -> State:
    return {"messages": []}

