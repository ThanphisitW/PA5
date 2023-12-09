import streamlit as st
import openai
import json
import pandas as pd

user_api_key = st.sidebar.text_input("OpenAPI API key", type="password")

client = openai.OpenAI(api_key=user_api_key)
prompt = """Act as an Anime Guru. You will receive users' preferences and requirements,
and your job is to recommend anime that match those preferences and requirements.
If the user is unsure or does not have any specific preferences, recommend 5 random anime from different genres.
If you cannot find 5 anime that match the user's preferences and requirements, you can provide less than 5 suggestions.
Always provide the user with at least 5 suggestions. List the suggestions in a JSON array. one suggestion per line.
Each suggestion should include the following 5 fields:
- ENG: the title of the anime in English
- JPN: the title of the anime in Japanese (日本語)
- genre: genres of the anime
- year: the year the anime was released
- description: a short description of the anime
"""

st.title("Anime Guru :nerd_face:")
user_input = st.text_input("What kinds of anime are you into or looking to explore?", 'I want to watch an anime that is funny and has a lot of action.')
st.markdown("Please keep in mind that the AI model is built on data available up to the year 2021.")

st.title("Uncertain about what to watch or new to anime? :thinking_face:")
st.markdown("Click the button below to receive recommendations for five randomly selected anime that are suitable for beginners.")

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