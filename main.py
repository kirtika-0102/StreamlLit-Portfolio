import streamlit as st
st.title("Streamlit App")
home_page= st.Page(
    page= "views/home.py",
    title= "HOME"
)
profile_page= st.Page(
    page= "views/profile.py",
    title= "PROFILE",
    default= True
)
contact_page= st.Page(
    page= "views/contact.py",
    title= "CONTACT US"
)
nb= st.navigation({
    'Info':[home_page, profile_page],
    'Useful links':[contact_page]
    })

st.logo("assets\logo.jpeg")
st.sidebar.text("Powered by : Kirtika Mittal")
nb.run()