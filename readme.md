# CFIB Small-Business Confidence Tracker

An end-to-end data pipeline and visualization toolkit for the CFIB Business Barometer, including:
- **Data ingestion & cleaning**: process CFIB’s Excel data into tidy CSV
- **Static charts**: generate polished visuals with matplotlib
- **Interactive dashboard**: explore metrics over time with Streamlit

---

## Features

- **Raw-to-Tidy Pipeline** (`scripts/load_barometer.py`)
  - Reads CFIB’s `CFIB_MBB-data-donnes-YYYY-MM.xlsx`, extracts dates & metrics from `Dtfile_new`, pivots into a long format `data/processed/national_index.csv`.
- **Static Visualization** (`scripts/plot_static.py`)
  - Uses matplotlib to create:
    - **Long-term & short-term outlook** over the last decade (`images/outlook_trends.png`)
    - **Sector breakdown** for the most recent month (`images/sector_snapshot.png`)
- **Interactive Dashboard** (`app.py`)
  - Streamlit app to filter and chart any metric interactively.
- **Infographic-ready Assets**
  - Static images saved to `images/` for use in reports and social media.

---

## Tech Stack

- **Python 3.10+**
- **Data**: pandas, openpyxl
- **Static Viz**: matplotlib
- **Interactive**: Streamlit

---

## Installation

```bash
git clone git@github.com:hunainsh-99/cfib-confidence-tracker.git
cd cfib-confidence-tracker

python3 -m venv .venv
source .venv/bin/activate

# install all dependencies
pip install -r requirements.txt
```

> **requirements.txt** should include:
> ```text
> pandas
> openpyxl
> matplotlib
> streamlit
> ```

---

## Usage

1. **Prepare Data**
   ```bash
   # place CFIB_MBB-data-donnes-2025-04.xlsx in data/raw/
   python scripts/load_barometer.py
   ```
   Produces `data/processed/national_index.csv`.

2. **Generate Static Charts**
   ```bash
   python scripts/plot_static.py
   ```
   Outputs:
   - `images/outlook_trends.png`
   - `images/sector_snapshot.png`

3. **Launch Dashboard**
   ```bash
   streamlit run app.py
   ```

---

## Project Structure

```
cfib-confidence-tracker/
│
├── data/
│   ├── raw/
│   │   └── CFIB_MBB-data-donnes-2025-04.xlsx
│   └── processed/
│       └── national_index.csv
│
├── images/                 # static chart outputs
│   ├── outlook_trends.png
│   └── sector_snapshot.png
│
├── scripts/
│   ├── load_barometer.py   # raw Excel → tidy CSV
│   └── plot_static.py      # CSV → matplotlib charts
│
├── app.py                  # Streamlit dashboard
├── requirements.txt        # pinned dependencies
└── README.md               # this file
```

---





