"""
Command-line entrypoint for running the Market News Advisor pipeline.
"""

from __future__ import annotations

import argparse
from textwrap import dedent

from market_news_advisor.graph import MNA

DEFAULT_QUERY = dedent(
    """\
    Tell me about the recent news and how it affects the financial market.
    """
).strip()


def run_briefing(query: str, user_id: str) -> str:
    """
    Execute the briefing flow for the provided query and return the combined report.
    """
    mna = MNA()
    state = mna.forward(query, user_id)
    summary = state.get("summary") or ""
    advice = state.get("advice") or ""
    separator = "\n" + "-" * 100 + "\n" if summary and advice else ""
    content = f"{summary}{separator}{advice}".strip()
    return content


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the Market News Advisor pipeline and print the latest summary + advice."
    )
    parser.add_argument(
        "query",
        nargs="?",
        default=DEFAULT_QUERY,
        help="Custom research prompt. Defaults to a broad market update request.",
    )
    parser.add_argument(
        "-u",
        "--user",
        default="bolei",
        help="Thread identifier to scope conversation history (default: %(default)s).",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    content = run_briefing(query=args.query, user_id=args.user)
    if content:
        print(content)


if __name__ == "__main__":
    main()