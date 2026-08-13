def create_tables(connection):
    cursor = connection.cursor()

    connection.execute("PRAGMA foreign_keys = ON")

    # Create fact sales
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS fact_sales (
        sales_id INTEGER PRIMARY KEY,
        order_id TEXT,
        customer_id TEXT,
        product_id TEXT,
        seller_id TEXT,
        purchase_date_id TEXT,
        delivery_date_id TEXT,
        estimated_delivery_date_id TEXT,
        price REAL,
        freight_value REAL,
        FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id),
        FOREIGN KEY (product_id) REFERENCES dim_product(product_id),
        FOREIGN KEY (seller_id) REFERENCES dim_seller(seller_id),
        FOREIGN KEY (purchase_date_id) REFERENCES dim_date(date_id),
        FOREIGN KEY (delivery_date_id) REFERENCES dim_date(date_id)
    )
    """)

    # Create dim_customer
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dim_customer (
        customer_id TEXT primary key,
        customer_unique_id TEXT,
        customer_zip_code_prefix TEXT,
        customer_city TEXT,
        customer_state TEXT
    )
    """)

    # Create dim_product
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dim_product(
        product_id TEXT PRIMARY KEY,
        product_category_name TEXT,
        product_weight_g INTEGER,
        product_length_cm INTEGER,
        product_height_cm INTEGER,
        product_width_cm INTEGER
    )
    """)

    # Create dim_seller
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dim_seller(
        seller_id TEXT PRIMARY KEY,
        seller_zip_code_prefix TEXT,
        seller_city TEXT,
        seller_state TEXT
    )
    """)

    # Create dim_date
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS dim_date(
        date_id TEXT PRIMARY KEY,
        date DATETIME,
        year INTEGER,
        month INTEGER,
        day INTEGER,
        quarter INTEGER,
        week INTEGER,
        weekday INTEGER,
        is_weekend BOOLEAN
    )
    """)

    connection.commit()