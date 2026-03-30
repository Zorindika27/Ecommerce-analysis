import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------
# Load Data
# ----------------------------
df = pd.read_csv("ecommerce_dataset_updated.csv")

# ----------------------------
# Clean Data
# ----------------------------
df.columns = [
    "user_id", "product_id", "category",
    "price", "discount", "final_price",
    "payment_method", "purchase_date"
]

df["purchase_date"] = pd.to_datetime(df["purchase_date"], dayfirst=True)

# Extract month
df["month"] = df["purchase_date"].dt.month_name()

# Order months properly
df["month"] = pd.Categorical(
    df["month"],
    categories=[
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ],
    ordered=True
)

# ----------------------------
# Analysis
# ----------------------------
category_revenue = df.groupby("category")["final_price"].sum()
monthly_revenue = df.groupby("month")["final_price"].sum()
payment_counts = df["payment_method"].value_counts()

# ----------------------------
# Visualization
# ----------------------------

# Category Revenue
category_revenue.plot(kind="bar", title="Revenue by Category")
plt.xlabel("Category")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.savefig("charts/category_revenue.png")
plt.clf()

# Monthly Revenue
monthly_revenue.plot(kind="bar", title="Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("charts/monthly_revenue.png")
plt.clf()

# Payment Method
payment_counts.plot(kind="bar", title="Payment Method Distribution")
plt.xlabel("Payment Method")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("charts/payment_methods.png")
plt.clf()




