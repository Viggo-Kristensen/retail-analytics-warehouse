import pandas as pd

def transform_seller(seller_df):
    return seller_df[
        [
            "seller_id",
            "seller_zip_code_prefix",
            "seller_city",
            "seller_state"
        ]
    ]
