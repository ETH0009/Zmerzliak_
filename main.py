import streamlit as st
from send_email import send_email
from PIL import Image

image = Image.open("/rr.JPG")
st.title('Zmerzliak for today')
new_todo= st.text_input(label='Enter text', key='new_todo' )
st.image(image)
send_email(message=new_todo)