import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Car Price Prediction")

df = pd.read_csv("files/car_data.csv")

st.title("Car Price Predictor")
st.write("Enter car details below to predict the selling price 👇")

model_choice = st.radio("Select Model", ["Linear Regression", "Random Forest"])

if model_choice == "Linear Regression":
    model = pickle.load(open("files/linear_model.pkl", "rb"))
else:
    model = pickle.load(open("files/rf_model.pkl", "rb"))

st.write("### Car Details")

col1, col2 = st.columns(2)

with col1:
    present_price = st.number_input("Buying Price(Lakhs)", min_value=0.0, max_value=100.0, value=10.0, step=0.5)
    age = st.number_input("Car Age (years)", min_value=0, max_value=30, value=5)
    km = st.number_input("Kilometers Driven", min_value=0, max_value=500000, value=20000, step=1000)

with col2:
    owner_display = st.selectbox("Owner Type", ["First Owner", "Second Owner", "Third Owner or More"])

    owner_map = {"First Owner": 0, "Second Owner": 1, "Third Owner or More": 3}
    owner = owner_map[owner_display]
    
    fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
    seller = st.selectbox("Seller Type", ["Dealer", "Individual"])
    trans = st.selectbox("Transmission", ["Manual", "Automatic"])

if st.button("Predict Price",type="primary"):
    input_encoded = pd.DataFrame({
        "Present_Price": [present_price],
        "Driven_kms": [km],
        "Owner": [owner],
        "Car_Age": [age],
        "Fuel_Type_Diesel": [1 if fuel == "Diesel" else 0],
        "Fuel_Type_Petrol": [1 if fuel == "Petrol" else 0],
        "Selling_type_Individual": [1 if seller == "Individual" else 0],
        "Transmission_Manual": [1 if trans == "Manual" else 0]
    })

    price = model.predict(input_encoded)[0]
    
    st.success(f"Estimated Selling Price: {round(price, 2)} Lakhs")
    st.info(f"Model used: {model_choice}")

    depreciation = present_price - price
    depreciation_percent = (depreciation / present_price) * 100 if present_price > 0 else 0
    
    st.write(f"**Depreciation:** {round(depreciation, 2)} Lakhs ({round(depreciation_percent, 1)}%)")
    
    with st.expander("View Input Details"):
        st.write(f"**Present Price:** ₹{present_price} Lakhs")
        st.write(f"**Car Age:** {age} years")
        st.write(f"**Kilometers Driven:** {km:,} km")
        st.write(f"**Owner Type:** {owner_display}")
        st.write(f"**Fuel Type:** {fuel}")
        st.write(f"**Seller Type:** {seller}")
        st.write(f"**Transmission:** {trans}")
