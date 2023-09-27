import streamlit as st

st.title("Temperature Converter")

temperature = st.slider("What is the temperature?",-200,200,0)

convertTo = st.radio(
    "To what unity you want to convert",
    ("Farenheit","Celcius")
)


if (convertTo == "Farenheit"):
    newTemp=(temperature*9/5)+32
    unit="Farenheit"
else:
    newTemp=(temperature-32)*5/9
    unit="Celcius"

st.markdown("The convert temperature is **{:.2f}** degrees {}".format(newTemp,unit))