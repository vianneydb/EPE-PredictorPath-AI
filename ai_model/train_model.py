import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib

# Load dataset
df = pd.read_csv("data/patches.tsv", sep="\t")

# Convert dates to numeric features
df["Last Patch Age (days)"] = (pd.to_datetime("today") - pd.to_datetime(df["Last Patch Date"])).dt.days
df["Days Until Next Window"] = (pd.to_datetime(df["Next Available Window"]) - pd.to_datetime("today")).dt.days

# Encode categorical variables
df_encoded = pd.get_dummies(df, columns=["Regulatory Zone", "Requires Reboot"], drop_first=True)

# Features and target
X = df_encoded.drop(columns=["System ID", "Patch Priority", "Last Patch Date", "Next Available Window"])
y = df_encoded["Patch Priority"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = DecisionTreeClassifier(max_depth=5, random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "ai_model/model.pkl")
print("Model trained and saved as model/model.pkl")