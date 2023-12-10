import streamlit as st
#setting page config
st.set_page_config(
    page_title="Animagination",
    page_icon=":thought_balloon:",
    layout="wide",
    initial_sidebar_state="collapsed",
)

import openai
import json
import pandas as pd

#styling with css
with open("streamlit.css") as f:
    st.markdown("""
                <header class="showcase">
                    <div class="showcase-top">
                        <img src="https://i.ibb.co/r5krrdz/logo.png" alt="" />
                        <a href="#" class="btn btn-rounded">Sign In</a>
                    </div>
                    <div class="showcase-content">
                        <h1>See what's next</h1>
                        <p>Watch anywhere. Cancel Anytime</p>
                        <a href="#" class="btn btn-xl"
                            >Watch Free For 30 Days <i class="fas fa-chevron-right btn-icon"></i
                        ></a>
                    </div>
                </header>
                <section class="tabs">
                    <div class="container">
                        <div id="tab-1" class="tab-item tab-border">
                            <i class="fas fa-door-open fa-3x"></i>
                            <p class="hide-sm">Cancel at any time</p>
                        </div>
                        <div id="tab-2" class="tab-item">
                            <i class="fas fa-tablet-alt fa-3x"></i>
                            <p class="hide-sm">Watch anywhere</p>
                        </div>
                        <div id="tab-3" class="tab-item">
                            <i class="fas fa-tags fa-3x"></i>
                            <p class="hide-sm">Pick your price</p>
                        </div>
                    </div>
                </section>

                <section class="tab-content">
                    <div class="container">
                        <!-- Tab Content 1 -->
                        <div id="tab-1-content" class="tab-content-item show">
                            <div class="tab-1-content-inner">
                                <div>
                                    <p class="text-lg">
                                        If you decide Netflix isn't for you - no problem. No commitment.
                                        Cancel online anytime.
                                    </p>
                                    <a href="#" class="btn btn-lg">Watch Free For 30 Days</a>
                                </div>
                                <img src="https://i.ibb.co/J2xDJV7/tab-content-1.png" alt="" />
                            </div>
                        </div>

                        <!-- Tab Content 2 -->
                        <div id="tab-2-content" class="tab-content-item">
                            <div class="tab-2-content-top">
                                <p class="text-lg">
                                    Watch TV shows and movies anytime, anywhere — personalized for
                                    you.
                                </p>
                                <a href="#" class="btn btn-lg">Watch Free For 30 Days</a>
                            </div>
                            <div class="tab-2-content-bottom">
                                <div>
                                    <img src="https://i.ibb.co/DpdN7Gn/tab-content-2-1.png" alt="" />
                                    <p class="text-md">
                                        Watch on your TV
                                    </p>
                                    <p class="text-dark">
                                        Smart TVs, PlayStation, Xbox, Chromecast, Apple TV, Blu-ray
                                        players and more.
                                    </p>
                                </div>
                                <div>
                                    <img src="https://i.ibb.co/R3r1SPX/tab-content-2-2.png" alt="" />
                                    <p class="text-md">
                                        Watch instantly or download for later
                                    </p>
                                    <p class="text-dark">
                                        Available on phone and tablet, wherever you go.
                                    </p>
                                </div>
                                <div>
                                    <img src="https://i.ibb.co/gDhnwWn/tab-content-2-3.png" alt="" />
                                    <p class="text-md">
                                        Use any computer
                                    </p>
                                    <p class="text-dark">
                                        Watch right on Netflix.com.
                                    </p>
                                </div>
                            </div>
                        </div>

                        <!-- Tab Content 3 -->
                        <div id="tab-3-content" class="tab-content-item">
                            <div class="text-center">
                                <p class="text-lg">
                                    Choose one plan and watch everything on Netflix.
                                </p>
                                <a href="#" class="btn btn-lg">Watch Free For 30 Days</a>
                            </div>

                            <table class="table">
                                <thead>
                                    <tr>
                                        <th></th>
                                        <th>Basic</th>
                                        <th>Standard</th>
                                        <th>Premium</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr>
                                        <td>Monthly price after free month ends on 6/19/19</td>
                                        <td>$8.99</td>
                                        <td>$12.99</td>
                                        <td>$15.99</td>
                                    </tr>
                                    <tr>
                                        <td>HD Available</td>
                                        <td><i class="fas fa-times"></i></td>
                                        <td><i class="fas fa-check"></i></td>
                                        <td><i class="fas fa-check"></i></td>
                                    </tr>
                                    <tr>
                                        <td>Ultra HD Available</td>
                                        <td><i class="fas fa-times"></i></td>
                                        <td><i class="fas fa-times"></i></td>
                                        <td><i class="fas fa-check"></i></td>
                                    </tr>
                                    <tr>
                                        <td>Screens you can watch on at the same time</td>
                                        <td>1</td>
                                        <td>2</td>
                                        <td>4</td>
                                    </tr>
                                    <tr>
                                        <td>Watch on your laptop, TV, phone and tablet</td>
                                        <td><i class="fas fa-check"></i></td>
                                        <td><i class="fas fa-check"></i></td>
                                        <td><i class="fas fa-check"></i></td>
                                    </tr>
                                    <tr>
                                        <td>Unlimited movies and TV shows</td>
                                        <td><i class="fas fa-check"></i></td>
                                        <td><i class="fas fa-check"></i></td>
                                        <td><i class="fas fa-check"></i></td>
                                    </tr>
                                    <tr>
                                        <td>Cancel anytime</td>
                                        <td><i class="fas fa-check"></i></td>
                                        <td><i class="fas fa-check"></i></td>
                                        <td><i class="fas fa-check"></i></td>
                                    </tr>
                                    <tr>
                                        <td>First month free</td>
                                        <td><i class="fas fa-check"></i></td>
                                        <td><i class="fas fa-check"></i></td>
                                        <td><i class="fas fa-check"></i></td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </section>

                <footer class="footer">
                    <p>Questions? Call 1-866-579-7172</p>
                    <div class="footer-cols">
                        <ul>
                            <li><a href="#">FAQ</a></li>
                            <li><a href="#">Investor Relations</a></li>
                            <li><a href="#">Ways To Watch</a></li>
                            <li><a href="#">Corporate Information</a></li>
                            <li><a href="#">Netflix Originals</a></li>
                        </ul>
                        <ul>
                            <li><a href="#">Help Center</a></li>
                            <li><a href="#">Jobs</a></li>
                            <li><a href="#">Terms Of Use</a></li>
                            <li><a href="#">Contact Us</a></li>
                        </ul>
                        <ul>
                            <li><a href="#">Account</a></li>
                            <li><a href="#">Redeem Gift Cards</a></li>
                            <li><a href="#">Privacy</a></li>
                            <li><a href="#">Speed Test</a></li>
                        </ul>
                        <ul>
                            <li><a href="#">Media Center</a></li>
                            <li><a href="#">Buy Gift Cards</a></li>
                            <li><a href="#">Cookie Preferences</a></li>
                            <li><a href="#">Legal Notices</a></li>
                        </ul>
                    </div>
                </footer>
                <style>{}</style>""".format(f.read()), unsafe_allow_html=True)

#sidebar
user_api_key = st.sidebar.text_input("OpenAPI API key", type="password")
client = openai.OpenAI(api_key=user_api_key)

#Main
st.title("Welcome to Animagination! :partying_face:")
st.markdown("""Meet Animagination, your anime sidekick with a touch of AI magic! Whether you're an anime pro or just getting started, Animagination's here for you. Let's make your anime journey as delightful as discovering a hidden gem :star2:""")

#Animagination
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

user_input = st.text_input("What kinds of anime are you into or looking to explore?", 'I want to watch an anime that is funny and has a lot of action.')
st.markdown("Please keep in mind that the AI model is built on data available up to the year 2021.")

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