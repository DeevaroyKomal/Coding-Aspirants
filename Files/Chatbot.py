import streamlit as st
from pathlib import Path
import google.generativeai as genai

# Configure API key
genai.configure(api_key=st.secrets["api_key"])

# Model configuration
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
]

# System prompt
system_prompt = """
You are a medical assistant AI. You help analyze images and text descriptions of medical conditions. 
For images, provide a detailed analysis, and for text descriptions, respond with possible diagnoses, 
recommendations, and treatments. Always include a disclaimer advising users to consult a doctor.
"""

# Initialize model
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    generation_config=generation_config,
    safety_settings=safety_settings,
)

st.set_page_config(page_title="Medical Assistant", page_icon="🩺", layout="wide")
st.title("Virtual Medical Assistant 👨‍⚕️")

# Sidebar navigation
st.sidebar.header("Navigation")
page = st.sidebar.radio("Select an option", ["Text your Problem", "Upload the Image"])

if page == "Text your Problem":
    st.header("Describe Your Symptoms")
    user_input = st.text_area("Enter your symptoms or medical concerns:")
    submit_text = st.button("Get Analysis")
    
    if submit_text and user_input:
        response = model.generate_content([system_prompt, user_input])
        st.subheader("AI Response")
        st.write(response.text)
        st.warning("Disclaimer: This AI tool provides general medical information and should not be considered a substitute for professional medical advice. Always consult a healthcare provider.")

elif page == "Upload the Image":
    st.header("Upload an Image for Analysis")
    file_uploaded = st.file_uploader("Upload the image for analysis", type=["png", "jpg", "jpeg"])
    
    if file_uploaded:
        st.image(file_uploaded, width=300, caption="Uploaded Image")
        submit_img = st.button("Generate Analysis")
        
        if submit_img:
            image_data = file_uploaded.getvalue()
            image_parts = [{"mime_type": "image/jpeg", "data": image_data}]
            prompt_parts = [image_parts[0], system_prompt]
            response = model.generate_content(prompt_parts)
            
            st.subheader("Detailed Analysis Based on the Uploaded Image")
            st.write(response.text)
            st.warning("Disclaimer: This AI tool provides general medical information and should not be considered a substitute for professional medical advice. Always consult a healthcare provider.")
