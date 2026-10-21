import base64

from pathlib import Path
import streamlit as st

from scraper import scrape_website
from summarizer import summarize_text

#-------------------------------------#
# Page Configuration                  #
#-------------------------------------#
   
ICON_PATH = Path(__file__).parent / "icons" / "icon_title.png"

st.set_page_config(
    page_title="AI Website Summarizer",
    page_icon=str(ICON_PATH),
    layout="wide"

)

#----------------------------------------------------#
# Custom Styling                                     #
#----------------------------------------------------#
st.markdown("""
<style>
    .stApp{
        background: linear-gradient(
            180deg, #f5f7ff 0%, #eef2ff 100%
        );
        color: #172033;
    }

    .block-container {
        max-width: 1100px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    .hero{
        background: linear-gradient(
            120deg, #111827 0%, #312e81 65%, #4f46e5 100%
        );
        padding: 2rem;
        border-radius: 20px;
        margin-bottom: 1.8rem;
        box-shadow: 0 12px 28px rgba(31, 41, 55, 0.15);
    }

    .eyebrow {
        color: #c7d2fe;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    .hero-title {
        display: flex;
        flex-direction: row;
        align-items: center;
        gap: 14px;
        margin: 14px 0;
    }

    .hero-title img {
        width: 56px;
        height: 56px;
        object-fit: contain;
        flex-shrink: 0;
    }

    .hero-title h1 {
        color: white;
        font-size: 2.3rem;
        line-height: 1.2;
        margin: 0;
        padding: 0;
    }

    .hero p {
        color: #e0e7ff;
        font-size: 1.05rem;
        margin-bottom: 0;
    }

    div[data-testid="stTextInput"] input {
        border-radius: 12px;
        min-height: 3rem;
    }

    .stButton > button {
        border-radius: 12px;
        min-height: 3rem;
        font-weight: 600;
    }
</style>
""", unsafe_allow_html=True)


#-------------------------------------#
#  Application heading                #
#-------------------------------------#

icon_base64 = base64.b64encode(
    ICON_PATH.read_bytes()
).decode("ascii")

st.markdown(
    '<div class="eyebrow">AI-Powered Reading Assistant</div>',
    unsafe_allow_html=True
)
col1, col2 = st.columns([1, 10], vertical_alignment="center")

with col1:
    st.image(str(ICON_PATH), width=56)

with col2:
    st.title("AI Website Summarizer")

st.write(
    "Turn lengthy webpages into clear summaries and key insights."
)

# URL Input

st.subheader("🔗 Summarize a webpage")

url = st.text_input(
    "Enter a website URL : ",
    placeholder="https://example.com"
)

# Summarize button
if st.button("✨ Summarize Website", type = "primary"):
    if not url.strip():
        st.warning("Please enter a website URL.")
    elif not url.strip().startswith(("https://", "http://")):
        st.warning("Please enter a valid URL starting with http:// or https://.")

    else:
        try:
            # Scrape the webpage
            with st.spinner("🌐 Fetching webpage ....."):
                title, text = scrape_website(url.strip())

            # Generate the AI summary
            with st.spinner("Generating your AI Summary ...."):
                summary = summarize_text(text)

            # Display the results.
            st.success("Summary Generated Successfully!")
            st.subheader(f"📄 {title}")

            with st.container(border=True):
                st.markdown("### ✨ AI Summary")
                st.markdown(summary)

            with st.expander("📊 View processing details"):
                st.write(f"Characters analyzed: {len(text):,}")
                st.write(f"Source URL: {url.strip()}")

        except Exception as error:
            st.error(f"Unable to summarize this webpage: {error}")

