import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.title("Basic Data Analysis with Pandas & Matplotlib")


@st.cache_data
def load_data():
    return pd.read_csv("data.csv")

data = load_data()


st.subheader("Dataset Overview")
st.write(data)

def plot_histogram():
    st.subheader("Salary Distribution")
    plt.figure(figsize=(8, 5))
    sns.histplot(data['Salary'].dropna(), kde=True)
    st.pyplot(plt)


def plot_scatter():
    st.subheader("Experience vs. Salary")
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x='Experience_Years', y='Salary', data=data)
    st.pyplot(plt)


def plot_heatmap():
    st.subheader("Correlation Heatmap")
    numeric_data = data.select_dtypes(include=['float64', 'int64'])
    plt.figure(figsize=(8, 5))
    sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm')
    st.pyplot(plt)


plot_histogram()
plot_scatter()
plot_heatmap()
