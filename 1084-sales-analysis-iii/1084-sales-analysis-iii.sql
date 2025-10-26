# Write your MySQL query statement below
-- select p.product_id,p.product_name
-- from product p 
-- join sales s
-- on p.product_id=s.product_id
-- group by p.product_id
-- having min(s.sale_date)>=cast('2019-01-01' as date) and 
--         max(s.sale_date)<=cast('2019-03-01' as date);
SELECT product_id, product_name 
FROM Product 
WHERE product_id IN
(SELECT product_id
FROM Sales
GROUP BY product_id
HAVING MIN(sale_date) >= '2019-01-01' AND MAX(sale_date) <= '2019-03-31')