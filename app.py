import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- PAGE SETUP ---
st.set_page_config(page_title="CORD-19 Data Explorer", layout="wide")
st.title("🧬 CORD-19 Data Explorer")
st.write("Explore COVID-19 research papers using the metadata dataset")

# --- LOAD DATA ---
@st.cache_data
def load_data():
    df = pd.read_csv("metadata_sample.csv")  # use sample if full is large
    df['publish_time'] = pd.to_datetime(df['publish_time'], errors='coerce')
    df['year'] = df['publish_time'].dt.year
    return df

df = load_data()

st.subheader("🔍 Dataset Preview")
st.dataframe(df.head())

# --- FILTERS ---
years = df['year'].dropna().unique()
years.sort()
year_range = st.slider("Select Year Range", int(min(years)), int(max(years)), (2020, 2021))

filtered_df = df[(df['year'] >= year_range[0]) & (df['year'] <= year_range[1])]

# --- VISUALIZATIONS ---
st.subheader("📅 Publications by Year")
year_counts = filtered_df['year'].value_counts().sort_index()

fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x=year_counts.index, y=year_counts.values, ax=ax)
ax.set_title('Publications by Year')
ax.set_xlabel('Year')
ax.set_ylabel('Count')
st.pyplot(fig)

st.subheader("🏛️ Top Journals")
top_journals = filtered_df['journal'].value_counts().head(10)

fig, ax = plt.subplots(figsize=(8, 4))
sns.barplot(x=top_journals.values, y=top_journals.index, ax=ax)
ax.set_title('Top 10 Journals')
ax.set_xlabel('Number of Papers')
ax.set_ylabel('Journal')
st.pyplot(fig)

st.success("✅ Dashboard loaded successfully!")
