import streamlit as st

value = st.color_picker('Choose Color Of Text', '#00f900')
text = st.text_input("Enter Text: ")
value = value.lstrip('#')
lv = len(value)
coloor = tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
st.write(text, color = coloor)
