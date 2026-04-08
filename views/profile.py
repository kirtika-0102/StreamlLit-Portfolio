import streamlit as st
import pandas as pd

st.title("Profile")
col1,col2,col3 = st.columns(3)
col1.image("assets/logo.jpeg",width=100)

df = pd.DataFrame({
    "Project": ["Alpha", "Beta", "Gamma"],
    "Budget": [1000, 2500, 1500],
    "Status": ["Complete", "In Progress", "Pending"]
})

# 1. Interactive Dataframe
st.subheader("Interactive View")
st.dataframe(df, use_container_width=True)

# 2. Static Table
st.subheader("Static View")
st.table(df)

# 3. Editable Table
st.subheader("Editable Editor")
edited_df = st.data_editor(df)