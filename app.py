import streamlit as st
import pandas as pd
from datetime import date


# ============================================================
# OPERATION BAHU
# Birthday Edition
# ============================================================


# ------------------------------------------------------------
# PAGE CONFIGURATION
# ------------------------------------------------------------

st.set_page_config(
    page_title="Operation Birthday 🎂",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ------------------------------------------------------------
# BIRTHDAY INFORMATION
# ------------------------------------------------------------

BIRTHDAY = date(2026, 9, 26)


# ------------------------------------------------------------
# LOAD INTEREST DATA
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


# ============================================================
# SIDEBAR
# ============================================================

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
# HOME
# ============================================================

if page == "🏠 Home":

    st.title("🎂 Operation Bahu")

    st.subheader("Birthday Edition")

    st.write(
        "Welcome to the birthday portal of "
        "**Shubhangi aka Bahu** 🌸"
    )

    st.divider()

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

    st.header("🚀 Mission Brief")

    st.info(
        """
        Someone's birthday is approaching...

        So instead of sending a simple
        "Happy Birthday" message,

        we decided to build an entire
        birthday portal. 😂

        Welcome to **Operation Bahu**.
        """
    )

    st.divider()

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

    st.header("✨ What awaits inside?")

    col1, col2 = st.columns(2)

    with col1:

        st.write("🌸 **Bahu's World**")

        st.write(
            "A little look at the things you loves."
        )

        st.write("📸 **The Trio**")

        st.write(
            "A collection of memories from our trio."
        )

        st.write("🏆 **Bahu Awards**")

        st.write(
            "Some very official and definitely legitimate awards."
        )

    with col2:

        st.write("🧠 **Bahu Quiz**")

        st.write(
            "Let's see how well I know you."
        )

        st.write("🔮 **Birthday Machine**")

        st.write(
            "A completely scientific birthday prediction. 😂"
        )

        st.write("💌 **Final Message**")

        st.write(
            "A birthday message from Me."
        )


# ============================================================
# BAHU'S WORLD
# ============================================================

elif page == "🌸 Bahu's World":

    st.title("🌸 Bahu's World")

    st.subheader(
        "A little world built around the things she loves."
    )

    st.write(
        "Based on what I actually know about Shubhangi, "
        "these are the four things that define this section."
    )

    st.divider()

    # --------------------------------------------------------
    # TOP INTEREST METRICS
    # --------------------------------------------------------

    st.header("✨ The Four Pillars of Bahu")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "💃 Dance",
            "90%"
        )

    with col2:

        st.metric(
            "🎨 Painting",
            "85%"
        )

    with col3:

        st.metric(
            "🌸 Flowers",
            "95%"
        )

    with col4:

        st.metric(
            "🍕 Foodie",
            "100%"
        )

    st.divider()

    # --------------------------------------------------------
    # INTEREST EXPLORER
    # --------------------------------------------------------

    st.header("🔍 Explore Bahu's Interests")

    selected_interest = st.selectbox(
        "Choose an interest",
        [
            "💃 Classical Dance",
            "🎨 Painting",
            "🌸 Flowers",
            "🍕 Food"
        ]
    )

    interest_information = {

        "💃 Classical Dance": {

            "title": "💃 Classical Dance",

            "score": 90,

            "message": (
                "Grace, rhythm and expression. "
                "This is where art meets movement."
            ),

            "emoji": "💃"
        },

        "🎨 Painting": {

            "title": "🎨 Painting",

            "score": 85,

            "message": (
                "A creative side that turns a blank "
                "canvas into something personal."
            ),

            "emoji": "🎨"
        },

        "🌸 Flowers": {

            "title": "🌸 Flowers",

            "score": 95,

            "message": (
                "Some things simply make a day "
                "look a little more beautiful."
            ),

            "emoji": "🌸"
        },

        "🍕 Food": {

            "title": "🍕 Food",

            "score": 100,

            "message": (
                "Important research finding: "
                "Bahu is a certified foodie. 😂"
            ),

            "emoji": "🍕"
        }
    }

    selected = interest_information[
        selected_interest
    ]

    st.subheader(
        selected["title"]
    )

    st.write(
        selected["message"]
    )

    st.progress(
        selected["score"] / 100
    )

    st.caption(
        f"Fun project score: {selected['score']}%"
    )

    st.divider()

    # --------------------------------------------------------
    # INTEREST DATA
    # --------------------------------------------------------

    st.header("📊 Bahu's Interest Profile")

    st.dataframe(
        bahu_df,
        use_container_width=True,
        hide_index=True
    )

    st.subheader(
        "📈 Interest Comparison"
    )

    chart_data = bahu_df.set_index(
        "Interest"
    )

    st.bar_chart(
        chart_data
    )

    st.divider()

    # --------------------------------------------------------
    # STRONGEST INTEREST
    # --------------------------------------------------------

    strongest = bahu_df.loc[
        bahu_df["Interest_Score"].idxmax()
    ]

    st.success(
        f"🏆 According to our completely unofficial "
        f"birthday analysis, **{strongest['Interest']}** "
        f"currently holds the highest score at "
        f"**{strongest['Interest_Score']}%**."
    )

    st.divider()

    # --------------------------------------------------------
    # BAHU FORMULA
    # --------------------------------------------------------

    st.header("🧪 The Totally Unofficial Bahu Formula")

    st.write(
        "After extensive research conducted by absolutely "
        "unqualified scientists..."
    )

    formula_col1, formula_col2 = st.columns(2)

    with formula_col1:

        st.write("💃 Dance")

        st.write("🎨 Painting")

    with formula_col2:

        st.write("🌸 Flowers")

        st.write("🍕 Food")

    st.info(
        "🌸 + 🎨 + 💃 + 🍕 = **Bahu**"
    )

    st.caption(
        "Disclaimer: This formula has absolutely no scientific basis. 😂"
    )


# ============================================================
# THE TRIO
# ============================================================

elif page == "📸 The Trio":

    st.title("📸 The Trio")

    st.subheader(
        "Three people. One Friendship. Beginning of Memories. 🫂"
    )

    st.write(
        "A little collection of moments from "
        "April 2026 onwards."
    )

    st.divider()

    st.header("👨‍💻 + 👨‍🦱 + 👩")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "👨‍💻",
            "Aditya aka Eddie"
        )

    with col2:

        st.metric(
            "👨‍🦱",
            "Monojeet aka Mohit"
        )

    with col3:

        st.metric(
            "👩",
            "Shubhangi aka Bahu"
        )

    st.info(
        """
        **The Unofficial Trio**

        Somewhere around April 2026, this trio
        started collecting memories.

        And apparently, I decided those memories
        deserved their own webpage. 😂
        """
    )

    st.divider()

    # --------------------------------------------------------
    # PHOTO GALLERY
    # --------------------------------------------------------

    st.header("📸 Our Memories")

    st.write(
        "A few moments from the trio."
    )

    import os

    image_folder = "Memories"

    image_files = []

    if os.path.exists(image_folder):

        for filename in sorted(
            os.listdir(image_folder)
        ):

            if filename.lower().endswith(
                (".jpg", ".jpeg", ".png", ".webp")
            ):

                image_files.append(
                    os.path.join(
                        image_folder,
                        filename
                    )
                )

    if image_files:

        image_files = image_files[:9]

        for i in range(
            0,
            len(image_files),
            3
        ):

            row = image_files[i:i + 3]

            columns = st.columns(3)

            for offset, (column, image_path) in enumerate(
                zip(columns, row)
            ):

                photo_number = i + offset + 1

                with column:

                    st.image(
                        image_path,
                        use_container_width=True
                    )

                    st.caption(
                        f"📸 Memory #{photo_number}"
                    )

    else:

        st.warning(
            """
            📸 No photos found yet.

            Add your trio photos inside:

            `Memories/`

            Then refresh the app.
            """
        )

    st.divider()

    # --------------------------------------------------------
    # TRIO STATISTICS
    # --------------------------------------------------------

    st.header("📊 Official Trio Statistics")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "👥 People",
            "3"
        )

    with col2:

        st.metric(
            "📅 Together Since",
            "April 2026"
        )

    with col3:

        st.metric(
            "🎂 Birthday",
            "26 September"
        )

    st.divider()

    # --------------------------------------------------------
    # MEMORY MESSAGE
    # --------------------------------------------------------

    st.header("💭 One Simple Thought")

    st.success(
        """
        Some memories don't need a huge photo album.

        Sometimes a few pictures,
        a few conversations,
        and the right people
        are enough.

        Here's to the memories we've already made
        and the ones still waiting for us. 🫂
        """
    )


# ============================================================
# BAHU AWARDS
# ============================================================

elif page == "🏆 Bahu Awards":

    st.title("🏆 The Bahu Awards")

    st.subheader(
        "The most prestigious unofficial awards of the year. 😂"
    )

    st.write(
        "No committee was involved. "
        "No nominations were required. "
        "The results are completely final. 🏆"
    )

    st.divider()

    # --------------------------------------------------------
    # AWARDS
    # --------------------------------------------------------

    awards = {

        "🌸 Flower Enthusiast Award": {

            "emoji": "🌸",

            "reason": (
                "For having a special appreciation "
                "for flowers."
            )
        },

        "🎨 Creative Artist Award": {

            "emoji": "🎨",

            "reason": (
                "For her love of painting and creativity."
            )
        },

        "💃 Classical Dance Award": {

            "emoji": "💃",

            "reason": (
                "For bringing grace, rhythm and "
                "expression through classical dance."
            )
        },

        "🍕 Professional Foodie Award": {

            "emoji": "🍕",

            "reason": (
                "For taking food very seriously. "
                "A completely deserved award. 😂"
            )
        },

        "🫂 Official Trio Member Award": {

            "emoji": "🫂",

            "reason": (
                "For becoming part of the gang since April 2026."
            )
        }
    }

    # --------------------------------------------------------
    # AWARD EXPLORER
    # --------------------------------------------------------

    st.header("🎖️ Award Ceremony")

    selected_award = st.selectbox(
        "Choose an award to reveal",
        list(awards.keys())
    )

    award = awards[selected_award]

    st.divider()

    # --------------------------------------------------------
    # AWARD REVEAL
    # --------------------------------------------------------

    st.subheader(
        f"{award['emoji']} {selected_award}"
    )

    st.success(
        "🏆 Award officially presented to "
        "**Shubhangi aka Bahu**!"
    )

    st.write(
        f"**Why?** {award['reason']}"
    )

    st.divider()

    # --------------------------------------------------------
    # FINAL AWARD
    # --------------------------------------------------------

    st.header("🎉 And the most important award...")

    st.info(
        """
        🏆 **THE OFFICIAL TRIO MEMBER AWARD**

        Presented to:

        **Shubhangi aka Bahu** 🌸

        For becoming an important part of our trio
        and for all the memories we've collected
        since April 2026. 🫂
        """
    )

    st.balloons()


# ============================================================
# BAHU QUIZ
# ============================================================

elif page == "🧠 Bahu Quiz":

    st.title("🧠 How Well Do I Know Bahu?")

    st.write(
        "The official unofficial Bahu knowledge test."
    )

    st.divider()
# ============================================================
# QUIZ QUESTIONS
# ============================================================
 st.header("📝 The Quiz")

    q1 = st.radio(
        "1️⃣ When is Bahu's birthday?",
        [
            "20 September",
            "24 September",
            "26 September",
            "30 September"
        ],
        key="q1"
    )

    q2 = st.radio(
        "2️⃣ What is the favorite food of bahu?",
        [
            "CheeseCake",
            "Maggi",
            "MatarPaneer",
            "RedSaucePasta"
        ],
        key="q2"
    )

    q3 = st.radio(
        "3️⃣ What is the favorite song of bahu?",
        [
            "Barsaat",
            "Aaj din chadheya",
            "Apna bana le",
            "Kesariya"
        ],
        key="q3"
    )

    q4 = st.radio(
        "4️⃣ What is the favorite flower of bahu?",
        [
            "Rose",
            "Sunflower",
            "Mariegold",
            "Lily"
        ],
        key="q4"
    )

    q5 = st.radio(
        "5️⃣ What is Shubhangi's project codename?",
        [
            "Boss",
            "Bahu",
            "Captain",
            "Queen"
        ],
        key="q5"
    )

    st.divider()
# ============================================================
# SUBMIT QUIZ
# ============================================================
if st.button(
        "🎯 Submit Quiz",
        use_container_width=True
    ):

        score = 0

        # Correct answers

        if q1 == "26 September":
            score += 1

        if q2 == "CheeseCake":
            score += 1

        if q3 == "Aaj din chadheya":
            score += 1

        if q4 == "Lily":
            score += 1

        if q5 == "Bahu":
            score += 1

        st.divider()
# ============================================================
# RESULT
#=============================================================
st.header("🏆 Your Result")

        st.metric(
            "Your Score",
            f"{score} / 5"
        )

        if score == 5:

            st.balloons()

            st.success(
                """
                🏆 PERFECT SCORE!

                Okay, if all the answer i filled are correct. Then i know about bahu 😂.
                """
            )

        elif score >= 3:

            st.success(
                f"""
                🎉 Good job!

                You scored {score}/5.

                if my few answer are correct. then i know few about bahu. 🤏 
                """
            )

        elif score >= 1:

            st.warning(
                f"""
                😂 You scored {score}/5.

                I need to do revision of the Bahu database.
                """
            )

        else:

            st.error(
                """
                😭 0/5!

                I seriously have zero knowledge about bahu.😭
                """
            )

        st.divider()

        st.caption(
            "Quiz officially certified by absolutely nobody. 😂"
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

    st.title("💌 A Message From Us")

    st.write(
        "The final birthday message will appear here."
    )

    st.divider()

    st.info(
        "🚧 Final message coming in Phase 9."
    )
