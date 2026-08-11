import streamlit as st
st.title("AI Assistent")
question = st.chat_input("Ask Your Questions:")

if question:
    st.chat_message("user").write(question)
    answer = "this is the response from AI Agent"

    st.chat_message("assistant").write(answer)