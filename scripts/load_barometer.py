import pandas as pd

# 1. Point to your raw Excel
file_path = "data/raw/CFIB_MBB-data-donnes-2025-04.xlsx"

# 2. Read the sheet with no header  
raw = pd.read_excel(file_path, sheet_name="Dtfile_new", header=None)

# 3. Extract the dates from row 2, columns 4 onward  
date_row = raw.iloc[2, 4:]
# keep only real dates  
dates = pd.to_datetime(date_row[date_row.notna()])

# 4. Extract the metric names from column 0, rows 5 onward  
metrics = raw.iloc[5:, 0]
metrics = metrics[metrics.notna()].tolist()

# 5. Pull the data block (rows 5 → 5+len(metrics), cols 4 → 4+len(dates))  
data_block = raw.iloc[5 : 5 + len(metrics), 4 : 4 + len(dates)].values

# 6. Build a tidy DataFrame  
pivot = pd.DataFrame(data_block, index=metrics, columns=dates)

tidy = (
    pivot
    .reset_index()                  # bring metric names into a column
    .melt(
        id_vars="index",
        var_name="date",
        value_name="value"
    )
    .rename(columns={"index": "metric"})
)

# 7. Clean types & drop missing  
tidy["date"] = pd.to_datetime(tidy["date"], errors="coerce")
tidy["value"] = pd.to_numeric(tidy["value"], errors="coerce")
tidy = tidy.dropna(subset=["value"])

# 8. Make sure your output folder exists  
import os
os.makedirs("data/processed", exist_ok=True)

# 9. Save  
tidy.to_csv("data/processed/national_index.csv", index=False)
print("✅ saved tidy data:", tidy.shape)
