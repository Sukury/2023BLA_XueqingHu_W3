import streamlit as st

for a in range (0,99):
    num = 99 - a
    newNum = num-1
    st.write(f"{num} beers")
    st.write(f"take one down,{newNum} beers")
    a += 1
    if num == 1:
        st.write("no more")
    #else:
        st.write("hahaha")
