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

col1,col2=st.columns(2)

with col1:
    st.subheader("🚗Daily compute distance (in km)")
    distance=st.slider("Distance",0.0,100.0,key="distance_input")
     
    st.subheader("💡Monthly Electricity consumption (in kwh)")
    electricity=st.slider("electricity",0.0,1000.0,key="electricity_input")

with col2:
    st.subheader("♻️Waste generated per week (in kg)")
    waste=st.slider("waste",0.0,100.0,key="waste_input")
     
    st.subheader("🍎Number of Meals per day)")
    meals=st.number_input("meals",0,key="meals_input")

if electricity>0:
    electricity=electricity*12

if distance>0:
    distance=distance*365

if waste>0:
    waste=waste*52

transportation_emission=EMISSION_FACTORS[country]["Transportation"]*distance
electricity_emission=EMISSION_FACTORS[country]["Electricity"]*electricity
diet_emission=EMISSION_FACTORS[country]["Diet"]*meals
waste_emission=EMISSION_FACTORS[country]["Waste"]*waste

transportation_emission=round(transportation_emission/1000,2)
electricity_emission=round(electricity_emission/1000,2)
diet_emission=round(diet_emission/1000,2)
waste_emission=round(waste_emission/1000,2)

total_emission=round(
    transportation_emission+electricity_emission+diet_emission+waste_emission,2
)

if st.button("calculate CO2 emissions"):

    st.header="results"

    col3,col4=st.columns(2)

    with col3:
        st.subheader("Carbon emission based on Categories")
        st.info(f"🚗 Transporatation {transportation_emission} tonnes per year")
        st.info(f"💡 Electricity {electricity_emission} tonnes per year")
        st.info(f"♻️ Food {diet_emission} tonnes per year")
        st.info(f"🍎 Waste {waste_emission} tonnes per year")

    with col4:
        st.subheader("Total Carbon Footprint")
        st.info(f"🌏Total Carbon Emission is {total_emission} tonnes per year")
        st.warning("In 2022, India's per capita CO2 emissions were approximately 1.9 tons per person.")
        
    