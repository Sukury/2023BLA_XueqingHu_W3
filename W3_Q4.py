import streamlit as st

sample_dict = {
    "Physics":82,"Math":65,"history":75
}

minValue = min(sample_dict, key=lambda k:sample_dict[k])
maxValue = max(sample_dict, key=lambda k:sample_dict[k])
st.write(f"Lowest score course is: {minValue}")
st.write(f"Highest score course is: {maxValue}")