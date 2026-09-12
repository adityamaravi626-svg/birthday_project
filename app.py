
import streamlit as st
import pandas as pd
from datetime import date


# ============================================================
# OPERATION BAHU
# Birthday Edition
# Phase 2: Birthday Portal + Navigation
# ============================================================


# ------------------------------------------------------------
# PAGE CONFIGURATION
# ------------------------------------------------------------

st.set_page_config(
    page_title="Operation Bahu 🎂",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ------------------------------------------------------------
# BIRTHDAY INFORMATION
# ------------------------------------------------------------

BIRTHDAY = date(2026, 9, 26)


# ------------------------------------------------------------
# LOAD DATA
# ------------------------------------------------------------

try:

    bahu_df = pd.read_csv(
        "birthday/bahu_interests.csv"
    )

except FileNotFoundError:

    bahu_df = pd.DataFrame({
        "Interest": [
            "Classical Dance",
            "Painting",
            "Flowers",
            "Food"
        ],
        "Interest_Score": [
            90,
            85,
            95,
            100
        ]
    })


# ------------------------------------------------------------
# SIDEBAR NAVIGATION
# ------------------------------------------------------------

st.sidebar.title("🎂 Operation Bahu")

st.sidebar.write(
    "Birthday Edition"
)

st.sidebar.divider()

page = st.sidebar.radio(
    "Navigate",
    [
        "🏠 Home",
        "🌸 Bahu's World",
        "📸 The Trio",
        "🏆 Bahu Awards",
        "🧠 Bahu Quiz",
        "🔮 Birthday Machine",
        "💌 Final Message"
    ]
)

st.sidebar.divider()

st.sidebar.caption(
    "Made with Python + Streamlit"
)


# ============================================================
# HOME PAGE
# ============================================================

if page == "🏠 Home":

    st.title("🎂 Operation  Bahu")

    st.subheader(
        "Birthday Edition"
    )

    st.write(
        "Welcome to the birthday portal of "
        "**Shubhangi aka Bahu** 🌸"
    )

    st.divider()


    # --------------------------------------------------------
    # Birthday Mission
    # --------------------------------------------------------

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
            label="🫂 Family Since",
            value="April 2026"
        )


    st.divider()


    # --------------------------------------------------------
    # Welcome Message
    # --------------------------------------------------------

    st.header("🚀 Mission Brief")

    st.info(
        """
        Someone's birthday is approaching...

        So instead of sending a simple
        "Happy Birthday" message,

        I decided to build an entire
        birthday portal. 😂

        Welcome to **Operation Bahu**.
        """
    )


    # --------------------------------------------------------
    # Countdown
    # --------------------------------------------------------

    today = date.today()

    days_left = (
        BIRTHDAY - today
    ).days


    st.header("⏳ Birthday Countdown")

    if days_left > 0:

        st.metric(
            "Days Until Birthday",
            f"{days_left} days"
        )

        st.progress(
            min(
                1.0,
                max(
                    0.0,
                    1 - days_left / 365
                )
            )
        )

    elif days_left == 0:

        st.balloons()

        st.success(
            "🎉 TODAY IS THE DAY! 🎂"
        )

    else:

        st.success(
            "🎂 Happy Birthday, Bahu!"
        )


    st.divider()


    # --------------------------------------------------------
    # Quick Introduction
    # --------------------------------------------------------

    st.header("✨ What awaits inside?")

    col1, col2 = st.columns(2)

    with col1:

        st.write(
            "🌸 **Bahu's little World**"
        )

        st.write(
            "A little look at the things she loves."
        )

        st.write(
            "A collection of memories of our trio."
        )

        st.write(
            "🏆 **Bahu Awards**"
        )

        st.write(
            "Some very official and definitely legitimate awards."
        )


    with col2:

        st.write(
            "🧠 **Bahu Quiz**"
        )

        st.write(
            "Let's see how well I know her."
        )

        st.write(
            "🔮 **Birthday Machine**"
        )

        st.write(
            "A completely scientific birthday prediction. 😂"
        )

        st.write(
            "💌 **Final Message**"
        )

        st.write(
            "A birthday message from me."
        )


# ============================================================
# BAHU'S WORLD
# ============================================================

elif page == "🌸 Bahu's World":

    st.title("🌸 Bahu's World")

    st.write(
        "A small collection of things that make "
        "Shubhangi, well... Shubhangi."
    )

    st.divider()


    # --------------------------------------------------------
    # Interest Cards
    # --------------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("💃 Classical Dancer")

        st.write(
            "Grace, rhythm and creativity."
        )

        st.progress(0.90)

        st.caption(
            "Dance energy: 90%"
        )


        st.subheader("🎨 Painting")

        st.write(
            "A creative side that deserves "
            "its own gallery."
        )

        st.progress(0.85)

        st.caption(
            "Creative energy: 85%"
        )


    with col2:

        st.subheader("🌸 Flowers")

        st.write(
            "Because flowers somehow make "
            "everything better. And it is way better when it is placed above your ear"
        )

        st.progress(0.95)

        st.caption(
            "Flower appreciation: 95%"
        )


        st.subheader("🍕 Food")

        st.write(
            "This category requires no explanation. 😂"
        )

        st.progress(1.0)

        st.caption(
            "Foodie level: 100%"
        )


    st.divider()


    # --------------------------------------------------------
    # Data Table
    # --------------------------------------------------------

    st.header("📊 Interest Profile")

    st.dataframe(
        bahu_df,
        use_container_width=True,
        hide_index=True
    )


    # --------------------------------------------------------
    # Strongest Interest
    # --------------------------------------------------------

    strongest = bahu_df.loc[
        bahu_df["Interest_Score"].idxmax()
    ]

    st.success(
        f"🏆 Current highest score: "
        f"**{strongest['Interest']}** "
        f"({strongest['Interest_Score']}%)"
    )


# ============================================================
# THE TRIO
# ============================================================

elif page == "📸 The Trio":

    st.title("📸 The Trio")

    st.write(
        "Three people. One friendship. "
        "A questionable amount of nonsense. 😂"
    )

    st.divider()

    st.info(
        """
        📸 This section will contain our
        photos and memories.

        We'll build the complete photo gallery
        in **Phase 4**.
        """
    )

    st.subheader("👨‍💻 + 👨‍🦱 + 👩")

    st.write(
        "**Eddie + Monojeet + Bahu**"
    )

    st.write(
        "Together since April 2026 🫂"
    )


# ============================================================
# BAHU AWARDS
# ============================================================

elif page == "🏆 Bahu Awards":

    st.title("🏆 The Bahu Awards")

    st.write(
        "Some highly prestigious awards "
        "that definitely required no committee approval."
    )

    st.divider()

    awards = {
        "🌸": (
            "Flower Enthusiast Award",
            "For having a special appreciation for flowers."
        ),

        "🎨": (
            "Creative Artist Award",
            "For the painting skills."
        ),

        "💃": (
            "Classical Dance Award",
            "For possessing significantly more grace than the rest of us."
        ),

        "🍕": (
            "Professional Foodie Award",
            "For taking food very seriously."
        )
    
    }

    for icon, (title, description) in awards.items():

        st.subheader(
            f"{icon} {title}"
        )

        st.write(
            description
        )

        st.divider()


# ============================================================
# BAHU QUIZ
# ============================================================

elif page == "🧠 Bahu Quiz":

    st.title("🧠 How Well Do I Know Bahu?")

    st.write(
        "The official unofficial Bahu knowledge test."
    )

    st.divider()

    st.info(
        "🚧 Quiz coming in Phase 6."
    )


# ============================================================
# BIRTHDAY MACHINE
# ============================================================

elif page == "🔮 Birthday Machine":

    st.title("🔮 Birthday Machine")

    st.write(
        "A completely scientific prediction "
        "of what the future holds. 😂"
    )

    st.divider()

    st.info(
        "🚧 Birthday Machine coming in Phase 7."
    )


# ============================================================
# FINAL MESSAGE
# ============================================================

elif page == "💌 Final Message":

    st.title("💌 A Message From Me")

    st.write(
        "The final birthday message will appear here."
    )

    st.divider()

    st.info(
        "🚧 Final message coming in Phase 9."
    )
