import streamlit as st

#Q7
st.title("Prime Numbers")
st.info("Write a program that prints all the prime numbers between 0 and limit where limit is a variable.")

def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True

limit = st.number_input("Limit number:", min_value=2, step=1)

st.write("Prime numbers between 0 and", limit, "are:")

for num in range(2, limit + 1):
    if is_prime(num):
        st.write(num)

st.write("Done")