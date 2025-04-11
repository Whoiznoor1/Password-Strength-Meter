import streamlit as st
import re

# Inject custom styles for better UX
st.markdown("""
<style>
/* Title */
h1 {
    color: #2e7d32;
    font-size: 2.8em;
    font-weight: 700;
    text-align: center;
    margin-bottom: 0.2em;
}

/* Text input styling */
.stTextInput input {
    font-size: 1.1em;
    padding: 10px;
    border: 2px solid #2e7d32;
    border-radius: 6px;
}

/* Styled button */
.stButton>button {
    background-color: #2e7d32;
    color: white;
    border: none;
    border-radius: 8px;
    padding: 10px 25px;
    font-size: 1.1em;
    margin-top: 10px;
    transition: all 0.2s ease-in-out;
}
.stButton>button:hover {
    background-color: #256427;
}

/* Feedback messages */
.stAlert {
    font-size: 1.05em;
    border-radius: 8px;
    padding: 12px;
}
</style>
""", unsafe_allow_html=True)

# App header
st.markdown("## 🔐 Password Strength Evaluator")

# Input section
password_input = st.text_input("Enter a password you'd like to test:", type="password")

# Password evaluation logic
def evaluate_password(pwd):
    score = 0
    tips = []

    # Rule 1: Length
    if len(pwd) >= 8:
        score += 1
    else:
        tips.append("🔴 Use at least 8 characters for better security.")

    # Rule 2: Mix of uppercase and lowercase
    if re.search(r'[A-Z]', pwd) and re.search(r'[a-z]', pwd):
        score += 1
    else:
        tips.append("🔴 Include both **uppercase and lowercase** letters.")

    # Rule 3: Numbers
    if re.search(r'\d', pwd):
        score += 1
    else:
        tips.append("🔴 Add **numerical digits** (0–9) to increase strength.")

    # Rule 4: Special characters
    if re.search(r'[!@#$%^&*]', pwd):
        score += 1
    else:
        tips.append("🔴 Include special characters like **! @ # $ % ^ & ***.")

    return score, tips

# Check button
if st.button("🔎 Check Password"):
    if password_input:
        result, suggestions = evaluate_password(password_input)

        st.subheader("🔐 Evaluation Result")

        if result == 4:
            st.success("✅ Excellent! Your password is strong and secure.")
        elif result == 3:
            st.warning("⚠️ Decent password, but could be stronger.")
        else:
            st.error("❌ Weak password. Please improve it using the tips below.")

        if suggestions:
            st.markdown("### 💡 Tips to Strengthen Your Password")
            for tip in suggestions:
                st.write(tip)
    else:
        st.error("🚫 Please input a password to begin the evaluation.")

# App footer / context section
st.markdown("""
---
🔐 **Password Strength Checker Tool** helps you create a stronger, more secure digital presence by analyzing the following:

- ✅ **Minimum Length** of 8 characters  
- ✅ **Combination of uppercase & lowercase letters**  
- ✅ **Inclusion of numbers**  
- ✅ **Use of special characters**

🛡️ **Stay safe online—never share your passwords!**
""")
