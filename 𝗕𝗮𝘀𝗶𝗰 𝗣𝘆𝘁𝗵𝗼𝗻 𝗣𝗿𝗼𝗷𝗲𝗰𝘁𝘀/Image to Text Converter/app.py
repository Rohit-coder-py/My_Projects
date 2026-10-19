import streamlit as st
import pytesseract
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


# ---------- Glassmorphism styling (visual only) ----------
st.markdown(
    """
    <style>
    /* Colorful gradient backdrop so the glass has something to blur */
    .stApp {
        background:
            radial-gradient(circle at 15% 20%, rgba(255, 94, 196, 0.55) 0, transparent 40%),
            radial-gradient(circle at 85% 15%, rgba(94, 160, 255, 0.55) 0, transparent 40%),
            radial-gradient(circle at 75% 85%, rgba(140, 90, 255, 0.55) 0, transparent 45%),
            radial-gradient(circle at 20% 85%, rgba(0, 220, 190, 0.45) 0, transparent 40%),
            linear-gradient(135deg, #1b1042 0%, #2a1b6b 50%, #0f2a5c 100%);
        background-attachment: fixed;
    }

    /* Transparent top bar */
    [data-testid="stHeader"] {
        background: transparent;
    }

    /* Main frosted-glass card */
    .block-container {
        max-width: 760px;
        margin: 3rem auto;
        padding: 2.5rem 2.5rem 2.5rem 2.5rem !important;
        background: rgba(255, 255, 255, 0.12);
        backdrop-filter: blur(22px) saturate(160%);
        -webkit-backdrop-filter: blur(22px) saturate(160%);
        border: 1px solid rgba(255, 255, 255, 0.28);
        border-radius: 28px;
        box-shadow:
            0 8px 40px rgba(0, 0, 0, 0.35),
            inset 0 1px 0 rgba(255, 255, 255, 0.35);
    }

    /* Typography */
    h1, h2, h3, p, label, span, small {
        color: #ffffff !important;
    }
    h1 {
        font-weight: 700 !important;
        letter-spacing: 0.3px;
        text-shadow: 0 2px 12px rgba(0, 0, 0, 0.3);
    }
    h3 {
        font-weight: 400 !important;
        opacity: 0.85;
    }

    /* File uploader dropzone */
    [data-testid="stFileUploaderDropzone"] {
        background: rgba(255, 255, 255, 0.10);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        border: 1.5px dashed rgba(255, 255, 255, 0.45);
        border-radius: 20px;
        transition: all 0.25s ease;
    }
    [data-testid="stFileUploaderDropzone"]:hover {
        background: rgba(255, 255, 255, 0.18);
        border-color: rgba(255, 255, 255, 0.8);
        box-shadow: 0 0 24px rgba(255, 255, 255, 0.15);
    }
    [data-testid="stFileUploaderDropzone"] svg {
        color: #ffffff !important;
        fill: #ffffff !important;
    }

    /* Uploaded file chip */
    [data-testid="stFileUploaderFile"] {
        background: rgba(255, 255, 255, 0.10);
        border-radius: 14px;
    }

    /* Buttons (Convert + Browse files) */
    .stButton > button,
    [data-testid="stFileUploaderDropzone"] button {
        background: rgba(255, 255, 255, 0.18) !important;
        color: #ffffff !important;
        border: 1px solid rgba(255, 255, 255, 0.4) !important;
        border-radius: 14px !important;
        padding: 0.55rem 1.6rem;
        font-weight: 600;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        box-shadow:
            0 4px 18px rgba(0, 0, 0, 0.25),
            inset 0 1px 0 rgba(255, 255, 255, 0.35);
        transition: all 0.25s ease;
    }
    .stButton > button:hover,
    [data-testid="stFileUploaderDropzone"] button:hover {
        background: rgba(255, 255, 255, 0.30) !important;
        border-color: rgba(255, 255, 255, 0.75) !important;
        transform: translateY(-2px);
        box-shadow: 0 8px 26px rgba(0, 0, 0, 0.3);
    }
    .stButton > button:active {
        transform: translateY(0);
    }

    /* Result box (st.success) turned into glass */
    [data-testid="stAlert"] {
        background: rgba(255, 255, 255, 0.14) !important;
        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-left: 4px solid rgba(120, 255, 200, 0.9);
        border-radius: 18px;
        box-shadow: 0 6px 28px rgba(0, 0, 0, 0.25);
    }
    [data-testid="stAlert"] p {
        color: #ffffff !important;
        white-space: pre-wrap;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.title("Image to text converter app")

st.subheader("Convert any image into text ")

file = st. file_uploader("UPload your image file", type=["png","jpg","jpeg","img"])

button = st.button("Convert")

if button:
    image = Image.open(file)

    text = pytesseract.image_to_string(image)

    st.success(text)