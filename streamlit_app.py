"""A demo app for OSDC"""

# This is the famous first line of any Streamlit program.
import streamlit as st

num_hellos = st.slider("How many hellos", min_value=1, max_value=10)
for i in range(num_hellos):
    st.write(i, "Hello, world!!")

# Path to the Streamlit public S3 bucket
DATA_URL_ROOT = "https://streamlit-self-driving.s3-us-west-2.amazonaws.com/"

