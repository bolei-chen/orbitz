from typing import Optional, Any
from langchain.messages import AnyMessage
from typing_extensions import TypedDict


class State(TypedDict):
    messages: list[AnyMessage]
    researches: dict[str, Any]
    summary: Optional[str]
    advice: Optional[str]
    output_path: Optional[str]



def new_state(output_path: Optional[str]) -> State:
    state = State()
    state["messages"] = []
    state["summary"] = None
    state["advice"] = None
    state["output_path"] = output_path
    state["researches"] = {
        "foundation_model": {},
        "tech": {},
        "energy": {},
        "biotech": {},
        "fed_macro": {},
        "chips": {},
    }
    return state