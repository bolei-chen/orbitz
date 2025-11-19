from market_news_advisor.agents.state import State
from logging import Logger
import os
from datetime import datetime

OUTPUT_PATH = os.getenv("OUTPUT_PATH")

def local_store(state: State, logger: Logger) -> State:
    logger.info("local storing...")
    path = os.path.join(OUTPUT_PATH, "mna_" + datetime.now().strftime("%Y-%m-%d") + ".log")
    with open(path, "w") as f:
        f.write(state["summary"])
        f.write("\n" + "-" * 100 + "\n")
        f.write(state["advice"])
    return state