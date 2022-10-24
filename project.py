import streamlit as st
while True:
  color = st.color_picker('Choose Color Of Text', '#00f900')
  
  if color == '':
    Print("Select Color")
  else:
    text = input("Input Mesaage")
    st.write(text, color)
