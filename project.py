import streamlit as st

Height=st.number_input("Enter your height in centimeters: ")
Weight=st.number_input("Enter your Weight in Kg: ")
Height = float(Height)/100
BMI= Weight/(Height*Height)
st.write("your Body Mass Index is: ",BMI)
if(BMI>0):
	if(BMI<=16):
		st.write("you are severely underweight")
	elif(BMI<=18.5):
		st.write("you are underweight")
	elif(BMI<=25):
		st.write("you are Healthy")
	elif(BMI<=30):
		st.write("you are overweight")
	else: 
		st.write("you are severely overweight")
else:
    st.write("enter valid details")
