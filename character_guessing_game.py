import streamlit as st
import openai
import json
import pandas as pd

user_api_key = st.sidebar.text_input("OpenAPI API key", type="password")

client = openai.OpenAI(api_key=user_api_key)

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

# prompt = """
#         Act as a Akinator (character guessing game). The player will start with a short description about their character.
#         You need to guess the character by asking questions.
#         """

# st.title("Character Guessing Game")
# st.text_area("Please give a short description about your character", 'He is blonde and has spiky hair')

# """
# Character Guessing Game
# pseudocode
# 1. ให้มี initial guess ของ chatGPT ว่า Is your character a real person?
# 2. จากนั้นก็ให้ user ตอบ โดยเขียนบอกไว้ด้วยว่าให้ตอบ yes หรือ no
#     แต่ถ้าตอบไม่ได้เยอะ ๆ แล้วคำถาามเริ่มซ้ำ แบบแค่เปลี่ยน noun ก็บอก user ให้ give a hint หน่อย
#     + บอกว่า database แชทจีมีแค่ถึงปี 2021 ด้วย
# 3. จำกัดโควตาการทายของแชทจีอยู่ที่ 40 ครั้ง ถ้าเกินให้ยอมแพ้ เฉลยให้หน่อย

# additional functions
# - ให้ user กด space เพื่อส่งข้อความเหมือนแชทแทนที่จะเป็น button
# - ให้เลือกภาษาที่จะใช้ทายได้
# - เปลี่ยนโหมด dark / light (ถ้า streamlit ไม่มีก็ใช้ภาษาอื่นแทน)
# - ร้องขอ additional points จากอาจารย์
# """