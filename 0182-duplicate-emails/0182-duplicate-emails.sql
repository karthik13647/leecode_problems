# Write your MySQL query statement below
select distinct email as Email
 from(
    select *,
        count(*) over(partition by email) as ranks
    from person
)t
where ranks>=2;
