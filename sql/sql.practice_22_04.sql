/*
SQL ANALYTICAL JOINS & AGGREGATE LINKING - DAY 08
Focus: Grouped Subquery Joins (In-line Views), Scalar Filtering, and Result Stratification
Project: Categorical Benchmarking and Customer Order Density
*/

-- ==========================================
-- SECTION 1: CATEGORICAL BENCHMARKING (JOINS)
-- ==========================================

-- 1.1 Product Metadata linked with Category Inventory Totals
SELECT products.*, sub.total_products_in_category
FROM products
JOIN (
    SELECT categoryid, 
           COUNT(productid) AS total_products_in_category
    FROM products
    GROUP BY categoryid
) sub ON products.categoryid = sub.categoryid
ORDER BY sub.total_products_in_category DESC;

-- 1.2 Order Details linked with Customer Loyalty Density
SELECT orders.*, sub.total_orders_by_customer
FROM orders 
JOIN (
    SELECT customerid,
           COUNT(orderid) AS total_orders_by_customer
    FROM orders
    GROUP BY customerid
) sub ON orders.customerid = sub.customerid
ORDER BY sub.total_orders_by_customer DESC;

-- 1.3 Price Indexing: Comparing products against Category Average Prices
SELECT products.*, sub.category_avg_price 
FROM products
JOIN (
    SELECT categoryid,
           AVG(price) AS category_avg_price
    FROM products
    GROUP BY categoryid
) sub ON products.categoryid = sub.categoryid
ORDER BY sub.category_avg_price DESC;

-- ==========================================
-- SECTION 2: SCALAR SUBQUERIES & NESTED FILTERS
-- ==========================================

-- 2.1 Outlier Detection: Items priced below the Category 2 Floor
SELECT * FROM products
WHERE price < (SELECT MIN(price) FROM products WHERE categoryid = 2);

-- 2.2 Nested Time-Series Filter: Targeted 1997 Analysis
SELECT sub.*
FROM (
    SELECT * FROM orders
    WHERE YEAR(orderdate) = 1997
) sub
WHERE sub.customerid = 'QUICK';

-- 2.3 Aggregate Stratification: Premium Categories (> 30 Mean Price)
SELECT sub.categoryid, sub.mean_price
FROM (
    SELECT categoryid,
           AVG(price) AS mean_price,
           COUNT(productid) AS total_products
    FROM products
    GROUP BY categoryid
) sub
GROUP BY sub.categoryid
HAVING sub.mean_price > 30;

-- ==========================================
-- SECTION 3: TOP-TIER JOINS & LIMITING
-- ==========================================

-- 3.1 Metadata Recovery: Joining with the first 5 records
SELECT * FROM orders
JOIN (
    SELECT orderid FROM orders
    ORDER BY orderid 
    LIMIT 5
) sub ON orders.orderid = sub.orderid;

-- 3.2 Geographic Stratification: Top 5 Customer Distribution
SELECT * FROM customers
JOIN (
    SELECT country, customername FROM customers
    GROUP BY customername
    ORDER BY country DESC
    LIMIT 5
) sub ON customers.customername = sub.customername;