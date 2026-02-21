import pandas as pd
import matplotlib.pyplot as plt

# 1️ Load Dataset
df = pd.read_csv("data/retail_sales_dataset.csv")

print("Data Loaded Successfully \n")

# 2️ Convert Date Column
df['Date'] = pd.to_datetime(df['Date'])

# 3️ Basic Info
print("Dataset Shape:", df.shape)
print("\nColumns:\n", df.columns)
print("\nFirst 5 Rows:\n", df.head())

# -----------------------------------------
# 4️ Total Revenue
# ------------------------------------------
total_revenue = df['Revenue'].sum()
print("\nTotal Revenue:", total_revenue)

# ------------------------------------------
# 5️ Monthly Sales Analysis
# ------------------------------------------
df['Month'] = df['Date'].dt.to_period('M')

monthly_sales = df.groupby('Month')['Revenue'].sum()

print("\nMonthly Sales:\n", monthly_sales)

monthly_sales.plot(kind='bar')
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.show()

# ------------------------------------------
# 6️ Product Category Wise Sales
# ------------------------------------------
category_sales = df.groupby('Product Category')['Revenue'].sum().sort_values(ascending=False)

print("\nCategory Wise Sales:\n", category_sales)

category_sales.plot(kind='bar')
plt.title("Sales by Product Category")
plt.ylabel("Total Revenue")
plt.show()

# ------------------------------------------
# 7️ Gender Based Sales
# ------------------------------------------
gender_sales = df.groupby('Gender')['Revenue'].sum()

print("\nGender Wise Sales:\n", gender_sales)

gender_sales.plot(kind='bar')
plt.title("Sales by Gender")
plt.ylabel("Total Revenue")
plt.show()

# ------------------------------------------
# 8️ Top 5 Customers
# ------------------------------------------
top_customers = df.groupby('Customer ID')['Revenue'].sum().sort_values(ascending=False).head(5)

print("\nTop 5 Customers:\n", top_customers)

# ------------------------------------------
# 9️ Average Purchase Amount
# ------------------------------------------
average_purchase = df['Revenue'].mean()
print("\nAverage Purchase Value:", average_purchase)

print("\nAnalysis Completed Successfully ")
