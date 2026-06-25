import streamlit as st
import requests

st.title("AI Travel Planner")

destination = st.text_input("Destination")
budget = st.text_input("Budget")
days = st.number_input("Number of Days", min_value=1)

if st.button("Generate Plan"):

    data = {
        "destination": destination,
        "budget": budget,
        "days": int(days)
    }

    response = requests.post(
        "http://127.0.0.1:8000/plan",
        json=data
    )

    result = response.json()

    st.write(result["plan"])
