from langchain.messages import AnyMessage
from typing_extensions import TypedDict, Annotated
import operator


class State(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]


def new_state() -> State:
    state = State()
    state["messages"] = [] 
    return state