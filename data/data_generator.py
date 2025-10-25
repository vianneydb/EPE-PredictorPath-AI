import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# ----------------------------
# CONFIG
# ----------------------------
n = 1000
output_dir = "/workspaces/EPE-PredictorPath-AI/data"
np.random.seed(42)

# True directory
os.makedirs(output_dir, exist_ok=True)

# ----------------------------
# DATA GENERATOR
# ----------------------------
today = datetime.now()

# Fechas válidas
last_patch_dates = [
    (today - timedelta(days=int(x))).strftime("%Y-%m-%d")
    for x in np.random.randint(5, 180, n)
]
next_maintenance_windows = [
    (today + timedelta(days=int(x))).strftime("%Y-%m-%d")
    for x in np.random.randint(1, 60, n)
]

# Crear diccionario de datos
data = {
    "System ID": [f"SYS-{i:03d}" for i in range(1, n + 1)],
    "Regulatory Zone": np.random.choice(["Zone A", "Zone B", "Zone C"], n),
    "Criticality Level (1-5)": np.random.randint(1, 6, n),
    "Uptime (days)": np.random.randint(10, 400, n),
    "Last Patch Date": last_patch_dates,
    "Next Available Window": next_maintenance_windows,
    "Downtime Window (hours)": np.random.randint(1, 5, n),
    "Requires Reboot": np.random.choice(["Yes", "No"], n),
    "Vulnerability Score (0-10)": np.random.uniform(0, 10, n).round(2),
    "Predicted Failure Probability": np.random.uniform(0, 1, n).round(2),
}

# DataFrame
df = pd.DataFrame(data)

# ----------------------------
# CLASSIFICATION
# ----------------------------
conditions_high = (
    (df["Criticality Level (1-5)"] >= 4)
    & ((df["Vulnerability Score (0-10)"] > 7)
       | (df["Predicted Failure Probability"] > 0.6))
)

conditions_medium = (
    (df["Vulnerability Score (0-10)"].between(4, 7))
    | (df["Predicted Failure Probability"].between(0.3, 0.6))
)

df["Patch Priority"] = np.select(
    [conditions_high, conditions_medium],
    ["High", "Medium"],
    default="Low"
)

# ----------------------------
# SAVE
# ----------------------------
ordered_cols = [
    "System ID",
    "Regulatory Zone",
    "Criticality Level (1-5)",
    "Uptime (days)",
    "Last Patch Date",
    "Next Available Window",
    "Downtime Window (hours)",
    "Requires Reboot",
    "Vulnerability Score (0-10)",
    "Predicted Failure Probability",
    "Patch Priority",
]

df = df[ordered_cols]

# Guardar archivo con tabulaciones
output_path = os.path.join(output_dir, "patches.tsv")
df.to_csv(output_path, index=False, sep="\t")

print(f"✅ Synthetic dataset generated successfully: {output_path}")
print(df.head(10).to_string(index=False))