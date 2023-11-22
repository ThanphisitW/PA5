import streamlit as st
import openai
import json
import pandas as pd

user_api_key = st.sidebar.text_input("OpenAPI API key", type="password")

client = openai.OpenAI(api_key=user_api_key)
prompt = """
        Act as a Akinator (character guessing game). The player will start with a short description about their character.
        You need to guess the character by asking questions. The player will answer yes or no.
        """

st.title("Character Guessing Game")
st.text_area("Please give a short description about your character", 'He is blonde and has spiky hair')

# ถ้าหากตอบไม่ได้ครบ ... ครั้ง ให้ยอมแพ้
st.write("โปรดตอบแบบ บลาๆๆ หากตอบไม่ได้ซักทีก็ให้ hint หน่อย โปรดจำว่าดาต้าเบสมีแค่ถึงปี 202??")