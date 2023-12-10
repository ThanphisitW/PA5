import streamlit as st
#setting page config
st.set_page_config(
    page_title="Animagic",
    page_icon=":thought_balloon:",
    layout="wide",
    initial_sidebar_state="expanded",
)

import openai
import json
import pandas as pd

#styling with css
with open("streamlit.css") as f:
    st.markdown("""<style>{}</style>""".format(f.read()), unsafe_allow_html=True)

#sidebar
user_api_key = st.sidebar.text_input("OpenAPI API key", type="password")
client = openai.OpenAI(api_key=user_api_key)

#Main
col1, col2 = st.columns(2)
with col1:
    st.title('Welcome to Animagic! :partying_face:')
    st.markdown("""Meet Animagic, your anime sidekick with a touch of AI magic! Whether you're an anime pro or just getting started, Animagic's here for you. Let's make your anime journey as delightful as discovering a hidden gem :star2:""")
with col2:
    st.markdown("""
    <style>
        .my-image {
            width: 100%;
            height: auto;
            border-radius: 75%;
        }
    </style>
    """, unsafe_allow_html=True)
    st.markdown("""<img src="src/ezgif.com-gif-maker.gif" class="my-image">""", unsafe_allow_html=True)

#Animagic
prompt = """Act as an Anime Guru. You will receive users' preferences and requirements,
and your job is to recommend anime that match those preferences and requirements.
If you cannot find 5 anime that match the user's preferences and requirements, you can provide less than 5 suggestions.
Always provide the user with at least 5 suggestions. List the suggestions in a JSON array. one suggestion per line.
Each suggestion should include the following 5 fields:
- ENG: the title of the anime in English
- JPN: the title of the anime in Japanese (日本語)
- genre: genres of the anime
- year: the year the anime was released
- description: a short description of the anime
"""

user_input = st.text_input("What kinds of anime are you into or looking to explore? (Please keep in mind that the AI model is built on data available up to the year 2021.)", 'I want anime that reflects everyday life and the struggles of ordinary people. Something that feels relatable.')

if st.button('Submit'):
    messages_so_far = [
        {"role": "system", "content": prompt},
        {'role': 'user', 'content': user_input},
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages_so_far
    )
    st.markdown('**AI response:**')
    suggestion_dictionary = response.choices[0].message.content

    sd = json.loads(suggestion_dictionary)

    print (sd)
    suggestion_df = pd.DataFrame.from_dict(sd)
    suggestion_df_styled = suggestion_df.style.set_properties(**{
        'background-color': 'black',
        'color': 'lawngreen',
        'border-color': 'white'
    })
    print(suggestion_df_styled)
    st.table(suggestion_df_styled)

#New to anime?
fixed_user_input = "Recommend me 5 random anime from different genres"
for_newbies_prompt = """Act as an Anime Guru. The user is unsure or does not have any specific preferences,
recommend them 5 random anime from different genres. 3 of the mainstream anime and 2 of the non-mainstream anime.
List the suggestions in a JSON array. one suggestion per line.
Each suggestion should include the following 5 fields:
- ENG: the title of the anime in English
- JPN: the title of the anime in Japanese (日本語)
- genre: genres of the anime
- year: the year the anime was released
- description: a short description of the anime
"""

st.title("New to anime? :thinking_face:")
st.markdown("Click the button below to receive recommendations for anime that might interest you.")

if st.button('Help!'):
    messages_so_far = [
        {"role": "system", "content": for_newbies_prompt},
        {'role': 'user', 'content': fixed_user_input},
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages_so_far
    )
    st.markdown('**Here are some anime you might enjoy!:**')
    suggestion_dictionary = response.choices[0].message.content

    sd = json.loads(suggestion_dictionary)

    print (sd)
    suggestion_df = pd.DataFrame.from_dict(sd)
    suggestion_df_styled = suggestion_df.style.set_properties(**{
        'background-color': 'black',
        'color': 'lawngreen',
        'border-color': 'white'
    })
    print(suggestion_df_styled)
    st.table(suggestion_df_styled)