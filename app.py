import streamlit as st

# Set up page with futuristic dark theme
st.set_page_config(page_title="Unit Converter", layout="wide")

# Theme Toggle
theme = st.sidebar.radio("🌓 Choose Theme", ["Dark Blue", "Light Blue"])

# CSS for Dark Blue and Light Blue Gradient Background
if theme == "Light Blue":
    st.markdown(
        """
        <style>
            .stApp {
                background: linear-gradient(to right, #a0c4ff, #c2d9ff);
                color: #222;
            }
            [data-testid="stSidebar"] {
                background-color: #e0efff;
                color: #000;
                border-right: 2px solid #3f7ecf;
            }
            .glow-text {
                text-shadow: 0 0 5px #3f7ecf, 0 0 10px #3f7ecf, 0 0 20px #56a1ff;
                color: #e0d6f5;
                font-weight: bold;
            }
        </style>
        """,
        unsafe_allow_html=True
    )
else:
    # Dark Blue Gradient CSS
    st.markdown(
        """
        <style>
            .stApp {
                background: linear-gradient(to right, #0c1f3e, #1a3e66);
                color: #e0d6f5;
            }
            [data-testid="stSidebar"] {
                background: rgba(10, 26, 52, 0.95);
                border-right: 2px solid #56a1ff;
                box-shadow: 5px 0px 15px rgba(86, 161, 255, 0.4);
            }
            div[data-testid="stFileUploader"] {
                border: 2px dashed #56a1ff;
                border-radius: 12px;
                padding: 15px;
                transition: all 0.3s ease-in-out;
            }
            div[data-testid="stFileUploader"]:hover {
                border-color: #3f7ecf;
                transform: scale(1.02);
            }
            .stButton > button {
                background: linear-gradient(90deg, #3f7ecf, #56a1ff);
                color: white;
                border-radius: 12px;
                padding: 12px 20px;
                font-weight: bold;
                transition: all 0.3s ease-in-out;
                border: none;
            }
            .stButton > button:hover {
                background: linear-gradient(90deg, #56a1ff, #3f7ecf);
                transform: scale(1.05);
                box-shadow: 0px 0px 15px rgba(86, 161, 255, 0.7);
            }
            .stDownloadButton > button {
                background: linear-gradient(90deg, #85baff, #3f7ecf);
                color: white;
                border-radius: 12px;
                padding: 12px 20px;
                transition: all 0.3s ease-in-out;
                font-weight: bold;
            }
            .stDownloadButton > button:hover {
                background: linear-gradient(90deg, #3f7ecf, #85baff);
                transform: scale(1.05);
                box-shadow: 0px 0px 15px rgba(63, 126, 207, 0.7);
            }
            .stDataFrame {
                border-radius: 12px;
                overflow: hidden;
                border: 2px solid #56a1ff;
                box-shadow: 0px 0px 20px rgba(86, 161, 255, 0.3);
            }
            .glow-text {
                text-shadow: 0 0 5px #56a1ff, 0 0 10px #56a1ff, 0 0 20px #3f7ecf;
                color: #e0d6f5;
                font-weight: bold;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

# Sidebar - Futuristic Glow Theme
st.sidebar.title("💫 Unit Converter 💫")
st.sidebar.write("✨ Convert various units in style! 🌟")

# Main Title with Glowing Effect
st.markdown('<h1 class="glow-text">⚡ UnitForge: Unit Converter 💾</h1>', unsafe_allow_html=True)
st.write("🔄 Convert units with futuristic **style**! 🚀")

# Conversion Selector
unit_categories = ["📏 Length", "⚖️ Mass", "⏱️ Time", "🌡️ Temperature", "🏃‍♂️ Speed"]
category = st.sidebar.selectbox("Choose Unit Category", unit_categories)

# Unit Conversion Logic
if category == "📏 Length":
    units = ["Meters (m)", "Kilometers (km)", "Miles (mi)", "Centimeters (cm)"]
    from_unit = st.selectbox("Convert from", units)
    to_unit = st.selectbox("Convert to", units)
    value = st.number_input("Enter value:", min_value=0.0, value=1.0)

    if st.button("Convert 🚀"):
        # Conversion Logic
        conversion_factors = {
            "Meters (m)": 1,
            "Kilometers (km)": 1000,
            "Miles (mi)": 1609.34,
            "Centimeters (cm)": 100
        }
        result = value * (conversion_factors[to_unit] / conversion_factors[from_unit])
        st.write(f"{value} {from_unit} = {result} {to_unit} 🌟")

elif category == "⚖️ Mass":
    units = ["Grams (g)", "Kilograms (kg)", "Pounds (lbs)", "Ounces (oz)"]
    from_unit = st.selectbox("Convert from", units)
    to_unit = st.selectbox("Convert to", units)
    value = st.number_input("Enter value:", min_value=0.0, value=1.0)

    if st.button("Convert ⚖️"):
        # Conversion Logic
        conversion_factors = {
            "Grams (g)": 1,
            "Kilograms (kg)": 1000,
            "Pounds (lbs)": 453.592,
            "Ounces (oz)": 28.3495
        }
        result = value * (conversion_factors[to_unit] / conversion_factors[from_unit])
        st.write(f"{value} {from_unit} = {result} {to_unit} ⚖️")

elif category == "⏱️ Time":
    units = ["Seconds (s)", "Minutes (min)", "Hours (h)", "Days (d)"]
    from_unit = st.selectbox("Convert from", units)
    to_unit = st.selectbox("Convert to", units)
    value = st.number_input("Enter value:", min_value=0.0, value=1.0)

    if st.button("Convert ⏳"):
        # Conversion Logic
        conversion_factors = {
            "Seconds (s)": 1,
            "Minutes (min)": 60,
            "Hours (h)": 3600,
            "Days (d)": 86400
        }
        result = value * (conversion_factors[to_unit] / conversion_factors[from_unit])
        st.write(f"{value} {from_unit} = {result} {to_unit} ⏳")

elif category == "🌡️ Temperature":
    units = ["Celsius (°C)", "Fahrenheit (°F)", "Kelvin (K)"]
    from_unit = st.selectbox("Convert from", units)
    to_unit = st.selectbox("Convert to", units)
    value = st.number_input("Enter value:", min_value=-273.15, value=0.0)

    if st.button("Convert 🌡️"):
        if from_unit == "Celsius (°C)":
            if to_unit == "Fahrenheit (°F)":
                result = (value * 9/5) + 32
            elif to_unit == "Kelvin (K)":
                result = value + 273.15
            else:
                result = value
        elif from_unit == "Fahrenheit (°F)":
            if to_unit == "Celsius (°C)":
                result = (value - 32) * 5/9
            elif to_unit == "Kelvin (K)":
                result = (value - 32) * 5/9 + 273.15
            else:
                result = value
        elif from_unit == "Kelvin (K)":
            if to_unit == "Celsius (°C)":
                result = value - 273.15
            elif to_unit == "Fahrenheit (°F)":
                result = (value - 273.15) * 9/5 + 32
            else:
                result = value

        st.write(f"{value} {from_unit} = {result} {to_unit} ❄️")

elif category == "🏃‍♂️ Speed":
    units = ["Meters per second (m/s)", "Kilometers per hour (km/h)", "Miles per hour (mph)", "Feet per second (ft/s)"]
    from_unit = st.selectbox("Convert from", units)
    to_unit = st.selectbox("Convert to", units)
    value = st.number_input("Enter value:", min_value=0.0, value=1.0)

    if st.button("Convert 🏃‍♂️"):
        # Conversion Logic
        conversion_factors = {
            "Meters per second (m/s)": 1,
            "Kilometers per hour (km/h)": 3.6,
            "Miles per hour (mph)": 2.23694,
            "Feet per second (ft/s)": 3.28084
        }
        result = value * (conversion_factors[to_unit] / conversion_factors[from_unit])
        st.write(f"{value} {from_unit} = {result} {to_unit} 🏃‍♂️")
