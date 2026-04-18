import streamlit as st
import pandas as pd
import webbrowser

st.set_page_config(page_title="Sumalatha Loan Assistance", layout="wide")

# BACKGROUND
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
    color: white;
}
.card {
    padding:20px;
    border-radius:10px;
    background: rgba(255,255,255,0.1);
    text-align:center;
    transition:0.3s;
}
.card:hover {
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# SIDEBAR
st.sidebar.image("logo.jpg", width=120)
st.sidebar.title("Sumalatha Loan Assistance")

menu = st.sidebar.radio("Menu", ["Home", "Loan Details", "EMI Calculator", "Eligibility", "Apply", "Track Status", "Contact"])

# HOME
if menu == "Home":
    st.title("🏦 Welcome to Sumalatha Loan Assistance")
    st.write("Choose a loan below")

    col1, col2, col3, col4 = st.columns(4)

    if col1.button("🏠 Home Loan"):
        st.session_state.page = "Home Loan"
    if col2.button("💼 Personal Loan"):
        st.session_state.page = "Personal Loan"
    if col3.button("🎓 Education Loan"):
        st.session_state.page = "Education Loan"
    if col4.button("🟡 Gold Loan"):
        st.session_state.page = "Gold Loan"

# LOAN DETAILS PAGE
elif menu == "Loan Details":
    loan = st.selectbox("Select Loan", ["Home Loan","Personal Loan","Education Loan","Gold Loan"])

    if loan == "Home Loan":
        st.write("Interest: 8.5% | Tenure: up to 20 years")

    elif loan == "Personal Loan":
        st.write("Interest: 11% | Quick approval")

    elif loan == "Education Loan":
        st.write("Low interest for students")

    elif loan == "Gold Loan":
        st.write("Instant loan against gold")

# EMI
elif menu == "EMI Calculator":
    st.title("EMI Calculator")

    P = st.number_input("Loan Amount", value=100000)
    R = st.number_input("Interest (%)", value=10.0)
    T = st.number_input("Months", value=12)

    if st.button("Calculate"):
        r = R/1200
        emi = (P*r*(1+r)**T)/((1+r)**T-1)
        st.success(f"EMI: ₹ {round(emi,2)}")

# ELIGIBILITY (FIXED LOGIC)
elif menu == "Eligibility":
    st.title("Check Eligibility")

    salary = st.number_input("Monthly Salary", value=25000)
    age = st.number_input("Age", value=25)

    if st.button("Check"):
        if age < 21:
            st.error("Not eligible (age too low)")
        else:
            eligible = salary * 8   # more realistic
            st.success(f"Eligible Loan Amount: ₹ {eligible}")

# APPLY
elif menu == "Apply":
    st.title("Apply for Loan")

    name = st.text_input("Name")
    phone = st.text_input("Phone")
    loan = st.selectbox("Loan Type", ["Home","Personal","Education","Gold"])

    if st.button("Submit"):
        st.success("Application submitted!")

        # WhatsApp auto message
        msg = f"New Loan Application\nName: {name}\nPhone: {phone}\nLoan: {loan}"
        url = f"https://wa.me/918125157342?text={msg}"
        st.markdown(f"[Click to WhatsApp]({url})")

# TRACK STATUS
elif menu == "Track Status":
    st.title("Loan Status")

    app_id = st.text_input("Enter Phone Number")

    if st.button("Check Status"):
        st.info("Status: Under Review (Demo)")

# CONTACT
elif menu == "Contact":
    st.title("Contact")

    st.write("👩‍💼 Sumalatha")
    st.write("📱 8125157342")
    st.markdown("[WhatsApp](https://wa.me/918125157342)")
