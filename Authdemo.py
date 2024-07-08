import pickle
from pathlib import Path

import pandas as pd  # pip install pandas openpyxl

import streamlit as st  # pip install streamlit
import streamlit_authenticator as stauth  # pip install streamlit-authenticator


# # emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
# st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")


# --- USER AUTHENTICATION ---
names = ["Sennerikuppam Siva Kamakshi", "Tanveer Alam Shekh"]
usernames = ["ssennerikuppam", "astanveer"]

# load hashed passwords
file_path = Path(__file__).parent / "ssk_hashed.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)

authenticator = stauth.Authenticate(names, usernames, hashed_passwords,
    "sales_dashboard", "abcdef", cookie_expiry_days=0)

name, authentication_status, username = authenticator.login("Login", "main")

if authentication_status == False:
    st.error("Username/password is incorrect")

if authentication_status == None:
    st.warning("Please enter your username and password")

if authentication_status:
    st.header("yayyy!")