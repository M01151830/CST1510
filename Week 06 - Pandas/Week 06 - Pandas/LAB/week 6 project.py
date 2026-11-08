"""
RECORD CHECK  -  my version
===========================

Name  :JOASH KABACHI
Lane  :   IT      
Date  :11/8/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""
import pandas as pd
import matplotlib.pyplot as plt

# ================= LOAD =================
# Read the CSV file and store the data in a DataFrame called df
df = pd.read_csv("Week 06 - Pandas/LAB/servers.csv")
# ================= PROCESS =================
# Calculate the percentage of storage used
df["percent"] = df["used_gb"] / df["total_gb"] * 100

# Check each percentage and assign a status
# 100% or more = OVER LIMIT, 90% or more = WARNING, otherwise = OK
df["status"] = df["percent"].apply(
    lambda x: "OVER LIMIT" if x >= 100 else ("WARNING" if x >= 90 else "OK")
)


# ================= OUTPUT =================
# Display the complete DataFrame
print("== Full DataFrame ==")
print(df)

# Filter the DataFrame to show only servers that are not OK
# != means not equal to
print("\n== Filtered DataFrame (Not 'OK') ==")
not_ok_df = df[df["status"] != "OK"]
print(not_ok_df)