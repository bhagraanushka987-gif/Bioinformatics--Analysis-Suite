/*
SQL POSITIONAL EXCLUSION & WINDOW MATRICES - DAY 35
Focus: Left Join Exclusion Filters, Partitioned Positional Offsets, and Subquery Compressions
Project: High-Volume Operational Logistics, Inventory Tracking, and Multi-Entity Spatial Layouts
*/

-- ==========================================
-- SECTION 1: STATISTICAL BENCHMARKING & SCALS
-- ==========================================

-- 1.1 Inventory Depletion Audit: Isolating stock lines falling below global averages
-- Note: Adjusted subquery column name to match the master query key 'unitsinstock'
select * from products
where unitsinstock < (select avg(unitsinstock) from products);

-- 1.2 Logistics Stratification: Subquery separation for high-weight USA distributions
select sub.* from(
    select * from orders
    where freight > 50
)sub
where sub.shipcountry = 'USA';

-- 1.3 High-Throughput Spatial Slicing: Countries handling more than 20 distinct shipments
select sub.shipcountry, sub.total_orders 
from(
    select shipcountry, 
           max(freight) as max_freight,
           count(orderid) as total_orders
    from orders
    group by shipcountry
)sub
where sub.total_orders > 20;

-- ==========================================
-- SECTION 2: RELATIONAL INTEGRATION & EXCLUSION SETS
-- ==========================================

-- 2.1 Left Join Exclusion Filter: Identifying unpurchased inventory items
-- Note: Fixed aliases (p -> products) and corrected typos (prouctid -> productid) for schema alignment
select products.* from products
left join orderdetails od on products.productid = od.productid
where od.productid is null;

-- 2.2 Reagent Density Mapping: Products linked with cumulative quantitative sales
select p.productid, p.productname, p.unitprice, sub.total_quantity_sold
from products p
join(
    select productid,
           sum(quantity) as total_quantity_sold
    from orderdetails
    group by productid
)sub on p.productid = sub.productid
order by total_quantity_sold desc;

-- 2.3 Set Unification (Deduplicated): Comprehensive coordinates of core spatial hubs
select city, country from employees
union 
select city, country from customers
order by country, city;

-- ==========================================
-- SECTION 3: COMMON TABLE EXPRESSIONS (CTEs)
-- ==========================================

-- 3.1 Modular Sub-cohort Auditing: Modern sales divisions post-1993
with all_employees as(
    select * from employees
    where hiredate > '1993-01-01'
)
select * from all_employees
where title like '%Sales%';

-- ==========================================
-- SECTION 4: ADVANCED WINDOW METRICS & OFFSETS
-- ==========================================

-- 4.1 Hybrid Analytical Ranking: Tracking chronological sequence numbers vs. competitive financial weights
select customerid, orderid, orderdate, freight,
       row_number() over(partition by customerid order by orderdate) as row_num,
       rank() over(partition by customerid order by freight desc) as rank_desc
from orders;

-- 4.2 Neighboring Value Offsets: Partitioned forward and backward pricing variations
select categoryid, productname, unitprice,
       lag(unitprice, 1) over(partition by categoryid order by unitprice) as previous_unitprice,
       lead(unitprice, 1) over(partition by categoryid order by unitprice) as next_unitprice
from products
order by categoryid, unitprice;