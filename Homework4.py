import pandas as pd

#q1

brooklyn_sales = pd.read_csv("rollingsales_brooklyn.csv",skiprows= 4)
print(brooklyn_sales)