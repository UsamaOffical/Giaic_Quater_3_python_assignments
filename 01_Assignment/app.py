import streamlit as st

st.set_page_config(page_title="Unit Converter", page_icon="🔄", layout="centered")
st.title("🔄 Unit Converter App")
st.caption("Made with ❤️ using Streamlit | By Usama")

# Conversion logic dictionaries
length_units = {
    "Meter": 1,
    "Kilometer": 1000,
    "Centimeter": 0.01,
    "Millimeter": 0.001,
    "Mile": 1609.34,
    "Yard": 0.9144,
    "Foot": 0.3048,
    "Inch": 0.0254
}

weight_units = {
    "Gram": 1,
    "Kilogram": 1000,
    "Pound": 453.592,
    "Ounce": 28.3495
}

temperature_units = ["Celsius", "Fahrenheit", "Kelvin"]

# Category Selection
category = st.selectbox("Choose Conversion Category", ["Length", "Weight", "Temperature"])

# Length & Weight Logic
def convert_units(value, from_unit, to_unit, unit_dict):
    return value * unit_dict[from_unit] / unit_dict[to_unit]

# Temperature Conversion Logic
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    # Convert from input to Celsius
    if from_unit == "Fahrenheit":
        value = (value - 32) * 5/9
    elif from_unit == "Kelvin":
        value = value - 273.15
    # Convert from Celsius to output
    if to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif to_unit == "Kelvin":
        return value + 273.15
    return value

# Input Section
st.markdown("---")
value = st.number_input("Enter Value", format="%.4f")

if category == "Length":
    from_unit = st.selectbox("From", list(length_units.keys()))
    to_unit = st.selectbox("To", list(length_units.keys()))
    result = convert_units(value, from_unit, to_unit, length_units)
    st.success(f"{value} {from_unit} = {round(result, 4)} {to_unit}")

elif category == "Weight":
    from_unit = st.selectbox("From", list(weight_units.keys()))
    to_unit = st.selectbox("To", list(weight_units.keys()))
    result = convert_units(value, from_unit, to_unit, weight_units)
    st.success(f"{value} {from_unit} = {round(result, 4)} {to_unit}")

elif category == "Temperature":
    from_unit = st.selectbox("From", temperature_units)
    to_unit = st.selectbox("To", temperature_units)
    result = convert_temperature(value, from_unit, to_unit)
    st.success(f"{value}° {from_unit} = {round(result, 2)}° {to_unit}")
