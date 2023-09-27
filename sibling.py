import streamlit as st

st.write("""
I am Xueqing \n
I have 1 sister(s) \n
I have 1 brother(s) \n
In total, I have 2 sibling(s)
""")

name = "Xueqing"
brother = 1
sister = 1
sibling = brother+sister
st.write(f"""
I am {name} \n
I have {brother} brother(s) \n
I have {sister} sisters \n
In total, I have {sibling} siblings
""")

st.write(f"I am {name}")
st.write(f"I have {brother} brothers")