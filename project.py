import streamlit as st

valiue = st.color_picker('Choose Color Of Text', '#00f900')
text = st.text_input("Enter Text: ")
value = value.lstrip('#')
lv = len(value)
return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
st.write(text, color = value)
