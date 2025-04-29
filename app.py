import streamlit as st
import pandas as pd

# 1. Page config
st.set_page_config(page_title="CFIB Confidence Tracker", layout="wide")

# 2. Load data
@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/national_index.csv", parse_dates=["date"])
    return df

df = load_data()

# 3. Sidebar: pick metric
st.sidebar.header("Filter")
metrics = df["metric"].unique().tolist()
choice_metric = st.sidebar.selectbox("Choose metric", metrics)

# 4. Filter for your metric
plot_df = df[df["metric"] == choice_metric]

# 5. Title & chart
st.title("CFIB Business Barometer Confidence (Canada)")
st.subheader(choice_metric)
chart_data = plot_df.set_index("date")["value"]
st.line_chart(chart_data)

# 6. Show raw table
if st.checkbox("Show data table"):
    st.dataframe(plot_df[["date", "value"]].rename(columns={"value": choice_metric}))
