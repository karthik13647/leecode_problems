# Write your MySQL query statement below
select b.book_id,b.title,b.author,b.genre,b.publication_year,b.total_copies current_borrowers
from library_books b
join borrowing_records r
on b.book_id=r.book_id
where r.return_date is null
group by b.book_id
having count(*)=b.total_copies
order by current_borrowers desc,title asc;