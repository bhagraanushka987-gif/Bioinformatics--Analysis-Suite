/*
SQL ADVANCED DATA FILTERING - DAY 03
Focus: Scalar Subqueries, Aggregate Comparisons, and From-Clause Nesting
Target: Bioinformatics Data Stratification
*/

-- ==========================================
-- SECTION 1: SCALAR SUBQUERIES (COMPARISONS)
-- ==========================================

-- 1.1 Finding products priced higher than all items in Category 1
SELECT ProductName, Price 
FROM Products
WHERE Price > (SELECT MAX(Price) FROM Products WHERE CategoryID = 1);

-- 1.2 Finding products priced lower than the cheapest item in Category 2
SELECT ProductName, Price 
FROM Products
WHERE Price < (SELECT MIN(Price) FROM Products WHERE CategoryID = 2);

-- 1.3 Geography Matching: Finding customers in the same country as a specific ID
SELECT CustomerName, Country 
FROM Customers
WHERE Country = (SELECT Country FROM Customers WHERE CustomerID = 5);

-- 1.4 Statistical Filtering: Identifying products priced above the global average
SELECT COUNT(ProductID) AS AboveAverageCount
FROM Products
WHERE Price > (SELECT AVG(Price) FROM Products);

-- 1.5 Order History: Counting total orders for a specific customer relative to an OrderID
SELECT COUNT(OrderID) AS CustomerOrderTotal
FROM Orders
WHERE CustomerID = (SELECT CustomerID FROM Orders WHERE OrderID = 10248);

-- ==========================================
-- SECTION 2: NESTED QUERIES (FROM CLAUSE)
-- ==========================================

-- 2.1 Nested Category Filter: Price thresholding on a pre-filtered Category 1 set
SELECT sub.*
FROM (
    SELECT * FROM Products 
    WHERE CategoryID = 1
) sub
WHERE sub.Price > 15;

-- 2.2 Regional Stratification: Narrowing down specific cities within Germany
SELECT sub.* FROM (
    SELECT * FROM Customers 
    WHERE Country = 'Germany'
) sub
WHERE sub.City = 'Berlin';

-- 2.3 Double-Constraint Logic: Category filtering on premium-priced items
SELECT sub.* FROM (
    SELECT * FROM Products 
    WHERE Price > 20
) sub
WHERE sub.CategoryID = 2;

-- 2.4 Time-Series Nesting: Identifying specific customer activity in 1996
-- Note: Replaced Year() with professional date filtering syntax
SELECT sub.* FROM (
    SELECT * FROM Orders 
    WHERE OrderDate BETWEEN '1996-01-01' AND '1996-12-31'
) sub
WHERE sub.CustomerID = 'VINET';