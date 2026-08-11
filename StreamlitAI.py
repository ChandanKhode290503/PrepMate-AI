import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
import time 


st.title("PrepMate AI Agent")
model = ChatOllama(
    model = "qwen3:1.7b",
    temperature=0,
    thinking = False
)

message = [
    SystemMessage(
        content=""" You are an expert AI interviewer.

Instructions:
1. Read the user's input to determine the interview type.
2. If the user mentions "HR", conduct only an HR interview.
3. If the user mentions "Technical", conduct only a Technical interview.
4. Generate exactly 5 interview questions relevant to the requested interview type.
5. Ask five question with their answer at a time 

Do not mix HR and Technical questions unless the user explicitly requests a mixed interview."""
    )
]
question = st.chat_input("Ask Your Questions:")
if question:
    st.chat_message("user").write(question)
    message.append( HumanMessage(content=question) )

    response = model.invoke(message)
    st.chat_message("assistant").write(response.content)