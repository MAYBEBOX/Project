import streamlit as st

coolor = st.color_picker('Choose Color Of Text', '#00f900')
if st.button('change', color = coolor):
    st.write('Why hello there', color = coolor)
else:
    st.write('Goodbye', color = coolor)
st.write(text, color = coolor)
