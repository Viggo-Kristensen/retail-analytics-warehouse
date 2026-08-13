import pandas as pd

def transform_date(fact_sales):
    dim_date = (
        pd.concat([
            fact_sales["purchase_date_id"], 
            fact_sales["delivery_date_id"], 
            fact_sales["estimated_delivery_date_id"]])
            .dropna()
            .drop_duplicates()
            .reset_index(drop=True)
            .to_frame("date_id")
    )  

    dim_date["date"] = pd.to_datetime(dim_date["date_id"])
    dim_date["year"] = dim_date["date"].dt.year
    dim_date["quarter"] = dim_date["date"].dt.quarter
    dim_date["month"] = dim_date["date"].dt.month
    dim_date["day"] = dim_date["date"].dt.day

    dim_date["week"] = dim_date["date"].dt.isocalendar().week
    dim_date["weekday"] = dim_date["date"].dt.dayofweek
    dim_date["is_weekend"] = dim_date["weekday"] > 4

    return dim_date[
        [
            "date_id",
            "date",
            "year",
            "quarter",
            "month",
            "day",
            "week",
            "weekday",
            "is_weekend"
        ]
    ]
    



    
