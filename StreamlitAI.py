
import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage, HumanMessage

st.title("PrepMate AI Agent")

model = ChatOllama(
    model="qwen3:1.7b",
    temperature=0,
    thinking=False
)

system_message = SystemMessage(
    content="""
You are an expert AI interviewer.

Instructions:

1. Read the user's input to determine the interview type.
2. If the user mentions "HR", conduct only an HR interview.
3. If the user mentions "Technical", conduct only a Technical interview.
4. Generate exactly 5 interview questions relevant to the requested interview type.
5. Ask five questions with their answers at a time.

Do not mix HR and Technical questions unless the user explicitly requests a mixed interview.
"""
)

if "chat" not in st.session_state:
    st.session_state.chat = []

for role, message in st.session_state.chat:
    st.chat_message(role).write(message)

question = st.chat_input("Ask Your Questions:")

if question:
    st.chat_message("user").write(question)

    human_message = HumanMessage(content=question)

    response = model.invoke([
        system_message,
        human_message
    ])

    st.chat_message("assistant").write(response.content)

    st.session_state.chat.append(("user", question))
    st.session_state.chat.append(("assistant", response.content))

