"""Graph wiring for the market_news_advisor agents."""


import os

from langgraph.graph import END, START, StateGraph
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
import logging
logging.basicConfig(level=logging.INFO)

from market_news_advisor.agents.advicer.node import advicer
from market_news_advisor.agents.researchers.foundation_model.node import (
    openai_researcher, anthropic_researcher, deepmind_researcher,
)
from market_news_advisor.agents.researchers.tech.node import (
    microsoft_researcher, google_researcher, meta_researcher, tesla_researcher, palantir_researcher, apple_researcher, amazon_researcher,
)
from market_news_advisor.agents.researchers.energy.node import (
    exxon_researcher, chevron_researcher, nextera_researcher,
)
from market_news_advisor.agents.researchers.biotech.node import (
    amgen_researcher, gilead_researcher, vertex_researcher,
)
from market_news_advisor.agents.researchers.fed_macro.node import fed_macro_researcher
from market_news_advisor.agents.local_store.node import local_store
from market_news_advisor.agents.state import State, new_state
from market_news_advisor.agents.summarizer.node import summarizer

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OUTPUT_PATH = os.getenv("OUTPUT_PATH")

class MNA:
    def __init__(self, model: str = "gpt-4.1-mini") -> None:
        self.llm = ChatOpenAI(
            model=model,
            api_key=OPENAI_API_KEY,
            temperature=0.0,
        )
        self.researchers = {
            "foundation_model": {
                "openai": openai_researcher,
                "anthropic": anthropic_researcher,
                "deepmind": deepmind_researcher,
            },
            "tech": {
                "microsoft": microsoft_researcher,
                "google": google_researcher,
            },
            "energy": {
                "exxon": exxon_researcher,
                "chevron": chevron_researcher,
                "nextera": nextera_researcher,
            },
            "biotech": {
                "amgen": amgen_researcher,
                "gilead": gilead_researcher,
                "vertex": vertex_researcher,
            },
            "fed_macro": {
                "fed_macro": fed_macro_researcher,
            },
            "tech": {
                "microsoft": microsoft_researcher,
                "google": google_researcher,
                "meta": meta_researcher,
                "tesla": tesla_researcher,
                "palantir": palantir_researcher,
                "apple": apple_researcher,
                "amazon": amazon_researcher,
            },
        }
        self.logger = logging.getLogger(__name__)
        self.checkpointer = MemorySaver()
        self.graph = self._build_graph()

    def _build_graph(self):
        graph = StateGraph(State)

        prev = START
        for _, researchers in self.researchers.items():
            for n, f in researchers.items():
                graph.add_node(n, lambda state, f=f, n=n: f(state, self.logger))
                graph.add_edge(prev, n)
                prev = n
        graph.add_node("summarizer", lambda state: summarizer(state, self.llm, self.logger))
        graph.add_node("advicer", lambda state: advicer(state, self.llm, self.logger))
        graph.add_node("local_store", lambda state: local_store(state, self.logger))

        graph.add_edge(prev, "summarizer")
        graph.add_edge("summarizer", "advicer")
        graph.add_edge("advicer", "local_store")
        graph.add_edge("local_store", END)

        return graph.compile(self.checkpointer)


    def forward(self, input: str, id: str) -> State:
        config = {"configurable": {"thread_id": id}}
        state = new_state(output_path=OUTPUT_PATH)
        state["messages"].append(HumanMessage(content=input))
        end_state = self.graph.invoke(state, config)
        return end_state

__all__ = ["MNA"]

