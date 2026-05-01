import streamlit as st
from agent_system import TravelAgent

st.set_page_config(page_title="Travel AI Agent", layout="centered")

st.title("✈️ Travel AI Support Agent")

# Create agent
agent = TravelAgent()

# Input
query = st.text_input("Enter your travel query:")

# Options in columns
col1, col2 = st.columns(2)

with col1:
    mode = st.selectbox("Mode", ["baseline", "smart"])

with col2:
    use_retrieval = st.checkbox("Use Retrieval")

# Run button
if st.button("Run Agent"):
    if query.strip() == "":
        st.warning("Please enter a query.")
    else:
        if mode == "baseline":
            result = agent.baseline_respond(query)
        else:
            result = agent.smart_respond(query, use_retrieval)

        st.subheader("Response:")
        st.write(result["answer"])

