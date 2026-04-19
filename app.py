import streamlit as st

st.set_page_config(page_title="Sumalatha Loan Assistance", layout="wide")

# 🔁 SESSION STATE
if "menu" not in st.session_state:
    st.session_state.menu = "Home"

if "selected_loan" not in st.session_state:
    st.session_state.selected_loan = "Home Loan"

# 🎨 STYLE
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

# 📌 SIDEBAR MENU (AUTO CONTROLLED)
menu_options = ["Home", "Loan Details", "EMI Calculator", "Eligibility Checker", "Apply", "Track Status", "Contact"]

menu = st.sidebar.radio("Menu", menu_options, index=menu_options.index(st.session_state.menu))
st.session_state.menu = menu

# 🏠 HOME (CLICK → CHANGE SIDEBAR)
if menu == "Home":
    st.subheader("Choose Loan Type")

    col1, col2, col3, col4 = st.columns(4)

    if col1.button("🏠 Home Loan"):
        st.session_state.selected_loan = "Home Loan"
        st.session_state.menu = "Loan Details"
        st.rerun()

    if col2.button("💼 Personal Loan"):
        st.session_state.selected_loan = "Personal Loan"
        st.session_state.menu = "Loan Details"
        st.rerun()

    if col3.button("🎓 Education Loan"):
        st.session_state.selected_loan = "Education Loan"
        st.session_state.menu = "Loan Details"
        st.rerun()

    if col4.button("🟡 Gold Loan"):
        st.session_state.selected_loan = "Gold Loan"
        st.session_state.menu = "Loan Details"
        st.rerun()

# 📄 LOAN DETAILS (AUTO SELECTED)
elif menu == "Loan Details":
    loan = st.selectbox(
        "Select Loan",
        ["Home Loan", "Personal Loan", "Education Loan", "Gold Loan"],
        index=["Home Loan", "Personal Loan", "Education Loan", "Gold Loan"].index(st.session_state.selected_loan)
    )

    if loan == "Home Loan":
        st.info("🏠 Interest: 8.5% | Tenure: up to 20 years")

    elif loan == "Personal Loan":
        st.info("💼 Interest: 11% | Quick approval")

    elif loan == "Education Loan":
        st.info("🎓 Low interest for students")

    elif loan == "Gold Loan":
        st.info("🟡 Instant loan")

# 📊 EMI
elif menu == "EMI Calculator":
    st.subheader("EMI Calculator")

    P = st.number_input("Loan Amount (₹)", value=100000)
    R = st.number_input("Interest Rate (%)", value=10.0)
    T = st.number_input("Tenure (months)", value=12)

    if st.button("Calculate"):
        r = R/1200
        emi = (P*r*(1+r)**T)/((1+r)**T-1)
        st.success(f"EMI: ₹ {round(emi,2)}")

# 🧠 ELIGIBILITY
elif menu == "Eligibility Checker":
    st.subheader("Eligibility Checker")

    salary = st.number_input("Monthly Salary", value=25000)
    age = st.number_input("Age", value=25)

    if st.button("Check"):
        if age < 21:
            st.error("Not eligible")
        else:
            st.success(f"Eligible Loan: ₹ {salary * 8}")

# 📝 APPLY (FORM)
elif menu == "Apply":
    st.subheader("Apply for Loan")

    st.markdown("""
    <iframe src="https://docs.google.com/forms/d/e/1FAIpQLSeVufRgJn3Kvf871ceybPR9yIMi8YDhpfCg2lSCQO68n_er3A/viewform?embedded=true" 
    width="100%" height="800">
    </iframe>
    """, unsafe_allow_html=True)

# 📍 TRACK
elif menu == "Track Status":
    st.subheader("Track Status")

    phone = st.text_input("Enter Phone Number")

    if st.button("Check"):
        st.info("Status: Under Review")

# 📞 CONTACT
elif menu == "Contact":
    st.subheader("Contact")

    st.write("👩‍💼 Sumalatha")
    st.write("📱 8125157342")
    st.markdown("[WhatsApp](https://wa.me/918125157342)")

# FOOTER
st.markdown("---")
st.caption("© 2026 Sumalatha Loan Assistance | Designed by Shankar")
