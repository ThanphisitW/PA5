import streamlit as st
import openai
import json
import pandas as pd

user_api_key = st.sidebar.text_input("OpenAPI API key", type="password")

client = openai.OpenAI(api_key=user_api_key)
prompt = """Act as an Akinator. You will received a clue from player and your job is to guess the character or person that player think of.
You will first ask the player "Is your character a real person", then you will start to guess the character based on the player's past answer.
Do not ask the same question or repeated queestion.
"""

st.title("Character Guessing Game")
st.markdown("Please remind that the AI model is based on the information till 2021.")

messages_so_far = [
    {"role": "system", "content": prompt},
]

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=messages_so_far,
)

st.markdown("**AI**")
if response.choices[0].text == "Is your character a real person":
    pass
else:
    st.write(response.choices[0].message.content)

user_input = st.text_input("Player's Answer")
messages_so_far.append({"role": "user", "content": user_input})

# Clear session state if the user wants to play again
if st.button("Play Again"):
    st.session_state.asked_real_person = False