import os
import pandas as pd
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_sERVICE_ROLE_KEY")
TABLE_NAME = os.getenv("SUPABASE_TABLE", "patches")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

df = pd.read_csv("/vianneydb/EPE-PredictorPath-AI/data/patches.tsc", sep="\t")

df.columns = [
  "system_id",
  "regulatory_zone",
  "criticality_level",
  "uptime_days",
  "last_patch_date",
  "next_available_window",
  "downtime_window_hours",
  "requires_reboot",
  "vulnerability_score",
  "predicted_failure_probability",
  "patch_priority",
]

df["last_patch_date"] = pd.to_datetime(df["last_patch_date"])
df["next_available_window"] = pd.to_datetime(df["next_available_window"])

batch_size = 100
for i in range(0, len(df), batch_size):
  batch = df.iloc[i:i + batch_size].to_dict(orient="records")
  data, count = supabase.table("ProtectorPath_Table").insert(batch).execute()
  print(f"Uploaded rows {i}-{i + len(batch) - 1}")

print("All data uploaded successfully to Supabase!")
