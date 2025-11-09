# Write your MySQL query statement below

-- select coalesce(salary,null) as SecondHighestSalary from
--     (select salary,dense_rank() over (order by salary desc) SecondHighestSalary
--     from employee)t
-- where SecondHighestSalary=2;

-- select ( 
--     select salary
--     from employee 
--     order by salary desc 
--     limit 1 offset 1) SecondHighestSalary 

-- select max(salary) as SecondHighestSalary from employee
-- where salary<(select max(salary) from employee)

select max(e2.salary) SecondHighestSalary 
from employee e1,employee e2
where e1.salary>e2.salary
