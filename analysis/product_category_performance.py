# Run from project root:
# python -m analysis.delivery_analysis


import matplotlib.pyplot as plt
import sqlite3
from pathlib import Path

from database.repository import (
    get_best_categories_year,
    most_orders_product_category
)

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "warehouse.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

# Initialise plots
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Plot 1
rows = get_best_categories_year(cursor, 2018, 10)
product_category = []
revenue_category = []

for idx, row in enumerate(rows):
    product_category.append(row[0])
    revenue_category.append(row[1])

axes[1].barh(product_category, revenue_category, color="lightblue")
axes[1].invert_yaxis()
axes[1].set_xlabel("revenue (R$)")
axes[1].set_ylabel("product category")
axes[1].set_title("Highest revenue product categories 2018")
axes[1].tick_params(axis="x", labelrotation=90)


# Plot 2
rows = most_orders_product_category(cursor, 2018, 10)
orders_count = []
product_category = []

for row in rows:
    product_category.append(row[0])
    orders_count.append(row[1])

axes[0].barh(product_category, orders_count, color="lightgreen")
axes[0].invert_yaxis()
axes[0].set_xlabel("Orders")
axes[0].set_ylabel("product category")
axes[0].set_title("Most orders product categories 2018")
axes[0].tick_params(axis="x", labelrotation=90)


plt.tight_layout()
plt.savefig(BASE_DIR / "plots" / "product_category_performance.png", dpi=300, bbox_inches="tight")
plt.show()
connection.close()
