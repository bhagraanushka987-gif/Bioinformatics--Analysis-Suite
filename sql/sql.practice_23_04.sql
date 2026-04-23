/*
SQL SET OPERATIONS & DATA INTEGRATION - DAY 09
Focus: UNION/UNION ALL Operators, Nested Aggregates, and Global Benchmarking
Project: Cross-Entity Geography Mapping and Transactional Stratification
*/

-- ==========================================
-- SECTION 1: BENCHMARKING & NESTED FILTERS
-- ==========================================

-- 1.1 Global Price Outlier: Items exceeding Category 2's maximum price
SELECT * FROM products
WHERE price > (SELECT MAX(price) FROM products WHERE categoryid = 2);

-- 1.2 Targeted Time-Series: Customer 'HANAR' activity in 1996
SELECT sub.*
FROM (
    SELECT * FROM orders
    WHERE YEAR(orderdate) = 1996
) sub
WHERE sub.customerid = 'HANAR';

-- 1.3 High-Frequency Monthly Orders: Customers with > 2 orders per month
SELECT sub.customerid, sub.total_orders
FROM (
    SELECT 
        customerid,
        COUNT(orderid) AS total_orders,
        MONTH(orderdate) AS order_month
    FROM orders
    GROUP BY customerid, MONTH(orderdate)
) sub
GROUP BY sub.customerid
HAVING sub.total_orders > 2;

-- ==========================================
-- SECTION 2: ANALYTICAL JOINS (STRATIFICATION)
-- ==========================================

-- 2.1 Luxury Tier Mapping: Joining with Top 3 price outliers
SELECT products.* FROM products
JOIN (
    SELECT price FROM products
    ORDER BY price DESC
    LIMIT 3
) sub ON products.price = sub.price;

-- 2.2 Inventory Density: Products linked with Category Totals
SELECT products.*, sub.total_in_category 
FROM products
JOIN (
    SELECT 
        categoryid,
        COUNT(productid) AS total_in_category
    FROM products
    GROUP BY categoryid
) sub ON products.categoryid = sub.categoryid
ORDER BY sub.total_in_category DESC;

-- ==========================================
-- SECTION 3: SET OPERATIONS (UNION & UNION ALL)
-- ==========================================

-- 3.1 Distinct Global Entities (Customers and Suppliers)
SELECT customername AS entity_name, country FROM customers
UNION
SELECT suppliername AS entity_name, country FROM suppliers
ORDER BY country;

-- 3.2 Total Geographic Footprint (Includes duplicates)
SELECT country FROM customers
UNION ALL
SELECT country FROM suppliers
ORDER BY country;

-- 3.3 Urban Presence: Unique cities across both datasets
SELECT city FROM customers
UNION
SELECT city FROM suppliers;

-- 3.4 Full Urban Log: All city mentions across both datasets
SELECT city FROM customers
UNION ALL
SELECT city FROM suppliers;

-- 3.5 Categorical Unique Countries
SELECT country FROM customers
UNION 
SELECT country FROM suppliers
ORDER BY country;

-- 3.6 Cross-Entity City Audit (Cumulative)
SELECT customername, city FROM customers
UNION ALL 
SELECT suppliername, city FROM suppliers
ORDER BY city;

-- 3.7 Regional Deep-Dive: German Entities Only
SELECT country, customername AS name FROM customers
WHERE country = 'Germany'
UNION 
SELECT country, suppliername AS name FROM suppliers
WHERE country = 'Germany';