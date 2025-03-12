import pandas as pd

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def clean_data(df):
    # Example cleaning steps
    df_cleaned = df.drop_duplicates().dropna()
    return df_cleaned
