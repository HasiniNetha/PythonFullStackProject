import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.title("🥤 Juice & Shake Recommendation System")
st.write("Get personalized juice and shake recommendations based on your favorite flavor!")

choice = st.radio("Choose Action", ["Get Recommendations", "Insert Sample Data", "Check Connection"])

# --- Check connection ---
if choice == "Check Connection":
    try:
        res = requests.get(f"{API_URL}/check")
        st.success(res.json().get("status"))
    except Exception as e:
        st.error(f"❌ Connection failed: {e}")

# --- Insert sample data ---
elif choice == "Insert Sample Data":
    if st.button("Insert Sample Drinks into Database"):
        try:
            res = requests.post(f"{API_URL}/insert-sample")
            st.success(res.json().get("status"))
        except Exception as e:
            st.error(f"❌ Failed to insert data: {e}")

# --- Get recommendations ---
elif choice == "Get Recommendations":
    flavor = st.text_input("Enter a flavor (e.g., Chocolate, Mango, Strawberry)")
    drink_type = st.selectbox("Choose type", ["Any", "Shake", "Juice", "Drink"])

    if st.button("Get Recommendations"):
        if not flavor:
            st.warning("Please enter a flavor!")
        else:
            try:
                type_param = None if drink_type == "Any" else drink_type
                res = requests.get(f"{API_URL}/recommend/", params={"flavor": flavor, "drink_type": type_param})
                if res.status_code == 200:
                    data = res.json()
                    st.subheader("Recommended Drinks:")
                    for item in data.get("recommendations", []):
                        st.write("✅", item)
                else:
                    st.error(f"Server Error: {res.status_code}")
                    st.code(res.text)
            except Exception as e:
                st.error(f"❌ Could not connect to API: {e}")
