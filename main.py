from database.connection import get_connection
from database.schema import create_tables

from etl.extract import extract
from etl.transform.customer import transform_customer
from etl.transform.date import transform_date
from etl.transform.product import transform_product
from etl.transform.sales import transform_sales
from etl.transform.seller import transform_seller
from etl.load import load_tables

def main():
    # Get connection
    connection = get_connection()

    # Create tables
    create_tables(connection)

    # Extract
    datasets = extract()

    # Transform
    fact_sales = transform_sales(datasets["order_items"], datasets["orders"])
    dim_customer = transform_customer(datasets["customers"])
    dim_product = transform_product(datasets["products"], datasets["product_translation"])
    dim_seller = transform_seller(datasets["sellers"])
    dim_date = transform_date(fact_sales)

    tables = {
        "dim_customer": dim_customer,
        "dim_product": dim_product,
        "dim_seller": dim_seller,
        "dim_date": dim_date,
        "fact_sales": fact_sales
    }

    # Load
    load_tables(connection, tables)

    connection.close()


if __name__ == "__main__":
    main()
    