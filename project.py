import streamlit as st

value = st.color_picker('Choose Color Of Text', '#00f900')
text = st.text_input("Enter Text: ").lstrip('#')



def hex_to_rgb(hex):
  rgb = []
  for i in (0, 2, 4):
    decimal = int(hex[i:i+2], 16)
    rgb.append(decimal)
  
  return tuple(rgb)
st.write(text, color = hex_to_rgb(value))
