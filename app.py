import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Title
st.title("Basic Data Analysis with Pandas & Matplotlib")

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv("data.csv")

data = load_data()

# Display Data
st.subheader("Dataset Overview")
st.write(data)

# Visualizations
st.subheader("Salary Distribution")
plt.figure(figsize=(8, 5))
sns.histplot(data['Salary'], kde=True)
st.pyplot(plt)

st.subheader("Experience vs. Salary")
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Experience_Years', y='Salary', data=data)
st.pyplot(plt)

st.subheader("Correlation Heatmap")
plt.figure(figsize=(8, 5))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
st.pyplot(plt)
