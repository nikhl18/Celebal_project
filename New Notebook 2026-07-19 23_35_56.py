# Databricks notebook source
display(
    spark.sql("""
    SELECT
    customer_state,
    COUNT(*) as Total_Orders
    FROM silver_customers
    GROUP BY customer_state
    ORDER BY Total_Orders DESC
    """)
)

# COMMAND ----------

display(
spark.sql("""
SELECT
order_status,
COUNT(*) AS Total_Orders
FROM silver_orders
GROUP BY order_status
ORDER BY Total_Orders DESC
""")
)

# COMMAND ----------

display(
spark.sql("""
SELECT
YEAR(order_purchase_timestamp) AS Year,
MONTH(order_purchase_timestamp) AS Month,
COUNT(*) AS Total_Orders
FROM silver_orders
GROUP BY YEAR(order_purchase_timestamp),
MONTH(order_purchase_timestamp)
ORDER BY Year, Month
""")
)

# COMMAND ----------

display(
spark.sql("""
SELECT
YEAR(order_purchase_timestamp) AS Year,
MONTH(order_purchase_timestamp) AS Month,
COUNT(*) AS Total_Orders
FROM silver_orders
GROUP BY YEAR(order_purchase_timestamp),
MONTH(order_purchase_timestamp)
ORDER BY Year, Month
""")
)