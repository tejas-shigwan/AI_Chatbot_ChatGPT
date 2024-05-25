from dotenv import load_dotenv
load_dotenv() # loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("AIzaSyDFw_DhcEMIN2kdul3liC-ZnbOG9ckZjqQ"))

# function to load Gemni Pro model and get responses
model=genai.GenerativeModel("gemini-pro")
def get_gemini_reponses(question):
    response=model.generate_content(question)
    return response.text

#initialize our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini Application")

input=st.text_input("Input: ",key="input")
submit=st.button("Ask the question")

# when submit is clicked

if submit:
    response=get_gemini_reponses(input)
    st.subheader("The response is")
    st.write(response)

