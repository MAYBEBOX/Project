import streamlit as st
import sys
Height=float(st.text_input("Enter your height in centimeters: "))
Weight=float(st.text_input("Enter your Weight in Kg: "))
Height = Height/100
BMI=Weight/(Height*Height)
st.write("your Body Mass Index is: ",BMI)
if(BMI>0):
	if(BMI<=16):
		print("you are severely underweight")
	elif(BMI<=18.5):
		print("you are underweight")
	elif(BMI<=25):
		print("you are Healthy")
	elif(BMI<=30):
		print("you are overweight")
	else: print("you are severely overweight")
else:
    st.write("enter valid details")
