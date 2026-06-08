import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

CLEANED_PATH = os.path.join("data", "cleaned_supply_chain.csv")
OUTPUT_PATH = os.path.join("dashboard")

def run_eda():
    df = pd.read_csv(CLEANED_PATH)
    print(f"✅ Data loaded: {df.shape[0]} rows, {df.shape[1]} columns")

    # 1. Basic stats
    print("\n📊 Basic Statistics:")
    print(df[['Order Item Profit Ratio', 'Order Item Quantity', 'Days for shipping (real)', 
          'Days for shipment (scheduled)', 'Sales']].describe())

    # 2. Late delivery rate
    late_rate = df['Is Late'].mean() * 100
    print(f"\n🚨 Late Delivery Rate: {late_rate:.2f}%")

    # 3. Plot 1 - Delivery Status Distribution
    plt.figure(figsize=(10, 5))
    df['Delivery Status'].value_counts().plot(kind='bar', color='steelblue')
    plt.title('Delivery Status Distribution')
    plt.xlabel('Status')
    plt.ylabel('Count')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_PATH, 'delivery_status.png'))
    print("✅ Saved delivery_status.png")

    # 4. Plot 2 - Profit by Market
    plt.figure(figsize=(10, 5))
    df.groupby('Market')['Sales'].sum().sort_values().plot(kind='barh', color='green')
    plt.title('Total Profit by Market')
    plt.xlabel('Profit')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_PATH, 'profit_by_market.png'))
    print("✅ Saved profit_by_market.png")

    # 5. Plot 3 - Shipping Delay Distribution
    plt.figure(figsize=(10, 5))
    sns.histplot(df['Shipping Delay'].dropna(), bins=30, color='orange')
    plt.title('Shipping Delay Distribution')
    plt.xlabel('Delay (days)')
    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_PATH, 'shipping_delay.png'))
    print("✅ Saved shipping_delay.png")

    plt.close('all')
    print("\n✅ EDA Complete!")

if __name__ == "__main__":
    run_eda()