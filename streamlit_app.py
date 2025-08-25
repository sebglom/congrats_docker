import os
from pathlib import Path

import streamlit as st

# Determine ASCII art path relative to this file or via ART environment variable
DEFAULT_ART = Path(__file__).with_name("ascii.txt")
ART_PATH = Path(os.environ.get("ART", DEFAULT_ART))
MSG = os.environ.get("MSG", "Congratulations Dr. Lennart Schürmann!")

# Read ASCII art
art = ART_PATH.read_text(encoding="utf-8")

# Render using Streamlit
st.text(art)
st.markdown(f"**{MSG}**")
