"""
visualization.py
================
Visualizations of clean tech salaries data using seaborn.

Run :
    python visualization.py
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# ─── Load clean data ──────────────────────────────────────────────────────────

chemin = os.path.join(os.path.dirname(__file__), "tech_salaries_clean.csv")

try:
    df = pd.read_csv(chemin)
    print("✅ File loaded")
except FileNotFoundError:
    print("❌ File not found — run cleaning.py first")
    exit()

# Style
sns.set_theme(style="whitegrid", palette="muted")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("Tech Company Salaries — Analysis", fontsize=15, fontweight="bold")

# ─── Chart 1 : Average salary by company ─────────────────────────────────────

avg_company = df.groupby("company")["salary"].mean().sort_values(ascending=False).reset_index()

sns.barplot(data=avg_company, x="salary", y="company", ax=axes[0, 0])
axes[0, 0].set_title("Average Salary by Company")
axes[0, 0].set_xlabel("Salary (USD)")
axes[0, 0].set_ylabel("")

# ─── Chart 2 : Average salary by job title ───────────────────────────────────

avg_job = df.groupby("job_title")["salary"].mean().sort_values(ascending=False).reset_index()

sns.barplot(data=avg_job, x="salary", y="job_title", ax=axes[0, 1], palette="Blues_d")
axes[0, 1].set_title("Average Salary by Job Title")
axes[0, 1].set_xlabel("Salary (USD)")
axes[0, 1].set_ylabel("")

# ─── Chart 3 : Salary vs Experience ──────────────────────────────────────────

sns.scatterplot(
    data=df,
    x="experience_years",
    y="salary",
    hue="job_title",   # color by job title
    ax=axes[1, 0],
    s=80               # dot size
)
axes[1, 0].set_title("Salary vs Years of Experience")
axes[1, 0].set_xlabel("Experience (years)")
axes[1, 0].set_ylabel("Salary (USD)")
axes[1, 0].legend(fontsize=7)

# ─── Chart 4 : Remote vs On-site salary ──────────────────────────────────────

sns.boxplot(
    data=df,
    x="remote",
    y="salary",
    ax=axes[1, 1],
    palette={"True": "#2563EB", "False": "#DC2626"}
)
axes[1, 1].set_title("Salary : Remote vs On-site")
axes[1, 1].set_xlabel("Remote")
axes[1, 1].set_ylabel("Salary (USD)")
axes[1, 1].set_xticklabels(["On-site", "Remote"])

plt.tight_layout()
plt.savefig("salaries_visualization.png", dpi=150, bbox_inches="tight")
plt.show()
print("✅ Chart saved : salaries_visualization.png")
