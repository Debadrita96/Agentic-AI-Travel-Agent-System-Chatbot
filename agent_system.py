
from openai import OpenAI
import os

client = OpenAI(
    base_url="https://openai.vocareum.com/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)

class TravelAgent:

    def baseline_respond(self, query):
        q = query.lower()
        if "refund" in q:
            return {"answer": "Refund depends on ticket type."}
        elif "baggage" in q:
            return {"answer": "Baggage depends on airline."}
        return {"answer": "Please provide more details."}

    def smart_respond(self, query, use_retrieval=False):
        prompt = f"""
        You are a travel assistant.
        Answer clearly and safely.

        Question: {query}
        """
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )
        return {"answer": response.choices[0].message.content}
