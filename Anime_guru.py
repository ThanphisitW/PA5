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
    st.markdown("""<!DOCTYPE html>
                <html lang="en">
                <body>
                    <nav id="desktop-nav">
                    <div class="logo">John Doe</div>
                    <div>
                        <ul class="nav-links">
                        <li><a href="#about">About</a></li>
                        <li><a href="#experience">Experience</a></li>
                        <li><a href="#projects">Projects</a></li>
                        <li><a href="#contact">Contact</a></li>
                        </ul>
                    </div>
                    </nav>
                    <nav id="hamburger-nav">
                    <div class="logo">John Doe</div>
                    <div class="hamburger-menu">
                        <div class="hamburger-icon" onclick="toggleMenu()">
                        <span></span>
                        <span></span>
                        <span></span>
                        </div>
                        <div class="menu-links">
                        <li><a href="#about" onclick="toggleMenu()">About</a></li>
                        <li><a href="#experience" onclick="toggleMenu()">Experience</a></li>
                        <li><a href="#projects" onclick="toggleMenu()">Projects</a></li>
                        <li><a href="#contact" onclick="toggleMenu()">Contact</a></li>
                        </div>
                    </div>
                    </nav>
                    <section id="profile">
                    <div class="section__pic-container">
                        <img src="./assets/profile-pic.png" alt="John Doe profile picture" />
                    </div>
                    <div class="section__text">
                        <p class="section__text__p1">Hello, I'm</p>
                        <h1 class="title">John Doe</h1>
                        <p class="section__text__p2">Frontend Developer</p>
                        <div class="btn-container">
                        <button
                            class="btn btn-color-2"
                            onclick="window.open('./assets/resume-example.pdf')"
                        >
                            Download CV
                        </button>
                        <button class="btn btn-color-1" onclick="location.href='./#contact'">
                            Contact Info
                        </button>
                        </div>
                        <div id="socials-container">
                        <img
                            src="./assets/linkedin.png"
                            alt="My LinkedIn profile"
                            class="icon"
                            onclick="location.href='https://linkedin.com/'"
                        />
                        <img
                            src="./assets/github.png"
                            alt="My Github profile"
                            class="icon"
                            onclick="location.href='https://github.com/'"
                        />
                        </div>
                    </div>
                    </section>
                    <section id="about">
                    <p class="section__text__p1">Get To Know More</p>
                    <h1 class="title">About Me</h1>
                    <div class="section-container">
                        <div class="section__pic-container">
                        <img
                            src="./assets/about-pic.png"
                            alt="Profile picture"
                            class="about-pic"
                        />
                        </div>
                        <div class="about-details-container">
                        <div class="about-containers">
                            <div class="details-container">
                            <img
                                src="./assets/experience.png"
                                alt="Experience icon"
                                class="icon"
                            />
                            <h3>Experience</h3>
                            <p>2+ years <br />Frontend Development</p>
                            </div>
                            <div class="details-container">
                            <img
                                src="./assets/education.png"
                                alt="Education icon"
                                class="icon"
                            />
                            <h3>Education</h3>
                            <p>B.Sc. Bachelors Degree<br />M.Sc. Masters Degree</p>
                            </div>
                        </div>
                        <div class="text-container">
                            <p>
                            Lorem ipsum dolor sit amet consectetur adipisicing elit. Hic quis
                            reprehenderit et laborum, rem, dolore eum quod voluptate
                            exercitationem nobis, nihil esse debitis maxime facere minus sint
                            delectus velit in eos quo officiis explicabo deleniti dignissimos.
                            Eligendi illum libero dolorum cum laboriosam corrupti quidem,
                            reiciendis ea magnam? Nulla, impedit fuga!
                            </p>
                        </div>
                        </div>
                    </div>
                    <img
                        src="./assets/arrow.png"
                        alt="Arrow icon"
                        class="icon arrow"
                        onclick="location.href='./#experience'"
                    />
                    </section>
                    <section id="experience">
                    <p class="section__text__p1">Explore My</p>
                    <h1 class="title">Experience</h1>
                    <div class="experience-details-container">
                        <div class="about-containers">
                        <div class="details-container">
                            <h2 class="experience-sub-title">Frontend Development</h2>
                            <div class="article-container">
                            <article>
                                <img
                                src="./assets/checkmark.png"
                                alt="Experience icon"
                                class="icon"
                                />
                                <div>
                                <h3>HTML</h3>
                                <p>Experienced</p>
                                </div>
                            </article>
                            <article>
                                <img
                                src="./assets/checkmark.png"
                                alt="Experience icon"
                                class="icon"
                                />
                                <div>
                                <h3>CSS</h3>
                                <p>Experienced</p>
                                </div>
                            </article>
                            <article>
                                <img
                                src="./assets/checkmark.png"
                                alt="Experience icon"
                                class="icon"
                                />
                                <div>
                                <h3>SASS</h3>
                                <p>Intermediate</p>
                                </div>
                            </article>
                            <article>
                                <img
                                src="./assets/checkmark.png"
                                alt="Experience icon"
                                class="icon"
                                />
                                <div>
                                <h3>JavaScript</h3>
                                <p>Basic</p>
                                </div>
                            </article>
                            <article>
                                <img
                                src="./assets/checkmark.png"
                                alt="Experience icon"
                                class="icon"
                                />
                                <div>
                                <h3>TypeScript</h3>
                                <p>Basic</p>
                                </div>
                            </article>
                            <article>
                                <img
                                src="./assets/checkmark.png"
                                alt="Experience icon"
                                class="icon"
                                />
                                <div>
                                <h3>Material UI</h3>
                                <p>Intermediate</p>
                                </div>
                            </article>
                            </div>
                        </div>
                        <div class="details-container">
                            <h2 class="experience-sub-title">Frontend Development</h2>
                            <div class="article-container">
                            <article>
                                <img
                                src="./assets/checkmark.png"
                                alt="Experience icon"
                                class="icon"
                                />
                                <div>
                                <h3>PostgreSQL</h3>
                                <p>Basic</p>
                                </div>
                            </article>
                            <article>
                                <img
                                src="./assets/checkmark.png"
                                alt="Experience icon"
                                class="icon"
                                />
                                <div>
                                <h3>Node JS</h3>
                                <p>Intermediate</p>
                                </div>
                            </article>
                            <article>
                                <img
                                src="./assets/checkmark.png"
                                alt="Experience icon"
                                class="icon"
                                />
                                <div>
                                <h3>Express JS</h3>
                                <p>Intermediate</p>
                                </div>
                            </article>
                            <article>
                                <img
                                src="./assets/checkmark.png"
                                alt="Experience icon"
                                class="icon"
                                />
                                <div>
                                <h3>Git</h3>
                                <p>Intermediate</p>
                                </div>
                            </article>
                            </div>
                        </div>
                        </div>
                    </div>
                    <img
                        src="./assets/arrow.png"
                        alt="Arrow icon"
                        class="icon arrow"
                        onclick="location.href='./#projects'"
                    />
                    </section>
                    <section id="projects">
                    <p class="section__text__p1">Browse My Recent</p>
                    <h1 class="title">Projects</h1>
                    <div class="experience-details-container">
                        <div class="about-containers">
                        <div class="details-container color-container">
                            <div class="article-container">
                            <img
                                src="./assets/project-1.png"
                                alt="Project 1"
                                class="project-img"
                            />
                            </div>
                            <h2 class="experience-sub-title project-title">Project One</h2>
                            <div class="btn-container">
                            <button
                                class="btn btn-color-2 project-btn"
                                onclick="location.href='https://github.com/'"
                            >
                                Github
                            </button>
                            <button
                                class="btn btn-color-2 project-btn"
                                onclick="location.href='https://github.com/'"
                            >
                                Live Demo
                            </button>
                            </div>
                        </div>
                        <div class="details-container color-container">
                            <div class="article-container">
                            <img
                                src="./assets/project-2.png"
                                alt="Project 2"
                                class="project-img"
                            />
                            </div>
                            <h2 class="experience-sub-title project-title">Project Two</h2>
                            <div class="btn-container">
                            <button
                                class="btn btn-color-2 project-btn"
                                onclick="location.href='https://github.com/'"
                            >
                                Github
                            </button>
                            <button
                                class="btn btn-color-2 project-btn"
                                onclick="location.href='https://github.com/'"
                            >
                                Live Demo
                            </button>
                            </div>
                        </div>
                        <div class="details-container color-container">
                            <div class="article-container">
                            <img
                                src="./assets/project-3.png"
                                alt="Project 3"
                                class="project-img"
                            />
                            </div>
                            <h2 class="experience-sub-title project-title">Project Three</h2>
                            <div class="btn-container">
                            <button
                                class="btn btn-color-2 project-btn"
                                onclick="location.href='https://github.com/'"
                            >
                                Github
                            </button>
                            <button
                                class="btn btn-color-2 project-btn"
                                onclick="location.href='https://github.com/'"
                            >
                                Live Demo
                            </button>
                            </div>
                        </div>
                        </div>
                    </div>
                    <img
                        src="./assets/arrow.png"
                        alt="Arrow icon"
                        class="icon arrow"
                        onclick="location.href='./#contact'"
                    />
                    </section>
                    <section id="contact">
                    <p class="section__text__p1">Get in Touch</p>
                    <h1 class="title">Contact Me</h1>
                    <div class="contact-info-upper-container">
                        <div class="contact-info-container">
                        <img
                            src="./assets/email.png"
                            alt="Email icon"
                            class="icon contact-icon email-icon"
                        />
                        <p><a href="mailto:examplemail@gmail.com">Example@gmail.com</a></p>
                        </div>
                        <div class="contact-info-container">
                        <img
                            src="./assets/linkedin.png"
                            alt="LinkedIn icon"
                            class="icon contact-icon"
                        />
                        <p><a href="https://www.linkedin.com">LinkedIn</a></p>
                        </div>
                    </div>
                    </section>
                    <footer>
                    <nav>
                        <div class="nav-links-container">
                        <ul class="nav-links">
                            <li><a href="#about">About</a></li>
                            <li><a href="#experience">Experience</a></li>
                            <li><a href="#projects">Projects</a></li>
                            <li><a href="#contact">Contact</a></li>
                        </ul>
                        </div>
                    </nav>
                    <p>Copyright &#169; 2023 John Doe. All Rights Reserved.</p>
                    </footer>
                    <script src="script.js"></script>
                </body>
                </html>
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