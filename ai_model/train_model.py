import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib

# Load dataset
df = pd.read_csv("data/patches.csv")

# Features and labels
X = df.drop(columns=["system_id", "patch_priority"])
y = df["patch_priority"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model training
model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "model/model.pkl")
print("✅ Model trained and saved as model/model.pkl")
