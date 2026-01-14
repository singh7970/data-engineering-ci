SELECT
    order_id,
    order_date,
    amount,
    UPPER(city) AS city
FROM sales
WHERE amount IS NOT NULL;
SELECT
    order_id,
    order_date,
    amount,
    UPPER(city) AS city
FROM sales
WHERE amount IS NOT NULL;
