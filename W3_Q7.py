import streamlit as st

def maxFinder(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    else:
        return num3

num1 = st.number_input("Number 1: ")
num2 = st.number_input("Number 2: ")
num3 = st.number_input("Number 3: ")

max = maxFinder(num1,num2,num3)
st.write("The maximum number of these three number is: ", max)