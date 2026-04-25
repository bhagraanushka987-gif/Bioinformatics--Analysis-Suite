/*
SQL COMMON TABLE EXPRESSIONS (CTEs) & WINDOWING - DAY 11
Focus: WITH Clause (CTEs), Partitioned Windowing, and Set Integration
Project: Global Sales Benchmarking and Inventory Stratification
*/

-- ==========================================
-- SECTION 1: COMMON TABLE EXPRESSIONS (CTEs)
-- ==========================================

-- 1.1 High-Value Inventory Filter
WITH total_price AS (
    SELECT * FROM products
    WHERE price > 50
)
SELECT * FROM total_price;

-- 1.2 Regional Customer Segment: Germany
WITH all_customers AS (
    SELECT * FROM customers
    WHERE country = 'Germany'
)
SELECT * FROM all_customers;

-- 1.3 Annual Order Segment: 1997 Transactional Data
WITH all_orders AS (
    SELECT * FROM orders
    WHERE YEAR(orderdate) = 1997
)
SELECT * FROM all_orders;

-- 1.4 Refined Categorical Analysis: Category 1 Premium Items
WITH all_products AS (
    SELECT * FROM products
    WHERE categoryid = 1
)
SELECT * FROM all_products
WHERE price > 10;

-- ==========================================
-- SECTION 2: ANALYTICAL WINDOW FUNCTIONS
-- ==========================================

-- 2.1 Cumulative Pricing: Running Total by Price Point
SELECT productname,
       price,
       SUM(price) OVER(ORDER BY price) AS running_total_price
FROM products;

-- 2.2 Segmented Accumulation: Category-wise Running Totals
SELECT productname, 
       categoryid,
       SUM(price) OVER(PARTITION BY categoryid ORDER BY price) AS category_running_total
FROM products;

-- ==========================================
-- SECTION 3: SUBQUERIES & ANALYTICAL JOINS
-- ==========================================

-- 3.1 Scalar Benchmarking: Items exceeding Category 2 average
SELECT * FROM products
WHERE price > (SELECT AVG(price) FROM products WHERE categoryid = 2);

-- 3.2 Targeted Filter: Customer 'ERNSH' 1997 Activity
SELECT sub.* FROM (
    SELECT * FROM orders
    WHERE YEAR(orderdate) = 1997
) sub
WHERE sub.customerid = 'ERNSH';

-- 3.3 Inventory Stratification: Joining with Top 3 Average-Price Categories
SELECT sub.* FROM products
JOIN (
    SELECT categoryid,
           AVG(price) AS avg_p
    FROM products 
    GROUP BY categoryid
    ORDER BY AVG(price) DESC
    LIMIT 3
) sub ON products.categoryid = sub.categoryid;

-- 3.4 Loyalty Metrics: Order totals per customer
SELECT orders.*, sub.total_orders FROM orders
JOIN (
    SELECT customerid,
           COUNT(orderid) AS total_orders
    FROM orders
    GROUP BY customerid
) sub ON orders.customerid = sub.customerid
ORDER BY sub.total_orders DESC;

-- ==========================================
-- SECTION 4: AGGREGATES & SET OPERATIONS
-- ==========================================

-- 4.1 Categorical Inventory Check: High-Volume Categories (> 5 Items)
SELECT categoryid, COUNT(productid) AS item_count 
FROM products
GROUP BY categoryid
HAVING COUNT(productid) > 5;

-- 4.2 Cross-Entity Data Integration (Products & US Suppliers)
SELECT productname AS item_name, price AS metric FROM products
WHERE price > 50
UNION ALL
SELECT suppliername AS item_name, city AS metric FROM suppliers
WHERE country = 'USA';

-- 4.3 Standard Transactional Join
SELECT customername, orderid 
FROM customers
INNER JOIN orders ON customers.customerid = orders.customerid;