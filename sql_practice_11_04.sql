/*
PHARMACEUTICAL DATA AUDIT - SATURDAY REVISION
Focus: Aggregates, Grouping, and Conditional Filtering
*/

-- 1. SPECIFIC CATEGORY SUMMARY
-- Wisdom: Quick snapshot of the "API" category (Category 1).
SELECT 
    COUNT(ProductID) AS Total_APIs, 
    AVG(Price) AS Average_Price
FROM Products
WHERE CategoryID = 1;

-- 2. DIVERSE INVENTORY FILTERING
-- Wisdom: Finding categories with high product variety (more than 5 items).
SELECT CategoryID, COUNT(ProductID) AS Product_Count
FROM Products
GROUP BY CategoryID 
HAVING COUNT(ProductID) > 5;

-- 3. CUSTOMER LOYALTY RANKING
-- Wisdom: Identifying top-ordering customers for loyalty programs.
SELECT CustomerID, COUNT(OrderID) AS Total_Orders
FROM Orders
GROUP BY CustomerID
ORDER BY Total_Orders DESC;

-- 4. GEOGRAPHIC DISTRIBUTION
-- Wisdom: Mapping global presence by counting customers per country.
SELECT Country, COUNT(CustomerName) AS Total_Customers
FROM Customers
GROUP BY Country
ORDER BY Total_Customers DESC;

-- 5. HIGH-VALUE CATEGORY IDENTIFICATION
-- Wisdom: Isolating premium product categories (Average Price > 30).
SELECT CategoryID, AVG(Price) AS Mean_Price
FROM Products
GROUP BY CategoryID
HAVING AVG(Price) > 30;