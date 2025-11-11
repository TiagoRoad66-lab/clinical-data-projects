"""
Data Explorer - Explore and profile the data
"""

import pandas as pd
from data_loader import load_csv


def get_basic_info(df):
    """
    Print basic information about the DataFrame
    
    Args:
        df: pandas DataFrame
    """
    print("=== BASIC INFO ===")
    print(f"Shape: {df.shape}")
    print(f"\nColumn names:\n{df.columns.tolist()}")
    print(f"\nData types:\n{df.dtypes}")
    print(f"\nMissing values:\n{df.isnull().sum()}")


def get_summary_stats(df):
    """
    Show summary statistics
    
    Args:
        df: pandas DataFrame
    """
    print("\n=== SUMMARY STATISTICS ===")
    print(df.describe())


if __name__ == "__main__":
    # Load the data
    filepath = "../data/raw/Bells Palsy Clinical Trial.csv"
    df = load_csv(filepath)
    
    if df is not None:
        get_basic_info(df)
        get_summary_stats(df)