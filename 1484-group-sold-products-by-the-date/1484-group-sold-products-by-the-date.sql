# Write your MySQL query statement below
select sell_date,count(distinct product) as num_sold,group_concat(distinct product) as products 
from activities 
group by sell_date;

-- this is foor the sql server.
-- select sell_date, count(product) as 'num_sold', string_agg(product, ',') as products
-- from
-- (
--     select distinct *
--     from Activities
-- ) t
-- group by sell_date