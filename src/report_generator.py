import pandas as pd
import matplotlib.pyplot as plt
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4

# 1️ Load Dataset
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
    else:
        print("Check column names for Quantity and Price per Unit")

# -----------------------------
# Basic Analysis
# -----------------------------
total_revenue = df['Revenue'].sum()
average_revenue = df['Revenue'].mean()
total_transactions = len(df)

# -----------------------------
# Monthly Sales Chart
# -----------------------------
if 'Date' in df.columns:
    df['Month'] = df['Date'].dt.to_period('M')
    monthly_sales = df.groupby('Month')['Revenue'].sum()

    plt.figure()
    monthly_sales.plot(kind='bar')
    plt.title("Monthly Revenue")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("monthly_revenue.png")
    plt.close()

# -----------------------------
# Category Wise Chart
# -----------------------------
if 'Product Category' in df.columns:
    category_sales = df.groupby('Product Category')['Revenue'].sum()

    plt.figure()
    category_sales.plot(kind='bar')
    plt.title("Category Wise Revenue")
    plt.tight_layout()
    plt.savefig("category_revenue.png")
    plt.close()

# -----------------------------
# Generate PDF Report
# -----------------------------
doc = SimpleDocTemplate("Retail_Sales_Report.pdf", pagesize=A4)
elements = []
styles = getSampleStyleSheet()

elements.append(Paragraph("<b>Retail Sales Revenue Report</b>", styles['Title']))
elements.append(Spacer(1, 0.5 * inch))

elements.append(Paragraph(f"Total Revenue: {total_revenue}", styles['Normal']))
elements.append(Paragraph(f"Average Revenue per Transaction: {average_revenue}", styles['Normal']))
elements.append(Paragraph(f"Total Transactions: {total_transactions}", styles['Normal']))
elements.append(Spacer(1, 0.5 * inch))

if 'Date' in df.columns:
    elements.append(Paragraph("<b>Monthly Revenue Chart</b>", styles['Heading2']))
    elements.append(Image("monthly_revenue.png", width=5*inch, height=3*inch))
    elements.append(Spacer(1, 0.5 * inch))

if 'Product Category' in df.columns:
    elements.append(Paragraph("<b>Category Wise Revenue Chart</b>", styles['Heading2']))
    elements.append(Image("category_revenue.png", width=5*inch, height=3*inch))

doc.build(elements)

print(" Report Generated Successfully: Retail_Sales_Report.pdf")
