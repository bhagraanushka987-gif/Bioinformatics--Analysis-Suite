/*
SQL RELATIONAL AUDITING & COMPARATIVE SEQUENCING - DAY 18
Focus: Subquery Benchmarking, Sequential Window Offsets (LAG), and Ranking Parity
Project: Global Supply Chain Logistics and Categorical Price Analysis
*/

-- ==========================================
-- SECTION 1: BENCHMARKING & REGIONAL FILTERS
-- ==========================================

-- 1.1 Category Floor Detection: Items below Category 3 mean price
select * from products
where price < (select avg(price) from products where categoryid = 3);

-- 1.2 Geographic Precision: Targeted German Customer Segment
select sub.*
from(
    select * from customers
    where country = 'Germany'
) sub
where city = 'Berlin';

-- 1.3 High-Value Segment Auditing: Categories exceeding 30 Average Price
select sub.categoryid, sub.average_price
from(
    select categoryid,
           avg(price) as average_price,
           count(price) as total_products
    from products
    group by categoryid
) sub
having sub.average_price > 30;

-- ==========================================
-- SECTION 2: RELATIONAL INTEGRATION & SETS
-- ==========================================

-- 2.1 Sequential Batch Processing: Joining with the first 5 orders
select sub.* from orders
join (
    select orderid from orders
    order by orderid
    limit 5
) sub on orders.orderid = sub.orderid;

-- 2.2 Customer Volume Mapping: Orders linked with Customer Total Counts
select orders.*, sub.total_orders from orders
join(
    select customerid,
           count(orderid) as total_orders
    from orders
    group by customerid
) sub on orders.customerid = sub.customerid;

-- 2.3 Unified Entity Mapping: Global Supplier and Customer Locations
select city, country from customers
union 
select city, country from suppliers
order by country;

-- ==========================================
-- SECTION 3: COMMON TABLE EXPRESSIONS (CTEs)
-- ==========================================

-- 3.1 Modular Price Filter: High-value Category 3 targets
with all_products as(
    select * from products
    where price > 30
)
select * from all_products
where categoryid = 3;

-- ==========================================
-- SECTION 4: ADVANCED RANKING & OFFSET WINDOWS
-- ==========================================

-- 4.1 Ranking Parity: Visualizing Row Number vs. Competitive Rank
-- Essential for identifying ties in biological docking scores
select categoryid, productname, price,
       row_number() over(partition by categoryid order by price desc),
       rank() over(partition by categoryid order by price desc)
from products;

-- 4.2 Sequential Difference Mapping: Comparative Lag Analysis
-- Captures the price of the previous item within the same category
select categoryid, productname, price,
       lag(price, 1) over(partition by categoryid order by price)
from products;