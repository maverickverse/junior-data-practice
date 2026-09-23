import pandas as pd

view_orders = pd.read_csv("session_01/orders.csv")

print(view_orders.head())
print(view_orders.shape) #(rows, columns)
print(view_orders.columns)
print(view_orders.dtypes)