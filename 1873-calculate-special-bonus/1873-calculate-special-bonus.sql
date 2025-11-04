# Write your MySQL query statement below
select employee_id,
case
    when employee_id %2=0 then 0
    when name not like 'M%' then salary
    else 0
end as bonus
from employees
order by employee_id