/*
SQL ANALYTICAL SUBQUERIES - DAY 06
Focus: Nested Aggregations, Filtered Joins, and Correlated Logic
Project: Transactional Trends and Product Stratification
*/

-- ==========================================
-- SECTION 1: NESTED AGGREGATIONS (HAVING CLAUSE)
-- ==========================================

-- 1.1 High-Volume Customer Identification per Year
SELECT sub.total_orders, sub.customerid, sub.order_year
FROM (
    SELECT 
        customerid, 
        COUNT(orderid) AS total_orders,
        YEAR(orderdate) AS order_year
    FROM orders
    GROUP BY customerid, YEAR(orderdate)
) sub
GROUP BY sub.customerid
HAVING sub.total_orders > 3;

-- 1.2 Premium Category Analysis: Filtering by Mean Price
SELECT sub.all_products, sub.mean_price
FROM (
    SELECT 
        categoryid,
        COUNT(productid) AS all_products,
        AVG(price) AS mean_price
    FROM products
    GROUP BY categoryid
) sub
HAVING sub.mean_price > 40
ORDER BY sub.categoryid;

-- ==========================================
-- SECTION 2: SCALAR & POSITIONAL SUBQUERIES
-- ==========================================

-- 2.1 Customer Linkage: Filtering by specific OrderID reference
SELECT * FROM orders
WHERE customerid = (SELECT customerid FROM orders WHERE orderid = 10260);

-- 2.2 Correlated Price Benchmark: Above Category 2 Average
SELECT categoryid, price
FROM products
WHERE price > (SELECT AVG(price) FROM products WHERE categoryID = 2);

-- ==========================================
-- SECTION 3: NESTED FILTERING (FROM CLAUSE)
-- ==========================================

-- 3.1 Pre-Filtered Category Search: Premium items in Category 1
SELECT sub.*
FROM (
    SELECT * FROM products
    WHERE categoryid = 1
) sub
WHERE sub.price > 10;

-- 3.2 Regional Stratification: Targeted London Metadata
SELECT sub.*
FROM (
    SELECT * FROM customers
    WHERE country = 'UK'
) sub
WHERE sub.city = 'London';