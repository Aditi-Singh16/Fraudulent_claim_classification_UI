import pandas as pd
import streamlit as st


def main():
    st.title("Fraudulent Claim Classification")
    menu = ['Home','About']
    choice = st.sidebar.selectbox("Menu",menu)

    if choice=="Home":
        st.subheader("Fraudulent Claim Classification Model Input Form")

        age = st.number_input("Age", min_value=0, max_value=120, value=0)
        gender = st.radio("Gender", ["Male", "Female", "Other"])
        income = st.number_input("Income", min_value=0, value=0)
        occupation = st.text_input("Occupation")
        policy_type = st.text_input("Policy Type")
        amount = st.number_input("Amount", min_value=0, value=0)
        premium = st.number_input("Premium", min_value=0, value=0)
        date_of_claim = st.date_input("Date of Claim")
        type_of_loss = st.text_input("Type of Loss")
        amount_claimed = st.number_input("Amount Claimed", min_value=0, value=0)
        payment_history = st.text_area("Payment History")

        if st.button("Submit"):
            st.success("Form submitted successfully!")
    else:
        st.title("About this App")

main() 