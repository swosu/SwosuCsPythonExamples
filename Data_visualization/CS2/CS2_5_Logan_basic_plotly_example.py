import streamlit as st
import plotly.express as px
import seaborn as sns
import pandas as pd

# Load dataset
tips = sns.load_dataset("tips")

st.title("Interactive Tip Analysis with Plotly")

# Dropdown to select hue
hue_option = st.selectbox("Color by:", options=["sex", "smoker", "day", "time"])

# Create interactive Plotly scatter plot
fig = px.scatter(
    tips,
    x="total_bill",
    y="tip",
    color=hue_option,
    title="Total Bill vs Tip",
    labels={"total_bill": "Total Bill ($)", "tip": "Tip ($)"}
)

# Show plot
st.plotly_chart(fig)
