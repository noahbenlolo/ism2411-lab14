# -- Exercise #1--
import pandas as pd 
df = pd.read_csv("data/messy_sales.csv")
df.info()
print(df.isnull().sum())

# 3 Data Quality Issues:
#1. There are missing values , in the customer ID, 
# the customer ID has 4,438 non-null so there are 362 
# are missing.
#2. The unit price is a string but it should be a float.
#3. The order date is a string but it should be a datetime object.
 
