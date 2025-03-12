import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def visualize_data(df):
    plt.figure(figsize=(8, 5))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt='.2f')
    plt.title('Correlation Heatmap')
    return plt
