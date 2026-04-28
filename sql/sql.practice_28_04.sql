/*
SQL STATISTICAL BENCHMARKING & WINDOW AGGREGATES - DAY 14
Focus: Simultaneous Multi-Metric Windowing, CTE Filter Pipelines, and Set Integration
Project: Global Market Demographics and Categorical Price Analysis
*/

-- ==========================================
-- SECTION 1: BENCHMARKING & CTE PIPELINES
-- ==========================================

-- 1.1 Price Floor Detection: Items below Category 1 average
SELECT * FROM products
WHERE price < (SELECT AVG(price) FROM products WHERE categoryid = 1);

-- 1.2 Regional Deep-Dive: Targeted London Customer Segment
SELECT sub.* FROM (
    SELECT * FROM customers
    WHERE country = 'UK'
) sub
WHERE sub.city = 'London';

-- 1.3 Modular Filter: Category 2 Premium Items (> 20)
-- Utilizing a CTE to isolate high-value products before category selection
WITH price_above AS (
    SELECT * FROM products
    WHERE price > 20
)
SELECT * FROM price_above
WHERE categoryid = 2;

-- 1.4 Aggregate Stratification: High-Value Categories (> 20 Mean Price)
SELECT sub.categoryid, sub.mean_price
FROM (
    SELECT categoryid,
           AVG(price) AS mean_price,
           COUNT(productid) AS total_products
    FROM products
    GROUP BY categoryid
) sub
WHERE sub.mean_price > 20;

-- ==========================================
-- SECTION 2: RELATIONAL JOINS & SET THEORY
-- ==========================================

-- 2.1 Chronological Analysis: Joining with the 3 most recent order dates
SELECT orders.* FROM orders
JOIN (
    SELECT orderdate FROM orders
    ORDER BY orderdate DESC
    LIMIT 3 
) sub ON orders.orderdate = sub.orderdate;

-- 2.2 Demographic Density: Customers linked with Country-wide Population Totals
SELECT customers.*, sub.total_in_country 
FROM customers
JOIN (
    SELECT country, 
           COUNT(customerid) AS total_in_country
    FROM customers
    GROUP BY country
) sub ON customers.country = sub.country
ORDER BY sub.total_in_country DESC;

-- 2.3 Global Geographic Footprint: Unique countries across Suppliers and Customers
SELECT country FROM customers
UNION
SELECT country FROM suppliers
ORDER BY country;

-- ==========================================
-- SECTION 3: ADVANCED ANALYTICAL WINDOWING
-- ==========================================

-- 3.1 Categorical Statistics: Comprehensive Partitioning (All Products)
-- Provides SUM, COUNT, and AVG for each category without row collapsing
SELECT categoryid, 
       productname, 
       price,
       SUM(price) OVER(PARTITION BY categoryid) AS category_total_price,
       COUNT(productid) OVER(PARTITION BY categoryid) AS category_product_count,
       AVG(price) OVER(PARTITION BY categoryid) AS category_average_price
FROM products;

-- 3.2 Filtered Partitioned Statistics: Premium Items (> 15)
-- Analyzes statistics only for products meeting a specific value threshold
SELECT categoryid, 
       productname, 
       price,
       SUM(price) OVER(PARTITION BY categoryid) AS filtered_total_price,
       COUNT(productid) OVER(PARTITION BY categoryid) AS filtered_product_count,
       AVG(price) OVER(PARTITION BY categoryid) AS filtered_average_price
FROM products
WHERE price > 15;

-- 3.3 Customer Loyalty Volume: Total orders per unique customer
SELECT customerid, 
       orderid, 
       COUNT(orderid) OVER(PARTITION BY customerid) AS customer_lifetime_orders
FROM orders;