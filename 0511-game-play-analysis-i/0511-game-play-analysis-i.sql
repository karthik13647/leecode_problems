# Write your MySQL query statement below
-- select distinct player_id,event_date as first_login
-- from activity
-- group by player_id
-- order by event_date desc;

select player_id,event_date first_login
from(
    select *,
    dense_rank() over (partition by player_id order by event_date asc) orde
    from activity
)t 
where orde=1;