from market_news_advisor.graph import MNA

mna = MNA()

me = "bolei"

query = """
Tell me about the recent news and how it affects the financial market.
"""

state = mna.forward(query, me)

print(state)