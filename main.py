import streamlit as st
import pandas as pd

st.write("""
# Multiplication of 2 given numbers.
""")

x = st.number_input(label="Enter first number")
y = st.number_input(label="Enter second number")

ans=x*y


if st.button("Calculate"):
    st.success(f"Answer = {ans}")

