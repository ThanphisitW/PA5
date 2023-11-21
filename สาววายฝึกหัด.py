import streamlit as st
import openai
import json
import pandas as pd

user_api_key = st.sidebar.text_input("OpenAPI API key", type="password")

client = openai.OpenAI(api_key=user_api_key)
prompt = """
        Act as a BL romance fiction writer. you will receive names of 2 male characters and a short description of the story
        you will write a long story about the 2 characters and their relationship. It required to be at least 3 chapters long.
        """

st.title("สาววายฝึกหัด")
top_name = st.text_area('โปรดกรอกชื่อตัวละคร:rainbow[ฝ่ารุก]:smirk: (ภาษาอังกฤษ)', 'ตัวอย่างเช่น Top Win')
bottom_name = st.text_area('โปรดกรอกชื่อตัวละคร:rainbow[ฝ่ายรับ]:wink: (ภาษาอังกฤษ)', 'ตัวอย่างเช่น Mild Fluke')
story = st.text_area('โปรดกรอกสตอรี่คร่าว ๆ ที่ต้องการ:flushed: (ภาษาอังกฤษ)', """
                     ตัวอย่างเช่น
                     In the cozy town of Evergreen Falls, there are two boys named Alex and Riley.
                     Alex loves reading books and taking pictures, while Riley is a cool skateboarder.
                     They become good friends even though they're different.
                     
                     As they spend time together, Alex and Riley realize they have special feelings for each other.
                     But it's not always easy because some people in the town don't understand their love.
                     
                     In the story, you'll see Alex and Riley facing challenges and discovering who they really are.
                     The town of Evergreen Falls becomes the backdrop for their sweet and sometimes tough journey.
                     It's a simple, heartwarming tale about friendship, love, and finding the courage to be yourself, no matter what others think.
                     """)
submit_button = st.button('Submit')

if submit_button:
    message = [
        {"role": "system", "content": prompt},
        {'role': 'user', 'content': [top_name, bottom_name, story]}
        ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=message
    )
    st.markdown('AI response:')
    suggestion_dictionary = response.choices[0].message.content

    sd = json.loads(suggestion_dictionary)

    print(sd)
    suggestion_df = pd.DataFrame.from_dict(sd)
    print(suggestion_df)
    st.table(suggestion_df)