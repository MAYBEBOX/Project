import streamlit as st
from PIL import ImageColor

value = st.color_picker('Choose Color Of Text', '#00f900')
text = st.text_input("Enter Text: ")
st.write(text)
color = ImageColor.getcolor(text, "RGB")

st.write(text, color = color)
