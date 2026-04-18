import streamlit as st
import pandas as pd

st.set_page_config(page_title="Sumalatha Loan Assistance", layout="wide")

# 🔥 CUSTOM CSS (BACKGROUND + ANIMATION)
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #141e30, #243b55);
    color: white;
}

.card {
    padding: 20px;
    border-radius: 10px;
    background: rgba(255,255,255,0.1);
    text-align: center;
    transition: 0.3s;
}

.card:hover {
    transform: scale(1.05);
}

</style>
""", unsafe_allow_html=True)

# 🧭 SIDEBAR
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/3135/3135706.png", width=100)
st.sidebar.title("Navigation")

menu = st.sidebar.radio("Go to", ["Home", "EMI Calculator", "Eligibility Checker", "Apply", "Contact"])

# 🏠 HOME
if menu == "Home":
    st.markdown("<h1 style='text-align:center;'>🏦 Sumalatha Loan Assistance</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align:center;'>Trusted Banking Guidance</h4>", unsafe_allow_html=True)

    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)

    col1.markdown("<div class='card'>🏠 Home Loan</div>", unsafe_allow_html=True)
    col2.markdown("<div class='card'>💼 Personal Loan</div>", unsafe_allow_html=True)
    col3.markdown("<div class='card'>🎓 Education Loan</div>", unsafe_allow_html=True)
    col4.markdown("<div class='card'>🟡 Gold Loan</div>", unsafe_allow_html=True)

# 📊 EMI CALCULATOR
elif menu == "EMI Calculator":
    st.title("📊 EMI Calculator")

    amount = st.number_input("Loan Amount (₹)", value=100000)
    rate = st.number_input("Interest Rate (%)", value=10.0)
    tenure = st.number_input("Tenure (months)", value=12)

    if st.button("Calculate EMI"):
        emi = (amount * rate/1200 * (1 + rate/1200)**tenure) / ((1 + rate/1200)**tenure - 1)
        st.success(f"Monthly EMI: ₹ {round(emi,2)}")

# 🧠 ELIGIBILITY CHECKER
elif menu == "Eligibility Checker":
    st.title("🧠 Loan Eligibility Checker")

    salary = st.number_input("Monthly Salary (₹)", value=25000)
    age = st.number_input("Age", value=25)
    employment = st.selectbox("Employment Type", ["Salaried", "Self-employed"])

    if st.button("Check Eligibility"):
        eligible_amount = salary * 20
        st.success(f"You are eligible for approx ₹ {eligible_amount}")

# 📝 APPLY FORM
elif menu == "Apply":
    st.title("📝 Apply for Loan")

    name = st.text_input("Full Name")
    phone = st.text_input("Phone Number")
    email = st.text_input("Email")
    city = st.text_input("City")

    loan_type = st.selectbox("Loan Type",
    ["Home Loan", "Personal Loan", "Education Loan", "Gold Loan"])

    income = st.number_input("Monthly Income")

    if st.button("Submit"):
        st.success("✅ Application submitted successfully!")

# 📞 CONTACT
elif menu == "Contact":
    st.title("📞 Contact")

    st.write("👩‍💼 Loan Advisor: Sumalatha")
    st.write("📱 Phone: 8125157342")
    st.write("📧 Email: slatha3245@gmail.com")

    st.markdown("[💬 Chat on WhatsApp](https://wa.me/+918125157342)")
