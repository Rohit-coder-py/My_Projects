"""
SlangDecode -- Gen-Z Slang & Acronym Decoder

A simple, reliable Streamlit app: type a Gen-Z slang term / acronym
and instantly see its full-form meaning. Built on top of a curated
acronym -> expansion dataset (data/slang_dataset.csv).

Run with:
    streamlit run app.py
"""

from __future__ import annotations

import logging
import random
from pathlib import Path

import streamlit as st

from utils.slang_utils import SlangDataError, load_slang_dict, lookup_slang

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("slangdecode")

BASE_DIR = Path(__file__).resolve().parent
LOGO_PATH = BASE_DIR / "assets" / "logo.png"
GRAPH_DIR = BASE_DIR / "graphs"

st.set_page_config(
    page_title="SlangDecode | Gen-Z Slang Decoder",
    page_icon="🔤",
    layout="centered",
)

# ---------------------------------------------------------------------
# Minimal styling
# ---------------------------------------------------------------------
st.markdown(
    """
    <style>
    .result-box {
        background-color: rgba(124, 92, 255, 0.10);
        border: 1px solid rgba(124, 92, 255, 0.35);
        border-radius: 12px;
        padding: 1.1rem 1.4rem;
        margin-top: 0.6rem;
    }
    .result-label {
        font-size: 0.8rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: #7C5CFF;
        font-weight: 600;
    }
    .result-text {
        font-size: 1.35rem;
        font-weight: 600;
        margin-top: 0.15rem;
    }
    .app-tagline {
        color: #9aa0a6;
        margin-top: -0.6rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------------------------------------------------------------------
# Data loading (cached so the CSV is parsed only once per session)
# ---------------------------------------------------------------------
@st.cache_resource(show_spinner="Loading slang dictionary...")
def get_slang_dict() -> dict[str, str]:
    return load_slang_dict()


# ---------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------
header_left, header_right = st.columns([1, 5])
with header_left:
    if LOGO_PATH.exists():
        st.image(str(LOGO_PATH), width=80)
    else:
        st.markdown("### 🔤")
with header_right:
    st.markdown("## SlangDecode")
    st.markdown(
        '<p class="app-tagline">Instantly decode Gen-Z slang & acronyms.</p>',
        unsafe_allow_html=True,
    )

st.caption(
    "Type a slang term like `iykyk`, `fr fr`, or `nglqm` and get its full meaning — "
    "backed by a curated dataset of 3,000+ acronym-to-expansion mappings."
)
st.divider()

# ---------------------------------------------------------------------
# Load data (with graceful failure)
# ---------------------------------------------------------------------
try:
    slang_dict = get_slang_dict()
except SlangDataError as exc:
    st.error(f"⚠️ Could not load the slang dataset.\n\n{exc}")
    st.stop()
except Exception:  # boundary of last resort -- log full detail, hide from user
    logger.exception("Unexpected error while loading the slang dataset")
    st.error(
        "⚠️ Something went wrong while starting the app. "
        "Please try again later or contact the maintainer."
    )
    st.stop()

# ---------------------------------------------------------------------
# Input section
# ---------------------------------------------------------------------
col_input, col_button = st.columns([4, 1])
with col_input:
    term = st.text_input(
        "Enter a slang term or acronym",
        placeholder="e.g. iykyk, fr fr, rizz, nglqm...",
        label_visibility="collapsed",
    )
with col_button:
    decode_clicked = st.button("Decode", use_container_width=True)

surprise_clicked = st.button("🎲 Surprise me with a random slang")

if surprise_clicked:
    term = random.choice(list(slang_dict.keys()))
    decode_clicked = True

# ---------------------------------------------------------------------
# Result section
# ---------------------------------------------------------------------
if decode_clicked:
    if not term or not term.strip():
        st.warning("Please enter a slang term before hitting Decode.")
    else:
        result = lookup_slang(term, slang_dict)

        if result.found:
            st.markdown(
                f"""
                <div class="result-box">
                    <div class="result-label">{result.query}</div>
                    <div class="result-text">{result.expansion}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.error(f"❌ \"{result.query}\" was not found in the dataset.")
            if result.suggestions:
                st.info("Did you mean: " + ", ".join(f"**{s}**" for s in result.suggestions) + "?")
            else:
                st.caption("Try checking the spelling, or browse the full list below.")

st.divider()

# ---------------------------------------------------------------------
# Browse full dataset
# ---------------------------------------------------------------------
with st.expander(f"📖 Browse all {len(slang_dict)} slang terms"):
    search = st.text_input("Filter list", placeholder="Type to filter...", key="filter_box")
    items = sorted(slang_dict.items())
    if search:
        s = search.strip().lower()
        items = [(k, v) for k, v in items if s in k or s in v.lower()]
    st.dataframe(
        {"Acronym": [k for k, _ in items], "Meaning": [v for _, v in items]},
        use_container_width=True,
        height=300,
    )

# ---------------------------------------------------------------------
# Model / project information
# ---------------------------------------------------------------------
with st.expander("ℹ️ About this app"):
    st.markdown(
        """
- **Type:** Dictionary/lookup-based decoder (rule-based, not a trained ML model)
- **Data:** ~3,350 curated Gen-Z acronym → expansion pairs (`data/slang_dataset.csv`)
- **Matching:** Case-insensitive exact match, with nearest-match suggestions
  (via Python's `difflib`) when a term isn't found
- **Framework:** Streamlit
- **Why not a neural network?** The task — mapping a known acronym to a fixed
  meaning — is a direct lookup problem. A dictionary is the correct, transparent
  tool for it; adding a model here wouldn't improve accuracy, only add opacity.
        """
    )

    if GRAPH_DIR.exists() and any(GRAPH_DIR.glob("*.png")):
        st.markdown("**Dataset overview:**")
        graph_cols = st.columns(2)
        graphs = sorted(GRAPH_DIR.glob("*.png"))
        for i, g in enumerate(graphs):
            with graph_cols[i % 2]:
                st.image(str(g), use_container_width=True)

st.caption("Built with Streamlit • Dataset-driven, not AI-generated results.")
