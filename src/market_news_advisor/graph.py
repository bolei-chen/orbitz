"""Graph wiring for the market_news_advisor agents."""


import os

from langgraph.graph import END, START, StateGraph
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.checkpoint.memory import MemorySaver
import logging
logging.basicConfig(level=logging.INFO)

from market_news_advisor.agents.advicer.node import advicer
from market_news_advisor.agents.filter_dedupe.node import filter_dedupe
from market_news_advisor.agents.researchers.foundation_model.node import foundation_model_researcher
from market_news_advisor.agents.researchers.faang.node import faang_researcher
from market_news_advisor.agents.researchers.chips.node import chips_researcher
from market_news_advisor.agents.researchers.energy.node import energy_researcher
from market_news_advisor.agents.researchers.fed_macro.node import fed_macro_researcher
from market_news_advisor.agents.researchers.biotech.node import biotech_researcher
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
        self.researchers = {
            "foundation_model": foundation_model_researcher,
            "faang": faang_researcher,
            "chips": chips_researcher,
            "energy": energy_researcher,
            "fed_macro": fed_macro_researcher,
            "biotech": biotech_researcher,
        }
        self.logger = logging.getLogger(__name__)
        self.checkpointer = MemorySaver()
        self.graph = self._build_graph()


    def _build_graph(self):
        graph = StateGraph(State)

        # graph.add_node("research_checker", lambda state: research_checker(state, self.logger))
        prev = START
        for n, f in self.researchers.items():
            graph.add_node(n, lambda state, f=f, n=n: f(state, self.logger))
            graph.add_edge(prev, n)
            prev = n
        graph.add_node("summarizer", lambda state: summarizer(state, self.llm, self.logger))
        graph.add_node("advicer", lambda state: advicer(state, self.llm, self.logger))

        # graph.add_node("filter_dedupe", filter_dedupe)
        graph.add_edge(prev, "summarizer")

        # graph.add_edge("research_checker", "summarizer")
        # graph.add_edge("research_checker", "filter_dedupe")
        # graph.add_edge("filter_dedupe", "summarizer")
        graph.add_edge("summarizer", "advicer")
        graph.add_edge("advicer", END)

        return graph.compile(self.checkpointer)


    def forward(self, input: str, id: str) -> State:
        config = {"configurable": {"thread_id": id}}
        state = new_state()
        state["messages"].append(HumanMessage(content=input))
        end_state = self.graph.invoke(state, config)
        return end_state

__all__ = ["MNA"]

