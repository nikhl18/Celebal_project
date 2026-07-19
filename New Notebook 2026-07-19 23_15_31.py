# Databricks notebook source
# DBTITLE 1,Daily Revenue Trends
revenue_df = spark.sql("""
SELECT 
    DATE(order_purchase_timestamp) as order_date,
    ROUND(SUM(price), 2) as revenue
FROM gold_sales
GROUP BY DATE(order_purchase_timestamp)
ORDER BY order_date
""")

display(revenue_df)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT
# MAGIC ROUND(SUM(price),2) AS Total_Revenue
# MAGIC FROM gold_sales;

# COMMAND ----------

spark.sql("""
SELECT
product_id,
COUNT(*) AS Total_Sales
FROM gold_sales
GROUP BY product_id
ORDER BY Total_Sales DESC
LIMIT 10
""").show()

# COMMAND ----------

spark.sql("""
SELECT
c.customer_state,
COUNT(o.order_id) AS Total_Orders
FROM silver_customers c
JOIN silver_orders o
ON c.customer_id=o.customer_id
GROUP BY c.customer_state
ORDER BY Total_Orders DESC
""").show()