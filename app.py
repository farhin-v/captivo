import streamlit as st
from config import LANGUAGES, PLATFORMS, OCCASIONS
from services.gemini import generate_caption
from services.sarvam import translate_caption

st.set_page_config(
    page_title="Captivo",
    page_icon="🛍️",
    layout="centered"
)

st.title("🛍️ Captivo")
st.subheader("AI-powered social media captions for Indian businesses")
st.divider()

st.markdown("### 📦 Product Details")

col1, col2 = st.columns(2)

with col1:
    product_name = st.text_input("Product Name", placeholder="e.g. Banarasi Saree")
    price = st.text_input("Price (₹)", placeholder="e.g. 2500")

with col2:
    category = st.text_input("Category", placeholder="e.g. Clothing")
    occasion = st.selectbox("Occasion", OCCASIONS)

st.divider()

st.markdown("### 📱 Platform & Language")

col3, col4 = st.columns(2)

with col3:
    platform = st.selectbox("Platform", PLATFORMS)

with col4:
    language = st.selectbox("Language", ["English"] + list(LANGUAGES.keys()))

st.divider()

if st.button("✨ Generate Caption", use_container_width=True):

    # Validate required fields before calling APIs
    if not product_name or not price or not category:
        st.error("Please fill in Product Name, Price and Category before generating.")

    else:
        with st.spinner("Generating your caption..."):

            english_caption = generate_caption(
                product_name, price, category, platform, occasion
            )

            if language == "English":
                final_caption = english_caption
            else:
                language_code = LANGUAGES[language]
                final_caption = translate_caption(english_caption, language_code)

        st.success("Caption generated!")
        st.divider()

        st.markdown(f"### Your {platform} Caption in {language}")
        st.code(final_caption, language=None, wrap_lines=True)

        if language != "English":
            with st.expander("See English version"):
                st.code(english_caption, language=None, wrap_lines=True)