import pandas as pd

def transform_sales(order_items_df, orders_df):
    fact_sales = order_items_df.copy()
    fact_sales["sales_id"] = range(1, len(fact_sales) + 1)
    
    orders_df = orders_df[[
        "order_id", 
        "order_purchase_timestamp", 
        "order_delivered_customer_date",
        "order_estimated_delivery_date",
        "customer_id"
        ]]

    fact_sales = fact_sales.merge(
        orders_df,
        on="order_id",
        how="left"
    )

    fact_sales = fact_sales.rename(columns={
        "order_purchase_timestamp": "purchase_date_id",
        "order_delivered_customer_date": "delivery_date_id",
        "order_estimated_delivery_date": "estimated_delivery_date_id"
    })

    fact_sales["purchase_date_id"] = pd.to_datetime(
        fact_sales["purchase_date_id"]).dt.strftime("%Y%m%d")

    fact_sales["delivery_date_id"] = pd.to_datetime(
        fact_sales["delivery_date_id"]).dt.strftime("%Y%m%d")
    
    fact_sales["estimated_delivery_date_id"] = pd.to_datetime(
        fact_sales["estimated_delivery_date_id"]).dt.strftime("%Y%m%d")
    
    
    return fact_sales[
        [
            "sales_id",
            "order_id",
            "customer_id",
            "product_id",
            "seller_id",
            "purchase_date_id",
            "delivery_date_id",
            "estimated_delivery_date_id",
            "price",
            "freight_value"
        ]
    ]
        
 
    
    
