import streamlit as st

num = int(st.number_input("Input Number: ",value=0))

totalSum = 0

for i in range(1, num+1):
    totalSum += i

st.write(f"Sum is: {totalSum}")