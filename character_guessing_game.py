import streamlit as st
import openai
import json
import pandas as pd

user_api_key = st.sidebar.text_input("OpenAPI API key", type="password")

client = openai.OpenAI(api_key=user_api_key)
prompt = """Act as a Akinator. You will received a clue from player and your job is to guess the character or person that player think of.
You will first ask the player if their character is a real person or fictional character. Then, you will guess based on player's answer.
"""

st.title("Character Guessing Game")
# Initial message from chatGPT
st.write("Is your character a real person?")
description = st.text_input("Please give a short description about your character", 'He is blonde and has spiky hair')
submit_button = st.button("Submit")

if submit_button:
    message = [
        {"role": "system", "content": "Is your character a real person?"},
        {'role': 'user', 'content': description}
    ]
    for i in range(40):  # Limit to 40 guesses
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=message
        )
        suggestion_dictionary = response.choices[0].message.content
        sd = json.loads(suggestion_dictionary)
        st.write(f'AI Guess {i+1}: {sd["content"]}')
        user_response = st.text_input("Please respond with yes or no, or give a hint if the question is repetitive.")
        message.append({'role': 'user', 'content': user_response})

"""
Murdurer guessing game
- Based on true story
- AI will give a brief story of murder case, then the user need to guess who is the real murderer
- After finished guessing, AI will give a full story of the murder case with a like for people who want to continue reading

Additional functions
- ให้ user กด space เพื่อส่งข้อความเหมือนแชทแทนที่จะเป็น button
- ให้เลือกภาษาที่จะใช้ทายได้
- เปลี่ยนโหมด dark / light (ถ้า streamlit ไม่มีก็ใช้ภาษาอื่นแทน)
- ร้องขอ additional points จากอาจารย์
"""