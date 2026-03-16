import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import joblib

def generate_mock_data(n_samples=1000):
    """Simulates sensor data for predictive maintenance."""
    np.random.seed(42)
    X = np.random.rand(n_samples, 5) * 100 # 5 sensor features
    # Synthetic logic: higher sensor values increase failure probability
    y = (X.sum(axis=1) > 250).astype(int) 
    return X, y

def train_model():
    print("🚀 Initiating Model Training Pipeline...")
    X, y = generate_mock_data(5000)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    print("\n📊 Model Evaluation:")
    print(classification_report(y_test, y_pred))
    
    cm = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:")
    print(cm)

    # Save model
    joblib.dump(model, "model_artifact.pkl")
    print("✅ Model saved as model_artifact.pkl")
    
    return cm

if __name__ == "__main__":
    train_model()
