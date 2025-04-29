import os
import pandas as pd
import matplotlib.pyplot as plt

# to ensure output folder exists
os.makedirs("images", exist_ok=True)

# to load tidy data
csv_path = "data/processed/national_index.csv"
df = pd.read_csv(csv_path, parse_dates=["date"])

# 1) Static Chart: Long-term & Short-term Outlook Trends
outlook_metrics = [
    "Canada - outlook on 12 months",
    "Canada - outlook on 3 months"
]
df_outlook = df[df["metric"].isin(outlook_metrics)]

pivot_outlook = df_outlook.pivot_table(
    index="date",
    columns="metric",
    values="value",
    aggfunc="mean"
)

plt.figure()
for metric in outlook_metrics:
    plt.plot(
        pivot_outlook.index,
        pivot_outlook[metric],
        label=metric
    )
plt.title("CFIB Business Barometer: Long-term & Short-term Outlook")
plt.xlabel("Date")
plt.ylabel("Confidence Index")
plt.legend()
plt.tight_layout()
plt.savefig("images/outlook_trends.png")
plt.close()

# 2) Static Chart: Sector Confidence Snapshot for Most Recent Month
sector_metrics = [
    "Agriculture",
    "Natural resources*",
    "Construction",
    "Manufacturing",
    "Wholesale",
    "Retail",
    "Transportation",
    "Info., arts, recreation",
    "Finance, insur. realty",
    "Prof., business services"
]
latest_date = df["date"].max()
df_latest = df[(df["date"] == latest_date) & (df["metric"].isin(sector_metrics))]

df_latest = df_latest.sort_values("value", ascending=False)

plt.figure()
plt.barh(
    df_latest["metric"],
    df_latest["value"]
)
plt.title(f"CFIB Sector Confidence Snapshot: {latest_date.strftime('%Y-%m')}")
plt.xlabel("Confidence Index")
plt.tight_layout()
plt.savefig("images/sector_snapshot.png")
plt.close()
