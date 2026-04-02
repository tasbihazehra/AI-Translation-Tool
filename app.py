import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
import io

# --- Page Setup ---
st.set_page_config(page_title="AI Language Translator", page_icon="🌐")

st.title("🌐 CodeAlpha AI Translation Tool")
st.markdown("---")

# --- UI Layout ---
# Get list of supported languages
langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)
lang_names = list(langs_dict.keys())

col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox("Select Source Language", ["auto"] + lang_names)
    input_text = st.text_area("Enter Text to Translate:", height=200)

with col2:
    target_lang = st.selectbox("Select Target Language", lang_names, index=lang_names.index("english"))
    
    if input_text:
        # Perform Translation
        translated = GoogleTranslator(source=source_lang, target=target_lang).translate(input_text)
        st.text_area("Translated Text:", value=translated, height=200)
        
        # Text-to-Speech Feature
        if st.button("🔊 Listen to Translation"):
            tts = gTTS(text=translated, lang=langs_dict[target_lang])
            audio_fp = io.BytesIO()
            tts.write_to_fp(audio_fp)
            st.audio(audio_fp, format='audio/mp3')
    else:
        st.info("Translation will appear here once you enter text.")

st.markdown("---")
st.caption("Developed for CodeAlpha AI Internship Task 1")
