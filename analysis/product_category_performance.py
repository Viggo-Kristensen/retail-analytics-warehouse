import matplotlib.pyplot as plt
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "warehouse.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

def get_best_categories_year(cursor, year, limit):
    cursor.execute("""
    SELECT product_category_name, SUM(price)
    FROM fact_sales
    JOIN dim_product
    ON fact_sales.product_id = dim_product.product_id
    JOIN dim_date d
    ON fact_sales.purchase_date_id = d.date_id
    WHERE d.year = ?
    GROUP BY dim_product.product_category_name
    ORDER BY SUM(price) DESC
    LIMIT ?
    """, (year, limit))
    return cursor.fetchall()

def most_orders_product_category(cursor, year, limit):
    cursor.execute("""
    SELECT product_category_name, COUNT(order_id)
    FROM fact_sales
    JOIN dim_date d
    ON fact_sales.purchase_date_id = d.date_id
    JOIN dim_product
    ON fact_sales.product_id = dim_product.product_id
    where year = ?
    GROUP BY product_category_name
    ORDER BY COUNT(order_id) DESC
    LIMIT ?
    """, (year, limit))
    return cursor.fetchall()

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
