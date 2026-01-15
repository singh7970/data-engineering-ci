-- This SQL represents warehouse-style transformations.
-- Logic is kept in SQL to mirror real data platforms
-- like Snowflake, BigQuery, or Spark SQL.

SELECT
    order_id,
    order_date,
    amount,
    UPPER(city) AS city  -- Standardizing city names for consistent analytics
FROM sales
WHERE amount IS NOT NULL;  -- Prevents null values from breaking aggregations
