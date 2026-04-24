# 📊 Tech Company Salaries — Data Cleaning & Visualization

## Why did I make it?

I wanted to practice the full data science workflow on a realistic dataset : cleaning messy data with pandas, then exploring it visually with seaborn. I created a raw CSV with intentional errors and wrote two scripts — one to clean it, one to visualize it.

## What tech did I use?

- **Python**
- **pandas** — data manipulation and cleaning
- **seaborn** — data visualization
- **matplotlib** — chart rendering and export

## What did I learn?

- How to detect and handle missing values with `.isnull()` and `.fillna()`
- How to fix inconsistent text with `.str.title()`, `.str.upper()`, `.str.lower()`
- How to convert wrong data types with `pd.to_numeric(errors="coerce")`
- How to fill missing values smartly using `.groupby().transform()` instead of a global average
- How to map text values to booleans (`"yes"` → `True`)
- How to build bar plots, scatter plots, histograms and box plots with seaborn
- How to read a box plot : median, Q1/Q3, whiskers, and what they tell you about salary distribution

## What went well?

- The `groupby().transform()` trick for filling missing salaries worked really well — filling by job title is more accurate than filling with the global median
- The 4-chart layout gives a clear overview of the dataset in one image
- The box plot (remote vs on-site) was the most insightful chart — it shows not just the average but the full salary spread

## What went poorly?

- I initially tried `df["salary"].fillna()` directly without groupby — the result was less accurate
- I forgot that `"N/A"` strings in a CSV are not automatically treated as missing values by pandas — I had to use `pd.to_numeric(errors="coerce")` to convert them
- The remote column needed extra cleaning (`.str.lower().map()`) before the box plot would work correctly

## What I would add next

- A salary prediction model with scikit-learn
- An interactive dashboard with Streamlit

## How to run

```bash
pip install pandas seaborn matplotlib
python cleaning.py       # generates tech_salaries_clean.csv
python visualization.py  # generates salaries_visualization.png
```

## Project structure

```
tech-salaries/
├── tech_salaries_raw.csv        # original messy dataset
├── cleaning.py                  # cleaning script
├── visualization.py             # visualization script
├── tech_salaries_clean.csv      # output of cleaning.py
├── salaries_visualization.png   # output of visualization.py
└── README.md
```
