import streamlit as st
from deep_translator import GoogleTranslator

st.title("Language Translator Tool 📋")
st.write("Enter Text To Translate Into Your Desired Language")

text = st.text_area("Enter Your Text")


languages = GoogleTranslator().get_supported_languages(as_dict=True)

language = st.selectbox(
    "Select Language",
    sorted(languages.keys())
)

if st.button("Translate 📜"):
    if text.strip() == "":
        st.warning("Please Enter Some Text To Translate")
    else:
        with st.spinner("Translating..."):
            translated_text = GoogleTranslator(
                source="auto",
                target=languages[language]
            ).translate(text)

        st.subheader("Translated Text 👇")
        st.write(translated_text)