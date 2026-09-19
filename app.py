import streamlit as st
from analyzer import FactifyAnalyzer

st.title("🛡️ Factify")
st.write("AI-Powered Misinformation & Fake News Detector")

user_text = st.text_area("Enter text to check:")

if st.button("Analyze"):
    if user_text.strip():
        analyzer = FactifyAnalyzer()
        result = analyzer.analyze(user_text)
        st.write(result)
    else:
        st.warning("Please enter some text.")