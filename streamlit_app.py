"""A demo app for OSDC"""

import streamlit as st

num_hellos = st.slider("How many hellos?", min_value=1, max_value=10)

for i in range(num_hellos):
    st.write(i, "Hello, ODSC!!")
