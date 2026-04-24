/*
SQL ANALYTICAL WINDOWING & SET THEORY - DAY 10
Focus: Window Functions (OVER, PARTITION BY), Running Totals, and Multi-Entity Unions
Project: Bikeshare Metrics and Categorical Price Benchmarking
*/

-- ==========================================
-- SECTION 1: BENCHMARKING & NESTED FILTERS
-- ==========================================

-- 1.1 Price Floor Detection: Items below Category 1 average
SELECT * FROM products
WHERE price < (SELECT AVG(price) FROM products WHERE categoryid = 1);

-- 1.2 Regional Deep-Dive: Targeted Sao Paulo Metadata
SELECT sub.* FROM (
    SELECT * FROM customers
    WHERE country = 'Brazil'
) sub
WHERE sub.city = 'Sao Paulo';

-- 1.3 Aggregate Stratification: High-Value Categories (> 25 Mean Price)
SELECT sub.categoryid, sub.mean_price 
FROM (
    SELECT categoryid,
           AVG(price) AS mean_price 
    FROM products 
    GROUP BY categoryid 
) sub
GROUP BY sub.categoryid
HAVING sub.mean_price > 25;

-- ==========================================
-- SECTION 2: ANALYTICAL JOINS & UNIONS
-- ==========================================

-- 2.1 Market Penetration: Joining with Top 2 most populated countries
SELECT * FROM customers
JOIN (
    SELECT country FROM customers
    GROUP BY country
    ORDER BY COUNT(customerid) DESC
    LIMIT 2
) sub ON customers.country = sub.country;

-- 2.2 Loyalty Density: Linking orders with Customer Order Totals
SELECT orders.*, sub.total_orders FROM orders
JOIN (
    SELECT customerid,
           COUNT(orderid) AS total_orders
    FROM orders
    GROUP BY customerid
) sub ON orders.customerid = sub.customerid
ORDER BY sub.total_orders DESC;

-- 2.3 Cross-Entity Geography Mapping (Unique Suppliers and Customers)
SELECT suppliername AS entity_name, country FROM suppliers
UNION 
SELECT customername AS entity_name, country FROM customers
ORDER BY country;

-- ==========================================
-- SECTION 3: WINDOW FUNCTIONS (ANALYTICAL AGGREGATES)
-- ==========================================

-- 3.1 Cumulative Pricing: Running Total by Price Point
SELECT price,
       SUM(price) OVER(ORDER BY price) AS running_total_price
FROM products;

-- 3.2 Partitioned Metrics: Summation by Bike ID
SELECT duration_seconds,
       SUM(duration_seconds) OVER(PARTITION BY bike_number ORDER BY bike_number) AS bike_total
FROM tutorial.dc_bikeshare_q1_2012;

-- 3.3 Chronological Accumulation: Running total per Bike by Start Time
SELECT duration_seconds,
       SUM(duration_seconds) OVER(PARTITION BY bike_number ORDER BY start_time) AS chronological_total
FROM tutorial.dc_bikeshare_q1_2012;

-- 3.4 Filtered Running Total: Sequential Accumulation for Specific Station
SELECT duration_seconds, 
       SUM(duration_seconds) OVER(ORDER BY start_time) AS station_running_total
FROM tutorial.dc_bikeshare_q1_2012
WHERE start_station = 'Calvert St & Baltimore Ave';