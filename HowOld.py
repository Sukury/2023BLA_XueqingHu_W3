import streamlit as st

age = st.number_input("What is your age?",min_value=0,value=0)

if age<=12:
    st.write("You are in the childhood.")
elif age<=20:
    st.write("You are in the adolescence.")
elif age<=30:
    st.write("You are in the young adulthood.")
elif age<=65:
    st.write("You are in the middle adulthood.")
else:
    st.write("You are in the late adulthood.")

#if age in range(0,12):
#   st.write("1")
#elif ...