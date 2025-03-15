import streamlit as st
import re

# Title
st.title("🔐 Password Generator")
st.markdown("""
       ## Welcome to the Password Generator App  
       This is a simple password generator app that checks the strength of your password.  

       ### Why Use This App?  
       - 🔐 Ensures your password is strong and secure  
       - 🛡️ Helps protect your accounts from hackers  
       - 🔍 Provides instant feedback on password strength  

       ### How to Use  
       1. Enter your password in the text field.  
       2. Click the **Check Password Strength** button.  
       3. Get instant feedback on how to improve your password.  

       *Make sure your password includes a mix of uppercase, lowercase, numbers, and special characters!*  
   """)

# User input
password = st.text_input("Enter your password", type="password")

# Button to check password strength
if st.button("Check Password Strength"):
    score = 0
    feedback = []

    if password:
        # Length check
        if len(password) >= 8:
            score += 1
        else:
            feedback.append("❌ Password must be at least 8 characters long")

        # Lower and upper case letter check
        if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
            score += 1
        else:
            feedback.append("❌ Password must contain at least one lowercase and one uppercase letter")

        # Digit check
        if re.search(r"\d", password):
            score += 1
        else:
            feedback.append("❌ Password must contain at least one number")

        # Special character check
        if re.search(r"[$#@%!]", password):
            score += 1
        else:
            feedback.append("❌ Password must contain at least one special character")

        # Password rating
        if score == 4:
            feedback.append("✅ Password is strong.")
            feedback.append("Password is created!")
        elif score == 3:
            feedback.append("⚠️ Password is moderate.")
        else:
            feedback.append("❌ Password is weak.")

        # Display feedback
        st.markdown("## Password Strength Feedback")
        for message in feedback:
            st.write(message)
    else:
        st.info("Please enter a password to check its strength.")
