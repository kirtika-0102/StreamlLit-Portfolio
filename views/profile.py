import streamlit as st

st.title("Profile")

row1,row2,row3 = st.rows(3)
row1.image("assets\logo.jpeg")
row3.write("This is text")