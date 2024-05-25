import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from PIL import Image
from vision import get_gemini_reponses
from qachat import get_gemini_response

load_dotenv()  # Loading environment variables

genai.configure(api_key=os.getenv("AIzaSyDFw_DhcEMIN2kdul3liC-ZnbOG9ckZjqQ"))  # Configure API key

def main():
    st.sidebar.title("Select an Application")
    app_choice = st.sidebar.radio("Choose Application", ("Vision", "Q&A Chat"))

    if app_choice == "Vision":
        st.title("Vision Application")
        st.header("Gemini Image Demo")

        input_text = st.text_input("Input Prompt:", key="input")

        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
        image = None
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)

        submit_button = st.button("Tell me about the image")

        if submit_button and image:
            with st.spinner("Generating response..."):
                response_text = get_gemini_reponses(input_text, image)
            st.subheader("The Response is")
            st.write(response_text)
        elif submit_button and not image:
            st.error("Please upload an image to proceed.")

    elif app_choice == "Q&A Chat":
        st.title("Q&A Chat Application")
        st.header("Gemini LLM Application")

        if 'chat_history' not in st.session_state:
            st.session_state['chat_history'] = []

        input_text = st.text_input("Input:", key="input")
        submit_button = st.button("Ask the question")

        if submit_button and input_text:
            with st.spinner("Generating response..."):
                response = get_gemini_response(input_text)
            st.session_state['chat_history'].append(("You", input_text))
            st.subheader("The Response is")
            for chunk in response:
                st.write(chunk.text)
                st.session_state['chat_history'].append(("Bot", chunk.text))

        st.subheader("The Chat history is")
        for role, text in st.session_state['chat_history']:
            st.write(f"{role}: {text}")

if __name__ == "__main__":
    main()
