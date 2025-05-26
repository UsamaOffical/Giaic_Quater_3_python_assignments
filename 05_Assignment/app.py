import streamlit as st
import hashlib
from cryptography.fernet import Fernet

# Generate a key (keep it same while app runs, in prod save/load securely)
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

# In-memory data store
stored_data = {}  # {"encrypted_text": {"encrypted_text": ..., "passkey": ...}}
failed_attempts = 0

# Hash passkey
def hash_passkey(passkey: str) -> str:
    return hashlib.sha256(passkey.encode()).hexdigest()

# Encrypt text
def encrypt_data(text: str) -> str:
    return cipher.encrypt(text.encode()).decode()

# Decrypt text if passkey matches
def decrypt_data(encrypted_text: str, passkey: str) -> str | None:
    global failed_attempts
    hashed_passkey = hash_passkey(passkey)

    if encrypted_text in stored_data:
        if stored_data[encrypted_text]["passkey"] == hashed_passkey:
            failed_attempts = 0
            decrypted = cipher.decrypt(encrypted_text.encode()).decode()
            return decrypted
    failed_attempts += 1
    return None

# Streamlit UI
st.title("🔒 Secure Data Encryption System")

# Navigation menu
menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigation", menu)

if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0

if choice == "Home":
    st.subheader("🏠 Welcome")
    st.write("Securely store and retrieve your data with a unique passkey.")

elif choice == "Store Data":
    st.subheader("📂 Store Data Securely")
    user_data = st.text_area("Enter Data:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Encrypt & Save"):
        if user_data and passkey:
            hashed_passkey = hash_passkey(passkey)
            encrypted_text = encrypt_data(user_data)
            stored_data[encrypted_text] = {"encrypted_text": encrypted_text, "passkey": hashed_passkey}
            st.success("✅ Data stored securely!")
        else:
            st.error("⚠️ Both fields are required!")

elif choice == "Retrieve Data":
    st.subheader("🔍 Retrieve Your Data")
    encrypted_text = st.text_area("Enter Encrypted Data:")
    passkey = st.text_input("Enter Passkey:", type="password")

    if st.button("Decrypt"):
        if encrypted_text and passkey:
            decrypted_text = decrypt_data(encrypted_text, passkey)
            if decrypted_text:
                st.success(f"✅ Decrypted Data: {decrypted_text}")
                st.session_state.failed_attempts = 0
            else:
                st.session_state.failed_attempts += 1
                attempts_left = 3 - st.session_state.failed_attempts
                st.error(f"❌ Incorrect passkey! Attempts remaining: {attempts_left}")
                if st.session_state.failed_attempts >= 3:
                    st.warning("🔒 Too many failed attempts! Redirecting to Login Page.")
                    st.session_state.failed_attempts = 0
                    st.experimental_rerun()
        else:
            st.error("⚠️ Both fields are required!")

elif choice == "Login":
    st.subheader("🔑 Reauthorization Required")
    login_pass = st.text_input("Enter Master Password:", type="password")

    if st.button("Login"):
        if login_pass == "admin123":  # Replace with your secure auth logic
            st.success("✅ Reauthorized successfully! You can now retrieve data.")
            st.experimental_rerun()
        else:
            st.error("❌ Incorrect password!")
