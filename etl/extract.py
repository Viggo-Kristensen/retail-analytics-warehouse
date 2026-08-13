import pandas as pd
from pathlib import Path

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = BASE_DIR / "data" / "raw"
CUSTOMERS_DATASET_PATH = RAW_DATA_DIR / "olist_customers_dataset.csv"
ORDER_ITEMS_DATASET_PATH = RAW_DATA_DIR / "olist_order_items_dataset.csv"
ORDER_PAYMENTS_DATASET_PATH = RAW_DATA_DIR / "olist_order_payments_dataset.csv"
ORDER_DATASET_PATH = RAW_DATA_DIR / "olist_orders_dataset.csv"
PRODUCTS_DATASET_PATH = RAW_DATA_DIR / "olist_products_dataset.csv"
SELLERS_DATASET_PATH = RAW_DATA_DIR / "olist_sellers_dataset.csv"
PRODUCT_CATEGORY_NAME_TRANSLATION_PATH = RAW_DATA_DIR / "product_category_name_translation.csv"

def extract():
    """Read the raw csv files from the olist dataset"""
    return {
        "customers": pd.read_csv(CUSTOMERS_DATASET_PATH),
        "order_items": pd.read_csv(ORDER_ITEMS_DATASET_PATH),
        "order_payments": pd.read_csv(ORDER_PAYMENTS_DATASET_PATH),
        "orders": pd.read_csv(ORDER_DATASET_PATH),
        "products": pd.read_csv(PRODUCTS_DATASET_PATH),
        "sellers": pd.read_csv(SELLERS_DATASET_PATH),
        "product_translation": pd.read_csv(PRODUCT_CATEGORY_NAME_TRANSLATION_PATH)
    }
    