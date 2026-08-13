import pandas as pd

def transform_product(product_df, translation_df):
    dim_product = product_df.merge(
        translation_df,
        on="product_category_name",
        how="left"
    )

    dim_product["product_category_name"] = dim_product["product_category_name_english"]

    return dim_product[
        [
            "product_id",
            "product_category_name",
            "product_weight_g",
            "product_length_cm",
            "product_height_cm",
            "product_width_cm"
        ]
    ]
