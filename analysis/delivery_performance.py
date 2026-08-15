# Run from project root:
# python -m analysis.delivery_performance

import sqlite3
import matplotlib.pyplot as plt
from pathlib import Path

from database.repository import (
    get_average_delivery_delay,
    get_average_delivery_time
)

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "warehouse.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

month_names = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

# Initialising plots
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# Plot 1 
rows = get_average_delivery_delay(cursor, 2018)
delivery_delay_list = [None] * 12

for idx, delivery_delay in enumerate(rows):
    delivery_delay_list[idx] = delivery_delay[1]

axes[0].plot(month_names, delivery_delay_list, color="green", linewidth=3)
axes[0].set_xlabel("months")
axes[0].set_ylabel("delivery delay")
axes[0].set_title("Average delivery delay each month")

# Plot 2
weeks = [None] * 52
delivery_time = [None] * 52

rows = get_average_delivery_time(cursor, 2018)
for idx, row in enumerate(rows):
    weeks[idx] = row[0]
    delivery_time[idx] = row[1]


axes[1].plot(weeks, delivery_time, linewidth=2, color="green")
axes[1].set_xlabel("week")
axes[1].set_ylabel("average delivery time")
axes[1].set_title("Olist average delivery time 2018")

plt.tight_layout()
plt.savefig(BASE_DIR / "plots" / "delivery_performance.png", dpi=300, bbox_inches="tight")
plt.show()
connection.close()

