
from agent_system import baseline_agent, llm_agent

queries = [
    "Can I get refund?",
    "Baggage limit?",
    "Cancel my ticket now"
]

for q in queries:
    print("\nQ:", q)
    print("Baseline:", baseline_agent(q))
    print("LLM:", llm_agent(q))
