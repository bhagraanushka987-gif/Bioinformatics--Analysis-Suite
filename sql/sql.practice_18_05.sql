/*
SQL TEMPORAL KINETICS & ADVANCED WINDOW AUDITS - DAY 33
Focus: Partitioned Lead-Lag Chronology, Subquery Mass Aggregations, and Rank Boundaries
Project: Supply Chain Freight Optimization and Global Distribution Networks
*/

-- ==========================================
-- SECTION 1: STATISTICAL BENCHMARKING & FILTERS
-- ==========================================

-- 1.1 Outlier Isolation: Orders exceeding the global average operational cost
select * from orders
where cost > (select avg(cost) from orders);

-- 1.2 Temporal Stratification: Subquery separation for 1997 German logistics
select sub.* from( 
    select * from orders
    where year(orderdate) = 1997
)sub
where sub.ship_country = 'Germany';

-- 1.3 High-Value Logistics Segment: Customers exceeding 500 cumulative freight cost
select sub.customerid, sub.total_freight
from(
    select customerid,
           count(orderid) as total_orders,
           sum(freight_cost) as total_freight 
    from orders
    group by customerid
)sub
where sub.total_freight > 500;

-- ==========================================
-- SECTION 2: RELATIONAL INTEGRATION & SET COMPOSITIONS
-- ==========================================

-- 2.1 Dynamic Time Slicing: Inner matching with the 5 most recent shipments
select orders.* from orders
join(
    select orderid from orders
    order by orderdate desc
    limit 5
)sub on orders.orderid = sub.orderid;

-- 2.2 Supplier Inventory Density: Linking company profiles with category volume caps
select suppliers.supplierid , suppliers.companyname, sub.total_products from suppliers
join(
    select supplierid,
           count(productid) as total_products
    from products
    group by supplierid
)sub on suppliers.supplierid = sub.supplierid
order by sub.total_products desc;

-- 2.3 Unified Geographic Mapping: Comprehensive footprint of all customer and vendor centers
select country from customers
union all
select country from suppliers
order by country;

-- ==========================================
-- SECTION 3: COMMON TABLE EXPRESSIONS (CTEs)
-- ==========================================

-- 3.1 Isolated Sub-cohort Auditing: High-weight USA distribution lanes
with all_orders as(
    select * from orders
    where freight > 100
)
select * from all_orders
where shipcountry = 'USA';

-- ==========================================
-- SECTION 4: PARTITIONED WINDOW METRICS & OFFSETS
-- ==========================================

-- 4.1 Divergent Scale Ranking: Asymmetric sequence tracking vs. competitive price tiers
select customerid, orderid, freight,
       row_number() over(partition by customerid order by freight) as row_num,
       rank() over(partition by customerid order by freight desc) as rank_desc
from orders;

-- 4.2 Chronological Interval Engine: Tracking preceding and succeeding data points
-- Essential for calculating kinetic time deltas across longitudinal research profiles
select customerid, orderid, orderdate,
       lag(orderdate, 1) over(partition by customerid order by orderdate) as prev_order_date,
       lead(orderdate, 1) over(partition by customerid order by orderdate) as next_order_date
from orders
order by customerid, orderdate;