import pandas as pd
import sqlite3
import os

CLEANED_PATH = os.path.join("data", "cleaned_supply_chain.csv")
DB_PATH = os.path.join("data", "supply_chain.db")

def load_to_sqlite():
    # Load cleaned data
    df = pd.read_csv(CLEANED_PATH)
    print(f"✅ Loaded cleaned data: {df.shape[0]} rows, {df.shape[1]} columns")

    # Connect to SQLite (acts as local data warehouse)
    conn = sqlite3.connect(DB_PATH)
    
    # Write to SQLite
    df.to_sql("SUPPLY_CHAIN_FACT", conn, if_exists="replace", index=False)
    print(f"✅ Data loaded to local warehouse: {DB_PATH}")

    # Verify
    result = pd.read_sql("SELECT COUNT(*) as total_rows FROM SUPPLY_CHAIN_FACT", conn)
    print(f"✅ Verified: {result['total_rows'][0]} rows in database")

    conn.close()
    print("✅ Load complete!")

if __name__ == "__main__":
    load_to_sqlite()