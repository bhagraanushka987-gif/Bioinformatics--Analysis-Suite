-- --- TASK 6: IDENTIFYING POWER USERS ---
-- Goal: Find customers who have placed more than 3 orders.
-- Logic: Uses GROUP BY with a HAVING clause to filter on the count.

SELECT customerid, count(orders.orderid) 
FROM orders
GROUP BY customerid
HAVING count(orders.orderid) > 3;

-- ----------------------------------------------------------

-- --- TASK 7: CATEGORY PRICE ANALYSIS ---
-- Goal: Calculate average product price per category.
-- Logic: Groups by category and sorts results from highest to lowest price.

SELECT categoryid, avg(price) 
FROM products
GROUP BY categoryid
ORDER BY avg(price) DESC;