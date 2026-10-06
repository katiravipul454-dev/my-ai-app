import streamlit as st

st.title("Meri Pehli AI App 🚀")
st.write("Hello! Yeh meri GitHub aur Gemini se bani hui app hai.")

name = st.text_input("Apna naam likhein:")
if name:
    st.success(f"Hello {name}! Aapka swagat hai.")
