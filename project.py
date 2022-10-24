import streamlit as st

import getpass
database = {"aman.kharwal": "123456", "kharwal.aman": "654321"}
username = st.text_input("Enter Your Username : ")
password = st.text_input"Enter Your Password : ")
password = getpass.getpass()
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = st.text_input"Enter Your Password Again : ")
            password = getpass.getpass()
        break
print("Verified")
