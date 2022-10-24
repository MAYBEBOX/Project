import streamlit as st

def hex_to_rgb(hex):
  return tuple(int(hex[i:i+2], 16) for i in (0, 2, 4)) 

value = st.color_picker('Choose Color Of Text', '#00f900')
text = st.text_input("Enter Text: ")
 
st.write(text, color = hex_to_rgb)
