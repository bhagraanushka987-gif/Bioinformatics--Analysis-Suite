/*
SQL ADVANCED JOINS & STRATIFICATION - DAY 07
Focus: Subquery Joins (In-line Views), Limit-Based Filtering, and Benchmarking
Project: Top-Tier Product and Customer Analytics
*/

-- ==========================================
-- SECTION 1: BENCHMARKING & SCALAR FILTERS
-- ==========================================

-- 1.1 Identifying products priced above Category 1 average
SELECT * FROM products
WHERE price > (SELECT AVG(price) FROM products WHERE categoryid = 1);

-- 1.2 Geography Matching: Customer location parity
SELECT * FROM customers
WHERE country = (SELECT country FROM customers WHERE customerid = 15);

-- ==========================================
-- SECTION 2: NESTED LOGIC (FROM CLAUSE)
-- ==========================================

-- 2.1 Premium Category 3 Stratification
SELECT sub.*
FROM (
    SELECT * FROM products
    WHERE price > 25
) sub
WHERE sub.categoryid = 3;

-- 2.2 Regional Focus: Paris Metadata
SELECT sub.*
FROM (
    SELECT * FROM customers
    WHERE country = 'France'
) sub
WHERE sub.city = 'Paris';

-- 2.3 Volume Analysis: High-Frequency Ordering
SELECT sub.customerid, sub.total_orders 
FROM (
    SELECT 
        customerid,
        COUNT(orderid) AS total_orders,
        YEAR(orderdate) AS date_ordered
    FROM orders
    GROUP BY customerid, YEAR(orderdate)
) sub
WHERE sub.total_orders > 2
ORDER BY sub.customerid;

-- ==========================================
-- SECTION 3: TOP-TIER ANALYSIS (SUBQUERY JOINS)
-- ==========================================

-- 3.1 Luxury Inventory: Joining with Top 5 highest-priced items
SELECT * FROM products
JOIN (
    SELECT price FROM products
    ORDER BY price DESC
    LIMIT 5
) sub ON products.price = sub.price;

-- 3.2 Time-Series: Fetching metadata for the 3 most recent orders
SELECT * FROM orders
JOIN (
    SELECT orderdate FROM orders
    ORDER BY orderdate DESC
    LIMIT 3
) sub ON orders.orderdate = sub.orderdate;

-- 3.3 Initial Records: Joining with the first 5 Order IDs
SELECT * FROM orders
JOIN (
    SELECT orderid FROM orders
    ORDER BY orderid
    LIMIT 5 
) sub ON orders.orderid = sub.orderid;

-- 3.4 Budget Categories: Joining with the 2 lowest average-price categories
SELECT * FROM products
JOIN (
    SELECT categoryid, AVG(price) AS avg_p
    FROM products
    GROUP BY categoryid
    ORDER BY AVG(price)
    LIMIT 2
) sub ON products.categoryid = sub.categoryid;

-- 3.5 Market Penetration: Joining with the Top 2 most populated countries
SELECT * FROM customers
JOIN (
    SELECT country, COUNT(customername) AS cust_count
    FROM customers
    GROUP BY country
    ORDER BY COUNT(customername) DESC
    LIMIT 2
) sub ON customers.country = sub.country;

-- 3.6 Premium Selection: Joining with the Top 3 highest prices
SELECT * FROM products
JOIN (
    SELECT price FROM products
    ORDER BY price DESC
    LIMIT 3 
) sub ON products.price = sub.price;