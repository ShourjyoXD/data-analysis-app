import streamlit as st
import pandas as pd
from data_cleaning import load_data, clean_data
from data_analysis import visualize_data

st.title("📊 Basic Data Analysis with Pandas & Matplotlib")
st.write("Analyze your data effortlessly with this interactive app!")

uploaded_file = st.file_uploader("Upload your CSV file", type=['csv'])

if uploaded_file is not None:
    df = load_data(uploaded_file)

    st.subheader("📋 Raw Data")
    st.write(df)

    df_cleaned = clean_data(df)
    st.subheader("🧹 Cleaned Data")
    st.write(df_cleaned)

    st.subheader("📈 Statistics")
    st.write(df_cleaned.describe())

    st.subheader("📊 Visualizations")
    heatmap_fig = visualize_data(df_cleaned)
    st.pyplot(heatmap_fig)

    st.subheader("💡 Insights")
    st.write("Based on the visualizations, here are some insights...")

else:
    st.warning("Please upload a CSV file to proceed.")
