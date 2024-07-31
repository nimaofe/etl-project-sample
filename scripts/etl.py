import pandas as pd
import requests
from sqlalchemy import create_engine

def extract_orders():
    # Sample data
    data = {
        'order_id': [1, 2, 3],
        'customer_id': [101, 102, 103],
        'product_id': [1, 2, 3],
        'quantity': [1, 2, 3],
        'order_date': ['2023-07-01', '2023-07-02', '2023-07-03']
    }
    return pd.DataFrame(data)

def extract_products():
    return pd.read_csv('data/products.csv')

def extract_transactions():
    response = requests.get('https://api.mocki.io/v1/b043df5a')
    return pd.DataFrame(response.json())

def transform_data(orders_df, products_df, transactions_df):
    orders_df['order_date'] = pd.to_datetime(orders_df['order_date'])
    merged_df = orders_df.merge(products_df, on='product_id')
    merged_df = merged_df.merge(transactions_df, on='order_id')
    return merged_df

def load_data(df):
    engine = create_engine('sqlite:///data/sales_analysis.db')
    df.to_sql('sales_data', engine, if_exists='replace', index=False)

def etl():
    orders_df = extract_orders()
    products_df = extract_products()
    transactions_df = extract_transactions()
    transformed_df = transform_data(orders_df, products_df, transactions_df)
    load_data(transformed_df)

if __name__ == "__main__":
    etl()
