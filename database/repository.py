def get_average_delivery_delay(cursor, year):
    cursor.execute("""
    SELECT d1.month, AVG(julianday(d1.date) - julianday(d2.date))
    FROM fact_sales
    LEFT JOIN dim_date d1
    ON fact_sales.delivery_date_id = d1.date_id
    LEFT JOIN dim_date d2
    ON fact_sales.estimated_delivery_date_id = d2.date_id
    WHERE d1.year = ?
    GROUP BY d1.month
    """, (year,))
    return cursor.fetchall()

def get_average_delivery_time(cursor, year):
    cursor.execute("""
    SELECT d1.week, AVG(julianday(d2.date) - julianday(d1.date))
    FROM fact_sales
    JOIN dim_date d1
    ON fact_sales.purchase_date_id = d1.date_id
    JOIN dim_date d2
    ON fact_sales.delivery_date_id = d2.date_id
    WHERE d1.year = ?
    GROUP BY d1.week
    ORDER BY d1.week ASC
    """, (year,))
    return cursor.fetchall()

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

def get_monthly_revenue(cursor, year):
    cursor.execute("""
    SELECT month, COALESCE(SUM(price), 0)
    FROM dim_date
    LEFT JOIN fact_sales
    ON dim_date.date_id = fact_sales.purchase_date_id
    WHERE year = ?
    GROUP BY month
    ORDER BY month
    """, (year,))
    return cursor.fetchall()

def get_daily_revenue(cursor):
    cursor.execute("""
    SELECT date_id, SUM(price)
    FROM dim_date
    LEFT JOIN fact_sales
    ON dim_date.date_id = fact_sales.purchase_date_id
    WHERE year = 2018
    GROUP BY date_id
    ORDER BY date_id 
    """)
    return cursor.fetchall()

def get_monthly_avg_order_value(cursor, year):
    cursor.execute("""
    SELECT month, SUM(price) / COUNT(DISTINCT order_id) AS avg_order_value
    FROM fact_sales
    JOIN dim_date
    ON fact_sales.purchase_date_id = dim_date.date_id
    where year = ?
    GROUP BY month
    ORDER BY month
    """, (year,))
    return cursor.fetchall()