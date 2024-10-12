import streamlit as st
import google.generativeai as genai

st.title("🕵🏻‍♂️ My Chatbot app")
st.subheader("Conversation")
st.write("DEMO FIRST APP.")


gemini_api_key = st.text_input(
    "Gemini API Key: ", placeholder="Type your API Key here ...",
    type='password'
)

if gemini_api_key:
    try:
        genai.configure(api_key=gemini_api_key)
        model = genai.GenerativeModel("gemini-1.0-pro")
        st.success("Gemini API Key successfully configured.")
    except Exception as e:
        st.error(f"An error occurred while setting up the Gemini model: {e}")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for role, message in st.session_state.chat_history:
    st.chat_message(role).markdown(message)

if prompt := st.chat_input("Type your message here ..."):
    st.session_state.chat_history.append(("user", prompt))
    st.chat_message("user").markdown(prompt)

    if model:
        try:
            response = model.generate_content(prompt)
            bot_response = response.text

            st.session_state.chat_history.append(("assistant", bot_response))
            st.chat_message("assistant").markdown(bot_response)

        except Exception as e:
            st.error(f"An error occurred while generating the response: {e}")
        


# if "chat_history" not in st.session_state:
#     st.session_state.chat_history = []

# for message in st.session_state.chat_history:
#     with st.chat_message("user"):
#         st.markdown(message)

# if prompt := st.chat_input("Type your message here ..."):
#     st.session_state.chat_history.append(prompt)
#     st.chat_message("user").markdown(prompt)

# st.write(st.session_state.chat_history)

# if user_input :=  st.text_input(label="You: ", placeholder="Type your message here..."):
#     st.session_state.chat_history.append(user_input) 









