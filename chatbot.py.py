#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import requests

# Replace with your Gemini API URL and Key
GEMINI_API_URL = "https://api.gemini.com/v1/chat"
API_KEY = "AIzaSyD2twuzUQBL5RCd9JsIgiBEhPaoDo5NB7M"

# Function to send a message to the Gemini API
def send_message_to_gemini(user_input):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "message": user_input,
    }
    try:
        response = requests.post(GEMINI_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        return response.json().get("response", "Sorry, I didn't understand that.")
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Streamlit Interface
st.title("Simple Chatbot")
st.write("Chat with me using the Gemini API!")

# Input Box for User Input
user_input = st.text_input("You:", placeholder="Type your message here...")

if user_input:
    # Process the input and display the response
    with st.spinner("Thinking..."):
        bot_response = send_message_to_gemini(user_input)
    st.write(f"Bot: {bot_response}")

# Add a footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit and Gemini API.")

