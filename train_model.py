import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle

# Create dummy data if CSV is missing, or load it
try:
    df = pd.read_csv("maternal health high risk pregnancy dataset 1.csv")
except FileNotFoundError:
    # Creating a synthetic dataset for demonstration if file not found
    data = {
        'Age': np.random.randint(15, 50, 100),
        'SystolicBP': np.random.randint(90, 160, 100),
        'DiastolicBP': np.random.randint(60, 100, 100),
        'BS': np.random.uniform(6, 15, 100),
        'BodyTemp': np.random.uniform(98, 103, 100),
        'HeartRate': np.random.randint(60, 100, 100),
        'RiskLevel': np.random.choice(['low risk', 'mid risk', 'high risk'], 100)
    }
    df = pd.DataFrame(data)

le = LabelEncoder()
df["RiskLevel"] = le.fit_transform(df["RiskLevel"])
pickle.dump(le, open("label_encoder.pkl", "wb"))

X = df.drop("RiskLevel", axis=1)
y = df["RiskLevel"]
pickle.dump(X.columns.tolist(), open("feature_names.pkl", "wb"))

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf = RandomForestClassifier(random_state=42)
rf.fit(X_train, y_train)

pickle.dump(rf, open("mom_ai_model.pkl", "wb"))
print("Model and encoders saved.")
