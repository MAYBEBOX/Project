import streamlit as st
from colorir import HexRGB, sRGB

value = st.color_picker('Choose Color Of Text', '#00f900')
text = st.text_input("Enter Text: ")
rgb = HexRGB(value).rgb()  
st.write(text, color = rgb)
