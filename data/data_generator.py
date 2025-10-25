import pandas as pd
import numpy as np

def generate_synthetic_data(n=500):
    np.random.seed(42)
    data = {
        "system_id": [f"SYS_{i:03d}" for i in range(n)],
        "criticality": np.random.randint(1, 6, n),
        "uptime_days": np.random.randint(10, 400, n),
        "last_patch_age_days": np.random.randint(5, 180, n),
        "vulnerability_score": np.random.uniform(0, 10, n).round(2),
        "regulatory_zone": np.random.choice(["Zone A", "Zone B", "Zone C"], n),
        "requires_reboot": np.random.choice([True, False], n),
        "downtime_window_hours": np.random.randint(1, 5, n),
        "predicted_failure_prob": np.random.uniform(0, 1, n).round(2),
    }

    df = pd.DataFrame(data)
    # Define a logic for patch priority (target label)
    df["patch_priority"] = np.where(
        (df["criticality"] >= 4) & 
        (df["vulnerability_score"] > 7) | 
        (df["predicted_failure_prob"] > 0.6),
        2,  # High
        np.where(df["vulnerability_score"] > 4, 1, 0)  # Medium or Low
    )

    df.to_csv("data/patches.csv", index=False)
    print("✅ Synthetic dataset generated: data/patches.csv")

if __name__ == "__main__":
    generate_synthetic_data(1000)
