import streamlit as st

st.title("Slider Test")

x = st.slider("select a value")

st.write(x, "square is",x*x)
