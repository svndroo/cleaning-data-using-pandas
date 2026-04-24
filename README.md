# 🧹 Tech Company Salaries — Data Cleaning

## Why did I make it?

I wanted to practice data cleaning with pandas on a realistic dataset.
Messy data is one of the most common problems in data science, so I created a raw CSV with intentional errors (missing values, inconsistent casing, wrong data types) and wrote a script to fix them.

## What tech did I use?

- **Python**
- **pandas** — data manipulation and cleaning

## What did I learn?

- How to detect and handle missing values with `.isnull()` and `.fillna()`
- How to fix inconsistent text with `.str.title()`, `.str.upper()`, `.str.lower()`
- How to convert wrong data types with `pd.to_numeric(errors="coerce")`
- How to fill missing values smartly using `.groupby().transform()` instead of a global average
- How to map text values to booleans (`"yes"` → `True`)

## What went well?

- The `groupby().transform()` trick for filling missing salaries worked really well — filling by job title is more accurate than filling with the global median
- The script is clean, readable and well commented

## What went poorly?

- I initially tried `df["salary"].fillna()` directly without groupby — the result was less accurate
- I forgot that `"N/A"` strings in a CSV are not automatically treated as missing values by pandas — I had to use `pd.to_numeric(errors="coerce")` to convert them

## What I would add next

- Visualizations with seaborn (salary by company, by job title...)
- A salary prediction model with scikit-learn

## How to run

```bash
pip install pandas
python cleaning.py
```

## Project structure

```
tech-salaries/
├── tech_salaries_raw.csv    # original messy dataset
├── cleaning.py              # cleaning script
├── tech_salaries_clean.csv  # output (generated after running the script)
└── README.md
```
