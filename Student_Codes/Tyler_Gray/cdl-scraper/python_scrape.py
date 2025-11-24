import requests
import pandas as pd

URL = "https://www.breakingpoint.gg/api/trpc/..."  # paste from DevTools

headers = {
    "accept": "*/*",
    "referer": "https://www.breakingpoint.gg/stats/advanced?timePeriod=2026&orderBy=kd",
}

resp = requests.get(URL, headers=headers)
resp.raise_for_status()
data = resp.json()

# Adjust this path based on the JSON you see
rows = data["result"]["data"]["json"]

df = pd.json_normalize(rows)
df.to_csv("breakingpoint_stats_2026.csv", index=False)
print("Wrote breakingpoint_stats_2026.csv with", len(df), "rows")
