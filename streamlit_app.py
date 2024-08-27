import requests
import io
from PIL import Image
import streamlit as st

# Set the authorization header
headers = {"Authorization": "Bearer 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"}

# Function to query the Stability Diffusion API
def query_stabilitydiff(payload, headers):
    API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

# Streamlit UI
st.title("Stable Diffusion Image Generator")

# User input for the prompt
prompt = st.text_input("Enter a prompt", value="")

if st.button("Generate Image"):
    # Get the image bytes from the API
    image_bytes = query_stabilitydiff({"inputs": prompt}, headers)
    
    # Display the image
    image = Image.open(io.BytesIO(image_bytes))
    st.image(image, caption=f'Here is your image related to "{prompt}"')
