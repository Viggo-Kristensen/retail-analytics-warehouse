def load_tables(connection, tables):
    for table_name, df in tables.items():
        df.to_sql(
            table_name,
            connection,
            if_exists="append",
            index=False
        )
