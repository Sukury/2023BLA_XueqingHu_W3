import streamlit as st

#Q6
st.title("Row Printer")
st.info("""
    Write a program that define a variable rows. If rows is 5, it should print the following:\n
    · *\n
    · **\n
    · ***\n
    · ****\n
    · *****
""")

num = st.number_input("Row number: ", min_value=0, value=0)
i = 1

while i <= num:
    st.write("·" + i*"*")
    i += 1
st.write("Done")