import streamlit as st

#Q1
num1 = 13
num2 = 25

st.write(num1)
st.write(num2)

if num1 < num2:
    st.write(f"the maximum number is {num2}")
else:
    st.write(f"the maximum number is {num1}")

st.write(" \n")

#Q2
inputNum = int(st.number_input("Please give me a number: ", min_value=0,value=0))
def fizz_buzz(inputNum):
    if inputNum % 3 == 0 and inputNum % 5 == 0:
        st.write("FizzBuzz")
    elif inputNum%5 == 0:
        st.write("Buzz")
    elif inputNum%3 == 0:
        st.write("Fizz")
    else:
        st.write(str(inputNum))
#result = fizz_buzz(inputNum)

#Q3
speed = st.number_input("Your Speed:")
demerit_point = 0

if speed < 70:
    st.write("OK")
elif speed >70:
    demerit_points = (speed - 70) // 5
    if demerit_points > 12:
        st.write("License suspended")
    else:
        st.write(f"Points: {demerit_points}")
