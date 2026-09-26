import sqlite3
import pandas as pd

orders = pd.read_csv("session_01/orders.csv")

connection = sqlite3.connect(":memory:")

orders.to_sql(
    "orders",
    connection,
    index=False,
    if_exists="replace"
)

result = pd.read_sql_query(
    """
    SELECT COUNT(*) 
    FROM orders
    WHERE total_amount > 300
    ORDER BY total_amount DESC
    """,
    connection
)

cancelled_orders = pd.read_sql_query(
    """
    SELECT *
    FROM orders
    WHERE status = 'cancelled'
    """,
    connection
)

print(cancelled_orders)