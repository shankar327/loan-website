import streamlit as st

st.title("🏦 Sumalatha Loan Assistance")

st.write("Apply for loans easily")

name = st.text_input("Enter your name")
phone = st.text_input("Enter phone number")

loan = st.selectbox("Select Loan Type",
["Home Loan", "Personal Loan", "Education Loan", "Gold Loan"])

if st.button("Submit"):
    st.success("Submitted Successfully!")
