#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import requests

# Hugging Face API URL for LLaMA model (adjust based on the specific model you're using)
MODEL_URL = "https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct"  # Adjust model URL based on LLaMA version
API_KEY = "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"  # Replace with your Hugging Face API key

# Function to send a message to the Hugging Face LLaMA model
def query_llama(message):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "inputs": message,
        "options": {"use_cache": False}  # Optional: can disable cache if needed
    }
    try:
        response = requests.post(MODEL_URL, headers=headers, json=payload)
        response.raise_for_status()  # Raise an error if the request fails
        return response.json()[0]["generated_text"]
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Streamlit Interface
st.title("Chat with LLaMA Bot!")
st.write("Ask me anything, and I'll respond using the LLaMA model hosted on Hugging Face.")

# Input Box for User Input
user_input = st.text_input("You:", placeholder="Type your message here...")

if user_input:
    with st.spinner("Thinking..."):
        bot_response = query_llama(user_input)
    st.write(f"Bot: {bot_response}")

# Add a footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit and LLaMA model via Hugging Face.")


