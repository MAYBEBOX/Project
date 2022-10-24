import streamlit as st
import sys

RESET = '\033[0m'
def get_color_escape(r, g, b, background=False):
    return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)

value = st.color_picker('Choose Color Of Text', '#00f900')
text = st.text_input("Enter Text: ")
st.write("no", value)
st.write(get_color_escape(255, 128, 0) + " "+text + get_color_escape(80, 30, 60, True))
