import streamlit as st



value = st.color_picker('Choose Color Of Text', '#00f900')
text = st.text_input("Enter Text: ")
byte_array = bytearray.fromhex(value)
byte_array.decode()
st.write(value)
