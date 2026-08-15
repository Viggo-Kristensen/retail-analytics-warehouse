## Project description
This project contains a retail analytics warehouse build around the OLIST e-commerce dataset. 

### Dataset
The dataset used is `Brazilian E-Commerce Public Dataset` by Olist from 2018. The dataset contains information from over 100k orders that where made from 2016 to 2018 on Brazilian markedplaces. The data is structured like a normalized relational database that is optimized for operational use. Among other things tables included are orders, products, sellers and customers.

### Database
The project uses an SQLite3 database. That means that the database used is serverless and the tables are stored in the warehouse.db file. `schema.py` encompasses the code that is needed to initialise the tables in SQLite and `repositary.py` contains all the SQL queries used in the analysis.

### Star-schema
The analytical database is build around a star-schema structure where sales is the central business activity to be analyzed.
- fact_sales: The fact_sales table mainly stores the primary key `sales_id` aswell as the forreign keys referencing the dimension tables surrounding it.
- dim_customer: Primarily Stores geographical information about the customers.  
- dim_product: Stores descriptional informations about the products that Olist sell.
- dim_seller: Keeps information on all the independent sellers that use Olist markedplace to sell items.
- dim_date: The date dimensions just stores calendar attributes (year, month day) which is usefull for timebased analysis. It functions as a roleplaying dimension by being able to use it for multiple types of time data that the fact_sales keeps.

![star schema](star_schema/star_schema.png)

### ETL
To get the data from the csv file format into the analytical warehouse an ETL process was used. Firstly the csv data files was extracted and saved as dataframes. The tables needed for the warehouse were then constructed by transforming the data using pandas to upload and convert it to SQL.



### Analysis
business_analysis.md contains a business analysis i have made based on the plots i have created from the sales star-schema.

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



#__________
The original data files from the Olist dataset is structured in a normalized relational database which is optimized for operational usage. Through an ETL process i have transformed the data and inserted it into my sqlite datawarehouse. The analytical database is build around a star-schema structure where sales is the central business activity to be analyzed. The dimensions surrounding the `fact_sales` table are `dim_product`, `dim_seller`, `dim_customer` and `dim_date`. 

# will not use 
In the original dataset the sales are not stored explicitly in rows. Instead they have a orders dataset where the primary key is a combination of order_id and 
#____________________