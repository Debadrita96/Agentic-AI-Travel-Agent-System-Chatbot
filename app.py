import streamlit as st
from agent_system import TravelAgent

st.title("Travel AI Support Agent")

agent = TravelAgent()

user_input = st.text_input("Enter your query:")

mode = st.selectbox("Mode", ["baseline", "smart"])

use_retrieval = st.checkbox("Use Retrieval")

if st.button("Run"):
    if mode == "baseline":
        result = agent.baseline_respond(user_input)
    else:
        result = agent.smart_respond(user_input, use_retrieval)

    st.write(result["answer"])
