import pandas as pd
import os

# Load raw data
RAW_PATH = os.path.join("data", "DataCoSupplyChainDataset.csv")

def extract_data():
    df = pd.read_csv(RAW_PATH, encoding='latin-1')
    print(f"✅ Data loaded: {df.shape[0]} rows, {df.shape[1]} columns")
    print(df.head())
    return df

if __name__ == "__main__":
    df = extract_data()