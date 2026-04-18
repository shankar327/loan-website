import streamlit as st

st.set_page_config(page_title="Sumalatha Loan Assistance", layout="wide")

# HEADER
st.markdown("<h1 style='text-align:center;'>🏦 Sumalatha Loan Assistance</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align:center;'>Empowering Your Financial Journey</h4>", unsafe_allow_html=True)

st.markdown("---")

# SERVICES
st.subheader("💼 Loan Services")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("🏠 Home Loan\n\nLow interest & long tenure")

with col2:
    st.info("💼 Personal Loan\n\nQuick approval, no collateral")

with col3:
    st.info("🎓 Education Loan\n\nFor higher tudies")
s
with col4:
    st.info("🟡 Gold Loan\n\nInstant loan against gold")

st.markdown("---")

# EMI CALCULATOR
st.subheader("📊 EMI Calculator")

col1, col2, col3 = st.columns(3)

with col1:
    amount = st.number_input("Loan Amount (₹)", value=100000)

with col2:
    rate = st.number_input("Interest Rate (%)", value=10.0)

with col3:
    tenure = st.number_input("Tenure (months)", value=12)

if st.button("Calculate EMI"):
    emi = (amount * rate/1200 * (1 + rate/1200)**tenure) / ((1 + rate/1200)**tenure - 1)
    st.success(f"Monthly EMI: ₹ {round(emi,2)}")

st.markdown("---")

# APPLICATION FORM
st.subheader("📝 Apply for Loan")

name = st.text_input("Full Name")
phone = st.text_input("Phone Number")
email = st.text_input("Email")

loan_type = st.selectbox("Select Loan Type",
["Home Loan", "Personal Loan", "Education Loan", "Gold Loan"])

income = st.number_input("Monthly Income")

if st.button("Submit Application"):
    st.success("✅ Application submitted successfully!")
    st.write("We will contact you soon.")

st.markdown("---")

# CONTACT
st.subheader("📞 Contact")

st.write("📱 Phone: +91 XXXXXXXX")
st.write("📧 Email: your@email.com")
st.write("🏢 Location: Your City")

st.markdown("---")

st.caption("© 2026 Sumalatha Loan Assistance | Designed by Shankar")
