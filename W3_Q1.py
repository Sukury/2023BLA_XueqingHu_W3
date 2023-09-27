import streamlit as st

givenNum = [1,3,5,7,9,11]

squaredNum = [x**2 for x in givenNum]

st.write(f"The square of numbers in the list: {givenNum} is {squaredNum}")