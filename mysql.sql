-- CREATE DATABASE ecom;
USE ecom;
SELECT SUM(final_Price) AS total_revenue
FROM ecom_data;
SELECT Category,
       COUNT(*) AS total_orders
FROM ecom_data
GROUP BY Category
ORDER BY total_orders DESC;
SELECT Category,
       SUM(final_Price) AS revenue
FROM ecom_data
GROUP BY Category
ORDER BY revenue DESC;
SELECT AVG(discount_pct) AS avg_discount
FROM ecom_data;
SELECT Payment_Method,
       COUNT(*) AS usage_count
FROM ecom_data
GROUP BY Payment_Method
ORDER BY usage_count DESC;
SELECT AVG(user_total)
FROM (
    SELECT User_ID,
           SUM(final_Price) AS user_total
    FROM ecom_data
    GROUP BY User_ID
) AS t;
SELECT *,
       Price - final_price AS discount_amount
FROM ecom_data;
SELECT User_ID,
       SUM(final_price) AS spending,
       CASE
           WHEN SUM(final_price) > 1000 THEN 'High Value'
           WHEN SUM(final_price) > 500 THEN 'Medium Value'
           ELSE 'Low Value'
       END AS customer_type
FROM ecom_data
GROUP BY User_ID;

