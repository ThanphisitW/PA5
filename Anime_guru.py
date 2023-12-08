import streamlit as st
import openai
import json
import pandas as pd

user_api_key = st.sidebar.text_input("OpenAPI API key", type="password")

client = openai.OpenAI(api_key=user_api_key)
prompt = """Act as an Anime Guru. You will received user's preferences and requirements,
your job is to recommend the anime that match those preferences and requirements.
Give the user at least 7 suggestions.
List the suggestions in a JSON array. one suggestion per line.
Each suggestion should have 4 fields:
- title: the title of the anime (both English and Japanese)
- genres: genres of the anime
- year: the year the anime was released
- description: a short description of the anime
"""

st.title("Anime Guru")
st.markdown("Please remind that the AI model is based on the information till 2021.")
user_input = st.text_input("Tell me your preferences and requirements", 'I want to watch an anime that is funny and has a lot of action.')

if st.button('Submit'):
    messages_so_far = [
        {"role": "system", "content": prompt},
        {'role': 'user', 'content': user_input},
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages_so_far
    )
    # Show the response from the AI in a box
    st.markdown('**AI response:**')
    suggestion_dictionary = response.choices[0].message.content


    sd = json.loads(suggestion_dictionary)

    print (sd)
    suggestion_df = pd.DataFrame.from_dict(sd)
    print(suggestion_df)
    st.table(suggestion_df)