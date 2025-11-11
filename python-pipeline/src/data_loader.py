import pandas as pd

def load_csv(filepath):
    df = pd.read_csv(filepath)
    return df

if __name__ == "__main__":
    filepath = "../data/raw/Bells Palsy Clinical Trial.csv"
    df = load_csv(filepath)
    print(f"Shape: {df.shape}")
    print(df.head())