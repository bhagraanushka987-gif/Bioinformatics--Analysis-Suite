/*
SQL COMPETITIVE RANKING & CATEGORICAL TIERING - DAY 16
Focus: RANK() vs. ROW_NUMBER(), Multi-Metric Windowing, and Subquery Benchmarking
Project: Global Market Leader Identification and Pharmaceutical Pricing Tiers
*/

-- ==========================================
-- SECTION 1: BENCHMARKING & TEMPORAL FILTERS
-- ==========================================

-- 1.1 Price Floor Detection: Items below Category 3 minimum price
select * from products
where price < (select min(price) from products where categoryid = 3);

-- 1.2 Temporal Precision: Analyzing 'QUICK' activity in 1997
select sub.*
from(
    select * from orders
    where year(orderdate) = 1997
) sub
where sub.customerid = 'QUICK';

-- 1.3 High-Value Segments: Categories exceeding 35 Mean Price
select sub.categoryid, sub.mean_price 
from(
    select categoryid,
           avg(price) as mean_price,
           count(price) as total_price
    from products
    group by categoryid
)sub
having sub.mean_price > 35;

-- ==========================================
-- SECTION 2: RELATIONAL DENSITY & SETS
-- ==========================================

-- 2.1 Regional Saturation: Joining with Top 3 highest-volume countries
select * from customers
join(
    select country from customers
    group by country
    order by count(customerid) desc
    limit 3
)sub on customers.country = sub.country;

-- 2.2 Inventory Proportionality: Linking items with Category density
select products.*, sub.total_in_category from products 
join(
    select categoryid,
           count(productid) as total_in_category
    from products
    group by categoryid
)sub on products.categoryid = sub.categoryid
order by sub.total_in_category desc;

-- 2.3 Unified Geographic Map: Global Supplier and Customer Cities
select city from customers
union 
select city from suppliers
order by city;

-- ==========================================
-- SECTION 3: COMMON TABLE EXPRESSIONS (CTEs)
-- ==========================================

-- 3.1 Luxury Tier Filtering: Category 1 items > 40
with products_price as(
    select * from products
    where price > 40
)
select * from products_price
where categoryid = 1;

-- ==========================================
-- SECTION 4: WINDOW FUNCTIONS (AGGREGATES & RANKING)
-- ==========================================

-- 4.1 Statistical Windowing: Count, Running Total, and Average by Category
select categoryid, productname, price,
       count(productid) over (partition by categoryid) as count,
       sum(price) over(partition by categoryid order by price) as running_total,
       avg(price) over(partition by categoryid) as avg_price
from products;

-- 4.2 Sequential Categorical Order: Partitioned Row Numbers
select categoryid, productname, price,
       row_number() over(partition by categoryid order by price desc) as row_num
from products;

-- 4.3 Global Competitive Rank: Price-based Leadership (Descending)
select productname, price,
       rank() over(order by price desc) 
from products;

-- 4.4 Replication: Global Competitive Rank Check
SELECT productname, price, 
       rank() over(order by price desc)
from products;

-- 4.5 Tiered Competitive Rank: Categorical Price Leadership
select categoryid, productname, price,
       rank() over(partition by categoryid order by price desc)
from products;

-- 4.6 Targeted Competitive Rank: Category 2 Pricing Hierarchy
select productname, price,
       rank() over(order by price)
from products
where categoryid = 2;

-- 4.7 Comparative Ranking: Row Number vs. Competitive Rank
-- Visualizing the gap between sequential and competitive ordering
select productname, price,
       row_number() over(order by price desc) as row_num,
       rank() over(order by price desc) as rank 
from products;