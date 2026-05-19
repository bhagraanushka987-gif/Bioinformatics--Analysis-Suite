/*
SQL CHRONOLOGICAL SEQUENCE ANALYSIS & WINDOW AUDITS - DAY 34
Focus: Chronological Lead-Lag Offsets, Top-N Volume Filtering, and Set Unification
Project: Corporate Human Capital Analytics, Inventory Optimization, and Global Logistics Lanes
*/

-- ==========================================
-- SECTION 1: STATISTICAL BENCHMARKING & SCALS
-- ==========================================

-- 1.1 Outlier Identification: Isolating personnel earning above the global average salary
select * from employees
where salary > (select avg(salary) from employees);

-- 1.2 Inventory Segment Stratification: Subquery filtering for Supplier 2 active stock
select sub.*
from(
    select * from products
    where unitunstock > 10
) sub
where sub.supplierid = 2;

-- 1.3 High-Throughput Asset Slicing: Products exceeding 100 cumulative units
select sub.productid, sub.total_quantity
from(
    select productid, 
           sum(quantity) as total_quantity,
           avg(price) as average_unit_price
    from orders
    group by productid
) sub
where sub.total_quantity > 100;

-- ==========================================
-- SECTION 2: RELATIONAL INTEGRATION & JUXTAPOSITION
-- ==========================================

-- 2.1 Top-N Volume Filtering: Restricting customer profiles to the Top 10 buyers
select customers.* from customers
join(
    select customerid, 
           count(orderid) as total_orders
    from orders
    group by customerid
    order by count(orderid) desc
    limit 10
) sub on customers.customerid = sub.customerid;

-- 2.2 Inventory Density Mapping: Linking items with transaction line counts
select products.productid, products.productname, sub.order_count from products
join(
    select productid, 
           count(*) as order_count 
    from orderdetails
    group by productid
) sub on products.productid = sub.productid
order by sub.order_count desc;

-- 2.3 Set Unification (Deduplicated): Comprehensive unique corporate entities
select companyname from customers
union
select companyname from suppliers
order by companyname;

-- ==========================================
-- SECTION 3: COMMON TABLE EXPRESSIONS (CTEs)
-- ==========================================

-- 3.1 Modular Geographic Filter: Targeted French logistic distribution lanes
with all_orders as(
    select * from orders
    where shipcountry = 'France'
)
select * from all_orders
where freight > 50;

-- ==========================================
-- SECTION 4: POSITION WINDOW METRICS & OFFSETS
-- ==========================================

-- 4.1 Divergent Scale Ranking: Asymmetric baseline sequencing vs. competitive luxury tiers
select productid, productname, unitprice,
       row_number () over(order by unitprice) as row_num,
       rank() over(order by unitprice desc) as rank_num
from products;

-- 4.2 Chronological Interval Engine: Tracking preceding and succeeding hiring steps
-- Essential for calculating kinetic delta timelines across longitudinal research profiles
select employeeid, lastname, hiredate,
       lag(hiredate, 1) over(order by hiredate) as previous_hire_date,
       lead(hiredate, 1) over(order by hiredate) as next_hire_date
from employees
order by hiredate;