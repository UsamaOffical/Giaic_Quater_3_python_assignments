import streamlit as st
import re
import random

# Common weak passwords list
blacklist = ["password", "123456", "qwerty", "abc123", "password123", "admin", "letmein", "welcome"]

# Function to check strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Check if in blacklist
    if password.lower() in blacklist:
        feedback.append("❌ This is a very common and unsafe password.")
        return 1, feedback

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    return score, feedback

# Strong password generator
def generate_password():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(12))

# Streamlit UI
st.set_page_config(page_title="Password Strength Meter", page_icon="🔐")
st.title("🔐 Password Strength Meter")
st.caption("Check how strong your password is!")

password = st.text_input("Enter your password", type="password")

if st.button("Check Strength"):
    if password:
        score, feedback = check_password_strength(password)
        st.markdown("---")
        if score == 4:
            st.success("✅ Strong Password!")
        elif score == 3:
            st.warning("⚠️ Moderate Password - Consider improving it.")
        else:
            st.error("❌ Weak Password - Improve it using the suggestions below.")
        st.write("### Feedback:")
        for fb in feedback:
            st.write(fb)
    else:
        st.warning("Please enter a password to check.")

# Extra: Password Generator
st.markdown("---")
if st.button("Suggest a Strong Password"):
    strong_pass = generate_password()
    st.info(f"🔒 Try this strong password: `{strong_pass}`")
