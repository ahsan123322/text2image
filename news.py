import requests
import streamlit as st
import io
from PIL import Image

# Define the Hugging Face API URL and authorization headers
API_URL = "https://api-inference.huggingface.co/models/runwayml/stable-diffusion-v1-5"
headers = {"Authorization": "Bearer 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"}

# Function to query the model and return the image
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

# Streamlit app
def main():
    st.title("Image Generator")

    # User input for the image description
    image_description = st.text_input("Enter an image description:")

    # Check if the user has provided a description
    if image_description:
        # Query the model with the user's input
        image_bytes = query({"inputs": image_description})

        # Display the generated image
        image = Image.open(io.BytesIO(image_bytes))
        st.image(image, caption="Generated Image", use_column_width=True)
    else:
        st.write("Please enter an image description to generate an image.")

if __name__ == "__main__":
    main()
