import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("🥤 Juice & Shake Recommendation System")

choice = st.radio("Choose Action", ["Get Recommendations", "Insert Sample Data"])

if choice == "Insert Sample Data":
    if st.button("Insert Sample Drinks"):
        res = requests.post(f"{API_URL}/insert-sample")
        st.success(res.json()["status"])

elif choice == "Get Recommendations":
    flavor = st.selectbox("Choose a flavor", ["Chocolate", "Mango", "Strawberry", "Pineapple", "Nutty", "Fruity", "Tangy", "Sweet", "Creamy", "Warm"])
    drink_type = st.selectbox("Choose type", ["Any", "Shake", "Juice", "Drink"])
    
    if st.button("Recommend"):
        type_param = None if drink_type == "Any" else drink_type
        res = requests.get(f"{API_URL}/recommend/", params={"flavor": flavor, "drink_type": type_param})
        
        st.subheader("Recommended Drinks:")
        for item in res.json()["recommendations"]:
            st.write("✅", item)
