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