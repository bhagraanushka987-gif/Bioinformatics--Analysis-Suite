/*
SQL RELATIONAL QUERIES - DAY 02
Focus: Joins (Inner/Left) and Set Operations (Union)
Target: Professional Database Management
*/

-- ==========================================
-- SECTION 1: JOIN OPERATIONS
-- ==========================================

-- 1.1 INNER JOIN: Fetching only matching records (Products with known Suppliers)
SELECT 
    p.ProductName, 
    s.SupplierName 
FROM Suppliers s
INNER JOIN Products p ON s.SupplierID = p.SupplierID;

-- 1.2 LEFT JOIN: Identifying all customers, including those who haven't ordered
SELECT 
    c.CustomerName, 
    COUNT(o.OrderID) AS TotalOrders
FROM Customers c
LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerName;

-- 1.3 INNER JOIN: Standard Order Retrieval
SELECT 
    c.CustomerName, 
    o.OrderID 
FROM Customers c
INNER JOIN Orders o ON c.CustomerID = o.CustomerID;

-- ==========================================
-- SECTION 2: SET OPERATIONS (UNION)
-- ==========================================

-- 2.1 UNION: Unique Countries across both Customers and Suppliers
-- (Note: UNION automatically removes duplicates)
SELECT Country FROM Customers
UNION 
SELECT Country FROM Suppliers;

-- 2.2 UNION: Distinct Cities for Logistics Mapping
SELECT City FROM Customers
UNION
SELECT City FROM Suppliers;