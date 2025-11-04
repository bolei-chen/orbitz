from langchain.messages import AnyMessage
from typing_extensions import TypedDict, Annotated
import operator


class State(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]
    researched: Annotated[list[str], operator.add]
    summary: str
    advice: str


def new_state() -> State:
    state = State()
    state["messages"] = [] 
    state["researched"] = []
    state["summary"] = ""
    state["advice"] = ""
    return state