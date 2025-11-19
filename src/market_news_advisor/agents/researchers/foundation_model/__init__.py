"""Foundation model researcher package."""

from .node import (
    openai_researcher,
    anthropic_researcher,
    deepmind_researcher,
)

__all__ = [
    "openai_researcher",
    "anthropic_researcher",
    "deepmind_researcher",
]