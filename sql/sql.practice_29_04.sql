/*
SQL ANALYTICAL RANKING & MULTI-LAYERED PARTITIONING - DAY 15
Focus: ROW_NUMBER() Ranking, Partitioned Aggregates, and CTE Data Stratification
Project: Global Sales Auditing and Categorical Product Benchmarking
*/

-- ==========================================
-- SECTION 1: TRANSACTIONAL BENCHMARKING
-- ==========================================

-- 1.1 Scalar Benchmarking: Products exceeding Category 1 maximum price
select * from products
where price > (select max(price) from products where categoryid = 1);

-- 1.2 Regional Precision: Targeted Paris Customer Segment
select sub.* from(
    select * from customers
    where country = 'France'
) sub
where sub.city = 'Paris';

-- 1.3 High-Frequency Monthly Orders: Customers with > 2 orders per month
select sub.customerid, sub.total_orders
from(
    select customerid, 
           count(orderid) as total_orders, 
           month(orderdate) as order_month
    from orders
    group by customerid, month(orderdate)
) sub
having sub.total_orders > 2;

-- ==========================================
-- SECTION 2: RELATIONAL INTEGRATION & SETS
-- ==========================================

-- 2.1 Luxury Tier Mapping: Joining with Top 3 price outliers
select sub.* from products
join (
    select price from products
    order by price desc
    limit 3
) sub on products.price = sub.price;

-- 2.2 Loyalty Volume: Linking orders with Customer-wide Order Totals
select orders.*, sub.total_orders from orders
join(
    select customerid, 
           count(orderid) as total_orders
    from orders
    group by customerid
) sub on orders.customerid = sub.customerid
order by total_orders desc;

-- 2.3 Comprehensive Entity Registry: Unified Suppliers and Customers
select suppliername, country from suppliers
union all
select customername, country from customers
order by country;

-- ==========================================
-- SECTION 3: COMMON TABLE EXPRESSIONS (CTEs)
-- ==========================================

-- 3.1 Modular Geographic Filter: Portland, USA Segment
with country_customers as(
    select * from customers
    where country = 'USA'
)
select * from country_customers
where city = 'Portland';

-- ==========================================
-- SECTION 4: ANALYTICAL WINDOWING (SUM & ROW_NUMBER)
-- ==========================================

-- 4.1 Categorical Cumulative Pricing: Partitioned Running Totals
select categoryid, price,
       sum(price) over(partition by categoryid order by price) as running_total 
from products;

-- 4.2 Categorical Ranking: Descending Row Numbers by Price
select categoryid, productname, price,
       row_number() over(partition by categoryid order by price desc)
from products;

-- 4.3 Global Pricing Rank: Ascending Row Numbers
SELECT productname, price,
       row_number() over(order by price ) as row_num
from products;

-- 4.4 Stratified Ranking: Categorical Ascending Order
select categoryid, productname, price,
       row_number() over(partition by categoryid order by price) as row_num
from products;

-- 4.5 Filtered Analytical Rank: Category 1 Price Order
select productname, price,
       row_number() over(order by price)
from products
where categoryid = 1;

-- 4.6 Chronological Sequence: Global Order History (Newest First)
select customerid, orderid, orderdate,
       row_number