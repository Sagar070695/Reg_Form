import streamlit as st

# Set the page title
st.title("User Registration Form")
# Add a text input with a caption
name = st.text_input("Enter your name")
email = st.text_input("Enter your email")
pwd = st.text_input("Enter your password", type="password")

# Add a button with the caption "Register"
if(st.button("Register")):
  st.write("Thank you!")
