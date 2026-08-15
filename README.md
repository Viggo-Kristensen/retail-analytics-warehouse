## Project description
This project contains a retail analytics warehouse build around the OLIST e-commerce dataset.


**Raw CSV data → Pandas ETL → SQLite star schema → SQL analysis → Visualizations** 

### Dataset
The dataset used is `Brazilian E-Commerce Public Dataset` by Olist from 2018. The dataset contains information from over 100k orders made from 2016 to 2018 on Brazilian marketplaces. The data is structured like a normalized relational database that is optimized for operational use. Among other things tables included are orders, products, sellers and customers.

### Database
The project uses an SQLite3 database. That means that the database is serverless and the tables are stored in a warehouse.db file. `schema.py` encompasses the code that is needed to initialize the tables in SQLite3 and `repository.py` contains all the SQL queries used for the analysis. 

### Star-schema
The analytical database is built around a star-schema structure where sales is the central business activity to be analyzed.
- fact_sales: The central fact table storing the foreign keys for the surrounding dimensions and sales-related measures such as price and freight value.
- dim_customer: Primarily stores geographical information about the customers.  
- dim_product: Stores descriptive information about the products that Olist sells.
- dim_seller: Keeps information on all the independent sellers that use Olist marketplace to sell items.
- dim_date: Stores calendar attributes such as year, month and day which is useful for time-based analysis. It functions as a role-playing dimension allowing the same date dimension to be used for different date attributes in the fact_sales table.

![star schema](star_schema/star_schema.png)

### ETL
The CSV files are first extracted into pandas DataFrames. The tables are then constructed by transforming the raw data using pandas before being loaded into SQLite.

### How to run 
- To create the analytical database run `main.py` from the root of the project.
- To generate each of the plots for the analysis run: 
    - python -m analysis.delivery_performance 
    - python -m analysis.product_category_performance
    - python -m analysis.sales_performance

### Project structure
```
.
├── README.md
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
