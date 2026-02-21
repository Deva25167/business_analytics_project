import pandas as pd
import matplotlib.pyplot as plt

# 1️⃣ Load Dataset
df = pd.read_csv("data/retail_sales_dataset.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Convert Date
if 'Date' in df.columns:
    df['Date'] = pd.to_datetime(df['Date'])

# Create Revenue column if not present
if 'Revenue' not in df.columns:
    if 'Quantity' in df.columns and 'Price per Unit' in df.columns:
        df['Revenue'] = df['Quantity'] * df['Price per Unit']

# ----------------------------------
# 1️⃣ Monthly Revenue Trend
# ----------------------------------
if 'Date' in df.columns:
    df['Month'] = df['Date'].dt.to_period('M')
    monthly_revenue = df.groupby('Month')['Revenue'].sum()

    plt.figure()
    monthly_revenue.plot(kind='line', marker='o')
    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# ----------------------------------
# 2️⃣ Category Wise Revenue
# ----------------------------------
if 'Product Category' in df.columns:
    category_revenue = df.groupby('Product Category')['Revenue'].sum()

    plt.figure()
    category_revenue.plot(kind='bar')
    plt.title("Revenue by Product Category")
    plt.xlabel("Product Category")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.show()

# ----------------------------------
# 3️⃣ Gender Wise Revenue
# ----------------------------------
if 'Gender' in df.columns:
    gender_revenue = df.groupby('Gender')['Revenue'].sum()

    plt.figure()
    gender_revenue.plot(kind='bar')
    plt.title("Revenue by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.show()

# ----------------------------------
# 4️⃣ Age Distribution
# ----------------------------------
if 'Age' in df.columns:
    plt.figure()
    df['Age'].plot(kind='hist', bins=10)
    plt.title("Customer Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.show()

# ----------------------------------
# 5️⃣ Top 5 Customers by Revenue
# ----------------------------------
if 'Customer ID' in df.columns:
    top_customers = df.groupby('Customer ID')['Revenue'].sum().sort_values(ascending=False).head(5)

    plt.figure()
    top_customers.plot(kind='bar')
    plt.title("Top 5 Customers by Revenue")
    plt.xlabel("Customer ID")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.show()

print("✅ Visualization Completed Successfully")
