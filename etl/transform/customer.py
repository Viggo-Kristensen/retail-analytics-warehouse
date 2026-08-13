import pandas as pd

def transform_customer(customer_df):
    return customer_df[
        [
            "customer_id",
            "customer_unique_id",
            "customer_zip_code_prefix",
            "customer_city",
            "customer_state"
        ]
    ]