import streamlit as st

coolor = st.color_picker('Choose Color Of Text', '#00f900')
text = st.text_input("Enter Text: ")
st.write(text, color = coolor)
