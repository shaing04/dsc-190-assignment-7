import pandas as pd
from dateutil import parser as dateparser
import sys

VALID_EVENT_TYPES = {"click", "login", "purchase", "scroll", "view"}

def normalize_timestamp(ts):
    try:
        return dateparser.parse(str(ts)).strftime("%Y-%m-%dT%H:%M:%S")
    except Exception:
        return None

df = pd.read_csv("data/raw/events.csv")

# Drop rows with any missing fields
df = df.dropna()

# Drop rows with invalid event_type
df = df[df["event_type"].isin(VALID_EVENT_TYPES)]

# Drop rows with non-positive duration_seconds
df["duration_seconds"] = pd.to_numeric(df["duration_seconds"], errors="coerce")
df = df.dropna(subset=["duration_seconds"])
df = df[df["duration_seconds"] > 0]
df["duration_seconds"] = df["duration_seconds"].astype(int)

# Normalize timestamp
df["timestamp"] = df["timestamp"].apply(normalize_timestamp)
df = df.dropna(subset=["timestamp"])

import os
os.makedirs("data/clean", exist_ok=True)

df.to_csv("data/clean/events.csv", index=False)
print(f"Clean: {len(df)} rows written to data/clean/events.csv")
