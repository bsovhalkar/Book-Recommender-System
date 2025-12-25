import streamlit as st
from recommend import recommend
import pandas as pd

st.set_page_config(page_title="Book Recommender", page_icon="📚", layout="wide")

df = pd.read_pickle("final_rating.pkl")

st.sidebar.title("📚 Book Recommendation System")

selected_book = st.sidebar.selectbox(
    "Select a Book",
    sorted(df['title'].dropna().unique())
)

if st.sidebar.button("✨ Recommend"):
    rec_df = recommend(selected_book).iloc[1:, :]

    st.subheader(f"📌 Books similar to **{selected_book}**")

    for _, row in rec_df.iterrows():
        st.markdown("---")

        col1, col2 = st.columns([3, 1])

        with col1:
            st.markdown(f"### 📘 {row['title']}")
            st.write(f"**Author:** {row['author']}")
            st.write(f"**Publisher:** {row['publisher']} ({row['year']})")

        with col2:
            st.metric(
                label="⭐ Average Ratings",
                value=int(row['avg_rating'])
            )
            st.write(f"**How Many People Rated:** {row['no_of_rating']}")


else:
    st.info("👈 Select a book from the sidebar and click **Recommend**")
