/*
SQL ANALYTICAL PIPELINES & SEQUENTIAL TRACKING - DAY 13
Focus: Multi-Level Window Partitions, Common Table Expressions (CTEs), and Set Operations
Project: Order Frequency Analysis and Categorical Price Distribution
*/

-- ==========================================
-- SECTION 1: BENCHMARKING & CTE LOGIC
-- ==========================================

-- 1.1 Category Outlier Detection: Items exceeding Category 3 maximum price
SELECT * FROM products
WHERE price > (SELECT MAX(price) FROM products WHERE categoryid = 3);

-- 1.2 Modular Temporal Analysis: Tracking 'VINET' activity in 1996
-- Utilizing a CTE for improved readability over nested subqueries
WITH all_orders AS (
    SELECT * FROM orders
    WHERE YEAR(orderdate) = 1996
)
SELECT * FROM all_orders
WHERE customerid = 'VINET';

-- 1.3 High-Frequency Annual Orders: Customers with > 2 orders per year
SELECT sub.customerid, sub.total_orders
FROM (
    SELECT customerid, 
           COUNT(orderid) AS total_orders,
           YEAR(orderdate) AS order_year
    FROM orders
    GROUP BY customerid, YEAR(orderdate)
) sub
WHERE sub.total_orders > 2;

-- ==========================================
-- SECTION 2: RELATIONAL JOINS & SET THEORY
-- ==========================================

-- 2.1 Value Tier Mapping: Joining with the 5 lowest-priced products
SELECT products.* FROM products
JOIN (
    SELECT price FROM products
    ORDER BY price
    LIMIT 5
) sub ON products.price = sub.price;

-- 2.2 Inventory Density: Products linked with Category Population Totals
SELECT products.*, sub.total_in_category 
FROM products
JOIN (
    SELECT categoryid,
           COUNT(productid) AS total_in_category
    FROM products
    GROUP BY categoryid
) sub ON products.categoryid = sub.categoryid;

-- 2.3 Global Geographic Presence: Unified City Registry (Unique)
SELECT customername AS entity_name, city FROM customers
UNION
SELECT suppliername AS entity_name, city FROM suppliers
ORDER BY city;

-- ==========================================
-- SECTION 3: ADVANCED WINDOW FUNCTIONS
-- ==========================================

-- 3.1 Cumulative Price Mapping: Categories 1, 2, and 3
SELECT categoryid, 
       price,
       SUM(price) OVER(PARTITION BY categoryid ORDER BY price) AS category_running_total
FROM products
WHERE categoryid IN (1, 2, 3);

-- 3.2 Feature Filtering with Windowing: Premium Running Totals (> 10)
SELECT categoryid,
       productname,
       price,
       SUM(price) OVER(PARTITION BY categoryid ORDER BY price) AS premium_running_total
FROM products
WHERE price > 10;

-- 3.3 Chronological Order Tracking: Cumulative count per customer
SELECT customerid, 
       orderid, 
       orderdate,
       COUNT(orderid) OVER(PARTITION BY customerid ORDER BY orderdate) AS cumulative_order_count
FROM orders;

-- 3.4 Target Segment Analysis: Running totals for Core Categories
SELECT categoryid, 
       productname, 
       price,
       SUM(price) OVER(PARTITION BY categoryid ORDER BY price) AS core_running_total
FROM products
WHERE categoryid IN (1, 2);