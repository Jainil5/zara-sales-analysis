import pandas as pd

df = pd.read_csv("dataset/zara-sales-sample.csv")

# print(df.columns)

df.drop_duplicates()
df.rename(columns={"Sales Volume": "Sales", "Product ID":"ID","sub category":"Category","gender":"Gender","name":"Name"}, inplace=True)

df["Revenue (USD)"] = df["Sales"] * df["price"]

sales_by_gender = df.groupby("Gender")["Sales"].sum().sort_values(ascending=False)
# print("Gender items:",sales_by_gender)
# print("--------------------")    
product_categories = df["Category"].value_counts().sort_values(ascending=False)
# print("Product Categories",product_categories)
# print("--------------------")    

sales_by_category = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
# print("Sales by Category:",sales_by_category)
# print("--------------------")    

highest_income = df.groupby("Category")["Revenue (USD)"].sum().sort_values(ascending=False)
# print("Highest income:",highest_income)
# print("--------------------")    

top_sellers = df.groupby("Name")["Sales"].sum().sort_values(ascending=False).head(5)
# print("Top sellers:",top_sellers)
# print("--------------------")    

least_sellers = df.groupby("Name")["Sales"].sum().sort_values(ascending=True).head(5)
# print("Least sellers:",least_sellers)
# print("--------------------")

top_revenue = df.groupby("Name")["Revenue (USD)"].sum().sort_values(ascending=False).head(5)
# print("Top revenue:",top_revenue)
# print("--------------------")    

least_revenue = df.groupby("Name")["Revenue (USD)"].sum().sort_values(ascending=True).head(5)
# print("Least revenue:",least_revenue)
# print("--------------------")    

total_sales = df['Sales'].sum()
total_revenue = df['Revenue (USD)'].sum()
total_items = len(df)
highest_sold_item = sales_by_category.idxmax()
least_sold_item = sales_by_category.idxmin()
highest_income_item = highest_income.idxmax()
