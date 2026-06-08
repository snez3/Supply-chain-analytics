import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os

CLEANED_PATH = os.path.join("data", "cleaned_supply_chain.csv")

def train_model():
    df = pd.read_csv(CLEANED_PATH)
    print(f"✅ Data loaded: {df.shape[0]} rows")

    # Features for prediction
    features = [
        'Days for shipping (real)',
        'Days for shipment (scheduled)',
        'Order Item Quantity',
        'Order Item Discount Rate',
        'Order Item Profit Ratio',
        'Sales',
        'Shipping Delay'
    ]

    # Target
    target = 'Is Late'

    # Drop nulls
    df = df[features + [target]].dropna()

    X = df[features]
    y = df[target]

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print(f"✅ Train: {X_train.shape[0]} rows, Test: {X_test.shape[0]} rows")

    # Train Random Forest
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    print("✅ Model trained!")

    # Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"\n🎯 Model Accuracy: {accuracy * 100:.2f}%")
    print("\n📊 Classification Report:")
    print(classification_report(y_test, y_pred))

    # Feature importance
    importance = pd.DataFrame({
        'Feature': features,
        'Importance': model.feature_importances_
    }).sort_values('Importance', ascending=False)
    print("\n🔑 Feature Importance:")
    print(importance)

    # Save model
    joblib.dump(model, os.path.join("models", "delay_model.pkl"))
    print("\n✅ Model saved to models/delay_model.pkl")

if __name__ == "__main__":
    train_model()