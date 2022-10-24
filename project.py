import streamlit as st
while True:
  color = st.color_picker('Choose Color Of Text', '#00f900')
  text = st.text_input("Input Mesaage")
  st.write(text, color = color)
