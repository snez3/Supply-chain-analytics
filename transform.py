import pandas as pd
import os

RAW_PATH = os.path.join("data", "DataCoSupplyChainDataset.csv")

def transform_data():
    df = pd.read_csv(RAW_PATH, encoding='latin-1')
    
    # 1. Drop unnecessary columns
    drop_cols = ['Product Description', 'Customer Password', 'Customer Email', 'Customer Fname', 'Customer Lname']
    df = df.drop(columns=[c for c in drop_cols if c in df.columns])
    
    # 2. Drop duplicates
    df = df.drop_duplicates()
    
    # 3. Handle missing values
    df = df.dropna(subset=['Order Id'])
    
    # 4. Create new feature — Shipping Delay (actual vs scheduled)
    df['Shipping Delay'] = df['Days for shipment (scheduled)'] - df['Days for shipping (real)']
    
    # 5. Flag late deliveries
    df['Is Late'] = df['Delivery Status'].apply(lambda x: 1 if 'Late' in str(x) else 0)
    
    # 6. Save cleaned data
    output_path = os.path.join("data", "cleaned_supply_chain.csv")
    df.to_csv(output_path, index=False)
    
    print(f"✅ Transformed: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"✅ Saved to {output_path}")
    return df

if __name__ == "__main__":
    df = transform_data()