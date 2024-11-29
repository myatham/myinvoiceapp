from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.set_page_config(page_title="Invoice Expert",page_icon="🤖")

st.header("Invoice Extracter Web Application")

input = st.text_input("Write your question here....")

uploaded_image = st.file_uploader("Choose an Image....",type=["jpg","png","jpeg"])

image = ""

submit = st.button("Submit")

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image,caption="Uploaded Image",use_container_width =True)

input_prompt = """You are expert in understanding invoices, you will get the input image as invoice and you
will have to answer the question based on the input invoice. If you get other image than invoice, then reply
with follwing message. ```I understand invoices only, please upload a valid invoice and ask relevant 
questions only``` 
"""
if submit:
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content([input_prompt,image,input])
    st.write(response.text)