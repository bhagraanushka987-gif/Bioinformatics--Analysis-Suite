/*
SQL DATA AUDIT DRILLS
Date: April 10, 2026
Objective: Targeted Inventory and Demographic Filtering

-- ==========================================
-- SECTION 1: SUPPLIER-SPECIFIC PRICE AUDIT
-- Wisdom: Filtering products by a specific manufacturer to monitor 
-- cost-effective inventory (Supplier 2, Price < 25).
-- ==========================================

SELECT ProductName, SupplierID, Price 
FROM Products
WHERE SupplierID = 2 
  AND Price < 25;


-- ==========================================
-- SECTION 2: REGIONAL DEMOGRAPHIC FILTERING
-- Wisdom: Precisely identifying localized customer groups for 
-- targeted pharmaceutical distribution or market research.
-- ==========================================

SELECT CustomerName, City, Country 
FROM Customers
WHERE Country = 'Germany'
  AND City = 'Berlin';