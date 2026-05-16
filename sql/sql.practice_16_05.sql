/*
SQL POSITIONAL OFFSETS & COMPREHENSIVE BENCHMARKING - DAY 32
Focus: Relative Window Offsets (Lead/Lag), Dynamic Join Bounds, and Partitioned Slicing
Project: Global Logistics Operations and Categorical Value Layering
*/

-- ==========================================
-- SECTION 1: BENCHMARKING & REGIONAL FILTERS
-- ==========================================

-- 1.1 Price Floor Evaluation: Slicing items below Category 1 baseline minimum
select * from products
where price < (Select min(price) from products where categoryid = 1);

-- 1.2 Geolocation Stratification: Subquery separation for São Paulo entries
select sub.* from(
    select * from customers
    where country = 'Brazil'
)sub
where sub.city = 'São Paulo';

-- 1.3 High-Value Categorical Auditing: Grouped segments exceeding 25 average units
select sub.categoryid, sub.average_price
from(
    select categoryid, 
           avg(price) as average_price,
           sum(price) as total_price
    from products
    group by categoryid
)sub
having sub.average_price > 25;

-- ==========================================
-- SECTION 2: RELATIONAL INTEGRATION & SETS
-- ==========================================

-- 2.1 Boundary Value Integration: Joining records with the Top 4 premium price tiers
select sub.* from products
join(
    select price from products
    order by price desc
    limit 4
)sub on products.price = sub.price;

-- 2.2 Entity Volume Overlap: Orders bound to sorted client transactional counts
select orders.*, sub.total_orders from orders
join(
    select customerid, 
           count(orderid) as total_orders
    from orders
    group by customerid
    order by count(orderid) desc
)sub on orders.customerid = sub.customerid;

-- 2.3 Unified Spatial Registry: All customer and supplier centers (retraining duplicates)
select city from customers
union all
select city from suppliers
order by city;

-- ==========================================
-- SECTION 3: COMMON TABLE EXPRESSIONS (CTEs)
-- ==========================================

-- 3.1 Isolated Sub-cohort Auditing: Luxury Category 1 entries
with all_products as(
    select * from products
    where price > 50
)
select * from all_products
where categoryid = 1;

-- ==========================================
-- SECTION 4: PARTITIONED WINDOW METRICS & OFFSETS
-- ==========================================

-- 4.1 Hybrid Analytical Ranking: Tracking continuous sequences vs. competitive ties
-- Note: Reversing your rank sort order to 'desc' aligns it perfectly with competitive grading
select categoryid, productname, price,
       row_number() over(partition by categoryid order by price),
       rank() over(partition by categoryid order by price desc)
from products;

--