import streamlit as st

st.set_page_config(page_title="Sumalatha Loan Assistance", layout="wide")

# 🔥 BACKGROUND STYLE
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

# 🏦 HEADER
st.markdown("""
<h1 style='text-align:center;'>🏦 Sumalatha Loan Assistance</h1>
<h4 style='text-align:center;'>Trusted Banking Guidance</h4>
<hr>
""", unsafe_allow_html=True)

# 📌 SIDEBAR
st.sidebar.markdown("## 🏦 Sumalatha Loan Assistance")
menu = st.sidebar.radio("Menu", [
    "Home", 
    "Loan Details", 
    "EMI Calculator", 
    "Eligibility Checker", 
    "Apply", 
    "Track Status", 
    "Contact"
])

# 🏠 HOME
if menu == "Home":
    st.subheader("Choose Loan Type")

    col1, col2, col3, col4 = st.columns(4)

    col1.markdown("<div class='card'>🏠 Home Loan</div>", unsafe_allow_html=True)
    col2.markdown("<div class='card'>💼 Personal Loan</div>", unsafe_allow_html=True)
    col3.markdown("<div class='card'>🎓 Education Loan</div>", unsafe_allow_html=True)
    col4.markdown("<div class='card'>🟡 Gold Loan</div>", unsafe_allow_html=True)

# 📄 LOAN DETAILS
elif menu == "Loan Details":
    loan = st.selectbox("Select Loan", 
        ["Home Loan", "Personal Loan", "Education Loan", "Gold Loan"])

    if loan == "Home Loan":
        st.info("Interest: 8.5% | Tenure: up to 20 years")

    elif loan == "Personal Loan":
        st.info("Interest: 11% | Quick approval")

    elif loan == "Education Loan":
        st.info("Low interest for students")

    elif loan == "Gold Loan":
        st.info("Instant loan against gold")

# 📊 EMI CALCULATOR
elif menu == "EMI Calculator":
    st.subheader("EMI Calculator")

    P = st.number_input("Loan Amount (₹)", value=100000)
    R = st.number_input("Interest Rate (%)", value=10.0)
    T = st.number_input("Tenure (months)", value=12)

    if st.button("Calculate EMI"):
        r = R/1200
        emi = (P*r*(1+r)**T)/((1+r)**T-1)
        st.success(f"Monthly EMI: ₹ {round(emi,2)}")

# 🧠 ELIGIBILITY CHECKER
elif menu == "Eligibility Checker":
    st.subheader("Check Loan Eligibility")

    salary = st.number_input("Monthly Salary (₹)", value=25000)
    age = st.number_input("Age", value=25)

    if st.button("Check Eligibility"):
        if age < 21:
            st.error("❌ Not eligible (Minimum age 21)")
        else:
            eligible = salary * 8
            st.success(f"✅ Eligible amount: ₹ {eligible}")

# 📝 APPLY (FORM CONNECTED HERE)
elif menu == "Apply":
    st.subheader("Apply for Loan")

    st.info("Fill the form below. Your details will be securely recorded.")

    st.markdown("""
    <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSeVufRgJn3Kvf871ceybPR9yIMi8YDhpfCg2lSCQO68n_er3A/viewform?embedded=true" 
    width="100%" height="800" frameborder="0" marginheight="0" marginwidth="0">
    Loading…
    </iframe>
    """, unsafe_allow_html=True)

# 📍 TRACK STATUS
elif menu == "Track Status":
    st.subheader("Track Loan Status")

    phone = st.text_input("Enter Phone Number")

    if st.button("Check Status"):
        st.info("📌 Status: Under Review (Demo)")

# 📞 CONTACT
elif menu == "Contact":
    st.subheader("Contact Details")

    st.write("👩‍💼 Loan Advisor: Sumalatha")
    st.write("📱 Phone: 8125157342")
    st.write("📧 Email: sumalatha.loans@gmail.com")

    st.markdown("[💬 Chat on WhatsApp](https://wa.me/918125157342)")

# FOOTER
st.markdown("---")
st.caption("© 2026 Sumalatha Loan Assistance | Designed by Shankar")
