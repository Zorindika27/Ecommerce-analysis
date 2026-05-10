import pandas as pd
import matplotlib.pyplot as plt

# LOAD DATA

df = pd.read_csv("ecommerce_dataset_updated.csv")

# DATA CLEANING

# Rename columns
df.columns = [
    "user_id",
    "product_id",
    "category",
    "price",
    "discount",
    "final_price",
    "payment_method",
    "purchase_date"
]

# Calculate savings amount
df["savings"] = df["price"] - df["final_price"]

# Discount percentage
df["discount_percentage"] = (
    (df["discount"] / df["price"]) * 100
).round(2)

# Total revenue
total_revenue = df["final_price"].sum()

# Average order value
average_order_value = df["final_price"].mean()

# Total customers
total_customers = df["user_id"].nunique()


# Top revenue category
category_revenue = (
    df.groupby("category")["final_price"]
    .sum()
    .sort_values(ascending=False)
)

# Payment method distribution
payment_distribution = df["payment_method"].value_counts()

# Average discount by category
avg_discount = (
    df.groupby("category")["discount_percentage"]
    .mean()
    .sort_values(ascending=False)
)

# Top spending customers
top_customers = (
    df.groupby("user_id")["final_price"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

# BUSINESS INSIGHTS


print("\n===== BUSINESS INSIGHTS =====")

print(f"Total Revenue: ₹{total_revenue:,.2f}")

print(f"Average Order Value: ₹{average_order_value:,.2f}")

print(f"Total Unique Customers: {total_customers}")

print(
    f"Top Revenue Category: "
    f"{category_revenue.idxmax()} "
    f"(₹{category_revenue.max():,.2f})"
)

print(
    f"Most Popular Payment Method: "
    f"{payment_distribution.idxmax()}"
)

print(
    f"Highest Discount Category: "
    f"{avg_discount.idxmax()} "
    f"({avg_discount.max():.2f}%)"
)


# SAVE ANALYSIS TO EXCEL


with pd.ExcelWriter("ecommerce_analysis_report.xlsx") as writer:

    # Cleaned data
    df.to_excel(
        writer,
        sheet_name="Cleaned_Data",
        index=False
    )

    # Category revenue
    category_revenue.to_frame(
        name="Revenue"
    ).to_excel(
        writer,
        sheet_name="Category_Revenue"
    )

    # Payment methods
    payment_distribution.to_frame(
        name="Count"
    ).to_excel(
        writer,
        sheet_name="Payment_Distribution"
    )

    # Average discount
    avg_discount.to_frame(
        name="Average_Discount_%"
    ).to_excel(
        writer,
        sheet_name="Average_Discount"
    )

    # Top customers
    top_customers.to_frame(
        name="Customer_Spending"
    ).to_excel(
        writer,
        sheet_name="Top_Customers"
    )

print("\nExcel analysis report saved successfully!")