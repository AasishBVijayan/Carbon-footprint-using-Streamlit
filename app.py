import streamlit as st

EMISSION_FACTORS={
    "India":{
        "Transportation":0.14,
        "Electricity":0.82,
        "Diet":1.25,
        "Waste":0.1
    }
}

st.set_page_config(layout="wide",page_title="Personal Carbon Calculator")

st.title("Personal Carbon Calculator App")

st.subheader("Your Country")
country=st.selectbox("Select",["India"])