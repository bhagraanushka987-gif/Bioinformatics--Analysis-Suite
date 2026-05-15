/*
SQL SEQUENTIAL AUDIT MAPPING & OFFSET ANALYSIS - DAY 31
Focus: Sequential Offsets (Lead/Lag), Competitive Rank Parity, and Windowed Running Totals
Project: Global Supply Chain Logistics and Categorical Price Analysis
*/

-- ==========================================
-- SECTION 1: BENCHMARKING & TEMPORAL FILTERS
-- ==========================================

-- 1.1 Price Ceiling Detection: Items exceeding Category 2 maximum price
select * from products
where price > (select max(price) from products where categoryid = 2);

-- 1.2 Subquery Stratification: Tracking 'TOMSP' activity in 1996
select sub.* from(
    select * from orders
    where year(orderdate) = 1996
) sub
where sub.customerid = 'TOMSP';

-- 1.3 High-Frequency Loyalty: Customers with > 2 total orders
select sub.customerid, sub.total_orders
from(
    select customerid,
           count(orderid) as total_orders
    from orders
    group by customerid
)sub
having sub.total_orders > 2;

-- ==========================================
-- SECTION 2: RELATIONAL INTEGRATION & SETS
-- ==========================================

-- 2.1 Regional Saturation: Joining with the Top 2 highest-volume countries
select sub.* from customers
join(
    select country from customers
    group by country
    order by count(customerid) desc
    limit 2
)sub on customers.country = sub.country;

-- 2.2 Inventory Density Mapping: Products linked with Category Volume Totals
select products.* , sub.total_in_category from products
join( 
    select categoryid,
           count(productid) as total_in_category
    from products
    group by categoryid
    order by count(productid) desc
) sub on products.categoryid = sub.categoryid;

-- 2.3 Unified Geographic Map: Global Supplier and Customer Entities
select customername, country from customers
union
select suppliername, country from suppliers
order by country;

-- ==========================================
-- SECTION 3: COMMON TABLE EXPRESSIONS (CTEs)
-- ==========================================

-- 3.1 Modular Geographic Filter: Targeted French Customer Segment
with all_customers as(
    select * from customers
    where country = 'France'
)
select * from all_customers
where city = 'Paris';

-- ==========================================
-- SECTION 4: ADVANCED WINDOWING & OFFSET FUNCTIONS
-- ==========================================

-- 4.1 Statistical Windowing: Partitioned Rank and Running Totals
-- Essential for identifying ties and cumulative value within categories
select categoryid, Productname, price, 
       rank() over(partition by categoryid order by price desc),
       sum(price) over(partition by categoryid order by price desc)
from products;

-- 4.2 Sequential Difference Mapping: Forward and Backward Price Offsets
-- Note: Fixed syntax to ensure both LEAD and LAG are comma-separated in the SELECT list
select productname, price,
       lead(price, 1) over(order by price desc) as next_price,
       lag(price, 1) over(order by price desc) as prev_price
from products;