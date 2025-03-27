import streamlit as st

def setup_page():
    st.set_page_config(page_title="Medical Assistant", page_icon="🩺", 
layout="wide")
st.title(" Virtual Medical Assistant 👨‍⚕️") 

st.write("\n")
st.subheader("About")
st.write(
    """
    Empowering Health with AI-Powered Insights""")
st.write("\n")
st.write(
    """
    Welcome to Virtual Medical Assisstant, a platform dedicated to improving healthcare accessibility through AI-driven assistance. Our goal is to make health information more accessible and actionable for everyone, ensuring early detection and informed decision-making."""
)

st.write("\n")
st.subheader("Text-Based Health Queries")
st.write(
    """
    Simply describe your symptoms in text, and our system will provide relevant health suggestions."""
)
st.subheader("Image-Based Diagnosis")
st.write(
    """
    Upload an image of a skin condition, wound, or any visible symptom, and get AI-powered insights on possible conditions and next steps."""
)
st.subheader("Instant Guidance")
st.write(
    """
    Our platform does not replace professional medical advice but helps you make informed decisions about when to seek medical attention."""
)
