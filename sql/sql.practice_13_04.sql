/* BIOINFORMATICS DATA ANALYSIS SUITE - DAY 01
   Focus: Advanced Aggregations, Filtering (HAVING), and Joins
   Author: Anushka Bhagra
   Date: April 13, 2026
*/

-- SECTION 1: Product Analysis (Aggregates & Sorting)
-- Goal: Calculate average price and total product count per category, sorted by highest average.
SELECT 
    categoryid, 
    AVG(price) AS Average_Price, 
    COUNT(productid) AS Total_Products 
FROM products
GROUP BY categoryid
ORDER BY AVG(price) DESC;

-- SECTION 2: Customer Loyalty Analysis (Filtering Aggregates)
-- Goal: Identify power-users who have placed more than 2 orders.
SELECT 
    customerid, 
    COUNT(orderid) AS Order_Count 
FROM orders
GROUP BY customerid
HAVING COUNT(orderid) > 2
ORDER BY COUNT(orderid) DESC;

-- SECTION 3: Price Range Analysis
-- Goal: Identify the spread between most and least expensive items per category.
SELECT 
    categoryid, 
    MAX(price) AS Max_Price, 
    MIN(price) AS Min_Price 
FROM products
group by categoryid;

-- SECTION 4: Regional Market Distribution
-- Goal: Find countries with a significant customer base (>3).
SELECT 
    country, 
    COUNT(customername) AS Customer_Count 
FROM customers
GROUP BY country
HAVING COUNT(customername) > 3
ORDER BY COUNT(customername) DESC;

-- SECTION 5: Phytochemical Relationship Mapping (Advanced Join)
-- Goal: Connect plant common names to their chemical compounds while preserving the master plant list.
SELECT 
    plant_info.Common_Name, 
    phyto_library.Chemical_Compound 
FROM plant_info
LEFT JOIN phyto_library 
ON plant_info.plant_id = phyto_library.plant_id;