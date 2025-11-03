"""Graph wiring for the market_news_advisor agents."""


import os

from langgraph.graph import END, START, StateGraph
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver

from market_news_advisor.agents.advicer.node import advicer
from market_news_advisor.agents.filter_dedupe.node import filter_dedupe
from market_news_advisor.agents.formatter.node import formatter
from market_news_advisor.agents.researchers.ai.node import ai_researcher
from market_news_advisor.agents.researchers.markets.node import markets_researcher
from market_news_advisor.agents.state import State, new_state
from market_news_advisor.agents.summarizer.node import summarizer

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class MNA:
    def __init__(self, model: str = "gpt-4.1-mini") -> None:
        self.llm = ChatOpenAI(
            model=model,
            api_key=OPENAI_API_KEY,
            temperature=0.0,
        )
        self.checkpointer = MemorySaver()
        self.graph = self._build_graph()


    def _build_graph(self):
        graph = StateGraph(State)

        graph.add_node("ai_researcher", ai_researcher)
        graph.add_node("markets_researcher", markets_researcher)
        graph.add_node("filter_dedupe", filter_dedupe)
        graph.add_node("summarizer", summarizer)
        graph.add_node("formatter", formatter)
        graph.add_node("advicer", lambda state: advicer(state, self.llm))

        graph.add_edge(START, "ai_researcher")

        graph.add_edge("ai_researcher", "markets_researcher")
        graph.add_edge("markets_researcher", "filter_dedupe")
        graph.add_edge("filter_dedupe", "summarizer")
        graph.add_edge("summarizer", "formatter")
        graph.add_edge("formatter", "advicer")
        graph.add_edge("advicer", END)

        return graph.compile(self.checkpointer)


    def forward(self, input: str, id: str) -> State:
        config = {"configurable": {"thread_id": "123"}}
        state = new_state()
        state["messages"].append(HumanMessage(content=input))
        end_state = self.graph.invoke(state, config)
        return end_state["messages"][-1].content

__all__ = ["MNA"]

