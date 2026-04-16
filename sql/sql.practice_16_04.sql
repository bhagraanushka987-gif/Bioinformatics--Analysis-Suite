/*
SQL ANALYTICAL AGGREGATIONS - DAY 04
Focus: Nested Aggregates, Time-Series Subqueries, and Having Clauses
Target: Statistical Dataset Stratification
*/

-- ==========================================
-- SECTION 1: SCALAR SUBQUERIES (BENCHMARKING)
-- ==========================================

-- 1.1 Products exceeding the global average price
SELECT ProductName, Price 
FROM Products
WHERE Price > (SELECT AVG(Price) FROM Products);

-- 1.2 Scalar Filter: Below Category 3 minimum price
SELECT ProductName, Price 
FROM Products
WHERE Price < (SELECT MIN(Price) FROM Products WHERE CategoryID = 3);

-- 1.3 Geography Match: Contextual filtering by Customer ID
SELECT CustomerName, Country 
FROM Customers
WHERE Country = (SELECT Country FROM Customers WHERE CustomerID = 20);

-- 1.4 Transactional Logic: Linking orders by specific ID reference
SELECT OrderID, CustomerID 
FROM Orders
WHERE CustomerID = (SELECT CustomerID FROM Orders WHERE OrderID = 10252);

-- ==========================================
-- SECTION 2: NESTED QUERIES (FROM CLAUSE)
-- ==========================================

-- 2.1 Nested Price Thresholding
SELECT sub.*
FROM (
     SELECT * FROM Products
     WHERE CategoryID = 2
) sub
WHERE sub.Price > 20;

-- 2.2 Double-Constraint Nesting: Price and Category identification
SELECT sub.* FROM (
     SELECT * FROM Products 
     WHERE Price > 30
) sub
WHERE sub.CategoryID = 1;

-- 2.3 Regional Stratification: USA City Search
SELECT sub.* FROM (
     SELECT * FROM Customers
     WHERE Country = 'USA'
) sub
WHERE sub.City = 'Portland';

-- ==========================================
-- SECTION 3: ANALYTICAL METRICS & TIME-SERIES
-- ==========================================

-- 3.1 Year-over-Year Average Order Analysis
SELECT AVG(sub.Total_Orders), sub.Order_Year
FROM (
    SELECT 
        CustomerID,
        COUNT(OrderID) AS Total_Orders,
        YEAR(OrderDate) AS Order_Year
    FROM Orders
    GROUP BY CustomerID, YEAR(OrderDate)
) sub
GROUP BY sub.Order_Year
ORDER BY sub.Order_Year;

-- 3.2 Monthly Peak Performance per Customer
SELECT MAX(sub.Total_Orders), sub.CustomerID
FROM (
    SELECT 
        CustomerID,
        COUNT(OrderID) AS Total_Orders,
        MONTH(OrderDate) AS Date_Of_Order
    FROM Orders
    GROUP BY CustomerID, MONTH(OrderDate)
) sub
GROUP BY sub.CustomerID
ORDER BY sub.CustomerID;

-- 3.3 Financial Aggregation with Group Filtering (HAVING)
SELECT sub.CategoryID, SUM(sub.Total_Price)
FROM (
    SELECT 
        CategoryID,
        SUM(Price) AS Total_Price,
        COUNT(ProductID) AS ProductCount
    FROM Products
    GROUP BY CategoryID 
) sub
GROUP BY sub.CategoryID
HAVING SUM(sub.Total_Price) > 100
ORDER BY sub.CategoryID;