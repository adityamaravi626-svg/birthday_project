
import streamlit as st
import pandas as pd

# ============================================================
# OPERATION Birthday - BIRTHDAY EDITION
# Phase 1: Data Foundation
# ============================================================

# ------------------------------------------------------------
# Page Configuration
# ------------------------------------------------------------

st.set_page_config(
    page_title="Operation Birthday 🎂",
    page_icon="🌸",
    layout="wide"
)


# ------------------------------------------------------------
# Title Section
# ------------------------------------------------------------

st.title("🎂 Operation Bahu")

st.subheader("Birthday Edition")

st.write(
    "Welcome to the birthday portal of "
    "**Shubhangi aka Bahu** 🌸"
)

st.divider()


# ------------------------------------------------------------
# Birthday Information
# ------------------------------------------------------------

st.header("🎉 Birthday Mission")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="🎂 Birthday",
        value="26 September"
    )

with col2:
    st.metric(
        label="🌸 Codename",
        value="Bahu"
    )

with col3:
    st.metric(
        label="📅 Since",
        value="April 2026"
    )


st.divider()


# ------------------------------------------------------------
# Interest Profile
# ------------------------------------------------------------

st.header("🌸 Bahu's Interest Profile")

st.write(
    "A fun representation of the interests I know about Bahu."
)


# Load dataset

try:

    bahu_df = pd.read_csv(
        "birthday/bahu_interests.csv"
    )

    # Display dataset

    st.dataframe(
        bahu_df,
        use_container_width=True,
        hide_index=True
    )

    # Bar chart

    st.subheader("📊 Interest Analysis")

    chart_data = bahu_df.set_index("Interest")

    st.bar_chart(
        chart_data
    )

except FileNotFoundError:

    st.error(
        "⚠️ Dataset not found. "
        "Make sure bahu_interests.csv is inside the data folder."
    )


st.divider()


# ------------------------------------------------------------
# Known Interests
# ------------------------------------------------------------

st.header("✨ Known About Bahu")

col1, col2 = st.columns(2)

with col1:

    st.write("💃 **Classical Dancer**")

    st.write(
        "Grace, rhythm and creativity."
    )

    st.write("🎨 **Painting**")

    st.write(
        "A creative side that deserves its own gallery."
    )


with col2:

    st.write("🌸 **Flowers**")

    st.write(
        "Clearly an important part of the Bahu universe."
    )

    st.write("🍕 **Foodie**")

    st.write(
        "Food deserves serious attention. 😂"
    )


st.divider()


# ------------------------------------------------------------
# Mission Status
# ------------------------------------------------------------

st.header("🚀 Mission Status")

st.success(
    "Birthday Mission Activated Successfully!"
)

st.info(
    "Phase 1 complete: Data foundation and Streamlit dashboard."
)


# ------------------------------------------------------------
# Footer
# ------------------------------------------------------------

st.caption(
    "Operation Bahu | Birthday Edition 🎂 | "
    "Created with Python + Streamlit"
)
