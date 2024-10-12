import streamlit as st
import google.generativeai as genai

st.title("🕵🏻‍♂️ My Chatbot app")
st.subheader("Conversation")
st.write("DEMO FIRST APP.")


gemini_api_key = st.text_input("Gemini API Key: ", placeholder="Type your API Key here ...")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message("user"):
        st.markdown(message)

if prompt := st.chat_input("Type your message here ..."):
    st.session_state.chat_history.append(prompt)
    st.chat_message("user").markdown(prompt)

st.write(st.session_state.chat_history)

# if user_input :=  st.text_input(label="You: ", placeholder="Type your message here..."):
#     st.session_state.chat_history.append(user_input) 









