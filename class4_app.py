import streamlit as st

st.title("Slider Test")
st.info("""
    use the slider tool in the streamlit library to create a slider tool for calculate the square of the input value
""")

x = st.slider("select a value")

st.write(x, "square is",x*x)
