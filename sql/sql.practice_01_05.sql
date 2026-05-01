/*
SQL SEQUENTIAL DIFFERENCE MAPPING & LEAD/LAG ANALYSIS - DAY 17
Focus: LAG() and LEAD() offsets, Price Difference Calculation, and Partitioned Windows
Project: Market Pricing Volatility and Global Customer Order Density
*/

-- ==========================================
-- SECTION 1: BENCHMARKING & TEMPORAL FILTERS
-- ==========================================

-- 1.1 Category Benchmarking: Items exceeding Category 2 average
select * from products
where price > (select avg(price) from products where categoryid = 2);

-- 1.2 Subquery Stratification: Tracking 'HANAR' activity in 1996
select sub.* 
from( 
    select * from orders
    where year(orderdate) = 1996
)sub
where sub.customerid = 'HANAR';

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

-- 2.1 Value Tier Mapping: Joining with the 3 lowest-priced products
select sub.* from products
join(
    select price from products
    order by price
    limit 3
)sub on products.price = sub.price;

-- 2.2 Demographic Density: Customers linked with Country-wide Population Totals
select customers.*, sub.total_in_country from customers
join(
    select country, 
           count(customername) as total_in_country
    from customers
    group by country 
) sub on customers.country = sub.country
order by sub.total_in_country desc;

-- 2.3 Global Entity Registry: Unified Suppliers and Customers (Including Duplicates)
select suppliername, city from suppliers
union all
select customername, city from customers
order by city;

-- ==========================================
-- SECTION 3: COMMON TABLE EXPRESSIONS (CTEs)
-- ==========================================

-- 3.1 Temporal Filter: Isolating 'ERNSH' transactions in 1997
with year_orderdate as(
    select * from orders
    where year(orderdate) = 1997
)
select * from year_orderdate
where customerid = 'ERNSH';

-- ==========================================
-- SECTION 4: ADVANCED WINDOWING & OFFSET FUNCTIONS
-- ==========================================

-- 4.1 Categorical Stats: Simultaneous Mean and Running Totals
select categoryid, productname, price,
       avg(price) over(partition by categoryid) as mean_price,
       sum(price) over(partition by categoryid order by price) as running_total
from products;

-- 4.2 Categorical Ranking: Sequence identification within categories
select categoryid, productname, price,
       row_number() over(partition by categoryid order by price )
from products;

-- 4.3 Global Competitive Rank: Price-based Leadership
select productname, price,
       rank() over(order by price desc)
from products;

-- 4.4 Sequential Comparisons: Visualizing Previous and Next pricing
select productname, price, 
       lag(price, 1) over(order by price),
       lead(price, 1) over(order by price)
from products;

-- 4.5 Forward Mapping: Identifying the immediate 'Next Price'
SELECT productname, price, 
       lead(price, 1) over(order by price) as next_price;

-- 4.6 Full Context Mapping: Comparative Price Environment
select productname, price,
       lag(price, 1) over(order by price) as prev_price,
       lead(price, 1) over(order by price) as next_price
from products;

-- 4.7 Partitioned Comparative Mapping: Previous price within Category
select categoryid, productname, price,
       lag(price, 1) over(partition by categoryid order by price) as prev_price
from products;

-- 4.8 Delta Calculation: Quantifying the exact price difference between rows
select productname, price,
       price - lag(price, 1) over(order by price) as price_diff
from products;