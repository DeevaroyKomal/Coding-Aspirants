import streamlit as st


about=st.Page(
    page="Files/About.py",
    title="About",
    default=True,
)

chat=st.Page(
    page="Files/Chatbot.py",
    title="Text your Problem",
)

image=st.Page(
    page="Files/ImageUpload.py",
    title="Upload the Image",
)

pg=st.navigation(pages=[about, chat, image])

pg.run()
