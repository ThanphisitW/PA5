import streamlit as st
import openai
import json
import pandas as pd

user_api_key = st.sidebar.text_input("OpenAPI API key", type="password")

client = openai.OpenAI(api_key=user_api_key)
prompt = """Act as an Akinator. You will received a clue from player and your job is to guess the character or person that player think of.
You will first ask the player "Is your character a real person?", then you will start to guess the character based on the player's answer.
"""

st.title("Character Guessing Game")
st.markdown("Please remind that the AI model is based on the information till 2021.")

user_input = st.text_input("Please answer yes or no", 'yes')
submit_button = st.button("Submit")

messages_so_far = [
    {"role": "system", "content": prompt},
]

if submit_button:
    messages_so_far.append({'role': 'user', 'content': user_input})
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages_so_far
    )
    # Extract the message content from the AI's response
    ai_response_text = response.choices[0].message.content

    # Print the AI's response
    st.markdown('**AI response:**')
    st.write(ai_response_text)

    # Add the AI's response to the conversation history
    messages_so_far.append({'role': 'assistant', 'content': ai_response_text})