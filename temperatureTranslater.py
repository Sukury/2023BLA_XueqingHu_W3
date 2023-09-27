import streamlit as st

st.title("Temperature Converter")
def fTranslater(cDegree):
    f = cDegree*9/5 + 32
    return f

def cTranslater(fDegree):
    c = (fDegree-32)*5/9
    return c

cDegree = st.number_input("centigrade converter:")
st.write(f"F = {fTranslater(cDegree)}")

fDegree = st.number_input("Fahrenheight converter:")
st.write(f"C = {cTranslater(fDegree)}")

