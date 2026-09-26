import pandas as pd

view_orders = pd.read_csv("session_01/orders.csv")
view_orders.head()
view_orders.shape #(rows, columns)
view_orders.columns
view_orders.dtypes

#Python filtering syntax family
high_value_orders = view_orders[view_orders["total_amount"] > 300]

order_1030 = view_orders[view_orders["order_id"] == "ORD1030"]

#syntax family: column calculation
view_orders["expected_total"] = view_orders["quantity"] * view_orders["unit_price"]

for order in view_orders:
    mismatched_orders = view_orders[view_orders["total_amount"] != view_orders["expected_total"]]


