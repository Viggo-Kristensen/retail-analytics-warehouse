# Run from project root:
# python -m analysis.sales_performance

import sqlite3
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

from database.repository import (
    get_daily_revenue,
    get_monthly_revenue,
    get_monthly_avg_order_value
)

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "warehouse.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

# initialise fig
fig, axes = plt.subplots(1, 3, figsize=(12, 4))
axes[0].set_title("Olist monthly revenue from 2016-2018")


# Plot 1
month_names = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

years = [2016, 2017, 2018]
x = np.arange(0, 12)
offset = 0.25
x = x - offset
for year in years:
    rows = get_monthly_revenue(cursor, year)
    revenue_per_month = [0] * 12
    for month, revenue in rows:
        revenue_per_month[month-1] = revenue
    axes[0].bar(x, revenue_per_month, width=0.25, label=str(year))
    axes[0].set_xlabel("month")
    axes[0].set_ylabel("revenue (R$)")
    x += offset

axes[0].set_xticks(np.arange(0, 12))
axes[0].set_xticklabels(month_names, rotation=45)
axes[0].legend()

# Plot 2
rows = get_daily_revenue(cursor)

date_ids = []
daily_revenue = []

for date_id, revenue in rows:
    date_ids.append(date_id)
    daily_revenue.append(revenue)

axes[1].plot(date_ids, daily_revenue)
axes[1].set_xlabel("Date")
axes[1].set_ylabel("Revenue (R$)")
axes[1].set_title("Daily Olist Revenue — 2018")
axes[1].set_xticks(date_ids[::30])
axes[1].tick_params(axis="x", rotation=45)

# Plot 3
monthly_aov = [None] * 12
rows = get_monthly_avg_order_value(cursor, 2018)

for idx, (month, aov) in enumerate(rows):
    monthly_aov[idx] = aov


axes[2].plot(month_names, monthly_aov)
axes[2].set_xlabel("Month")
axes[2].set_ylabel("avg order value")
axes[2].set_title("Olist avg order value per month 2018")
axes[2].tick_params(axis="x", rotation=45)

plt.tight_layout()
plt.savefig(BASE_DIR / "plots" / "sales_performance.png", dpi=300, bbox_inches="tight")
connection.close()
plt.show()






