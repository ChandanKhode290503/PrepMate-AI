import streamlit as st
st.title("My  First Web Application")

fname = st.text_input("Enter your First Name")
lname = st.text_input("Enter your Last Name")

if st.button("submit"):
    st.write(fname)
    st.write(lname)
