## Project description
This project contains a retail analytics warehouse I have build around the OLIST e-commerce dataset. 

The original data files from the Olist dataset is structured in a normalized relational database which is optimized for operational usage. Through an ETL process i have transformed the data and inserted it into my sqlite datawarehouse. The analytical database is build around a star-schema structure where sales is the central business activity to be analyzed. The dimensions surrounding the fact_sales table are `dim_product`, `dim_seller`, `dim_customer` and `dim_date`. In the original dataset the sales are not stored explicitly in rows. Instead 

### Star-schema
![star schema](star_schema/star_schema.png)

### How to run 
- To create the analytical database run `main.py` from the root of the project.
- To generate the plots for the analysis run python -m analysis.delivery_analysis in the terminal

### Project structure
```
.
├── analysis
│   ├── delivery_performance.py
│   ├── product_category_performance.py
│   └── sales_performance.py
├── data
│   └── raw
│       ├── olist_customers_dataset.csv
│       ├── olist_geolocation_dataset.csv
│       ├── olist_order_items_dataset.csv
│       ├── olist_order_payments_dataset.csv
│       ├── olist_order_reviews_dataset.csv
│       ├── olist_orders_dataset.csv
│       ├── olist_products_dataset.csv
│       ├── olist_sellers_dataset.csv
│       └── product_category_name_translation.csv
├── database
│   ├── connection.py
│   ├── repository.py
│   ├── schema.py
│   └── warehouse.db
├── etl
│   ├── extract.py
│   ├── load.py
│   └── transform
│       ├── customer.py
│       ├── date.py
│       ├── product.py
│       ├── sales.py
│       └── seller.py
├── main.py
├── plots
│   ├── delivery_performance.png
│   ├── product_category_performance.png
│   └── sales_performance.png
└── star_schema
    ├── notes.md
    └── star_schema.png
```