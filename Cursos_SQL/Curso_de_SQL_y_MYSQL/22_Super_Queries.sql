SELECT count (book_id),
sum(if(year <1950, 1, 0)) as 'MENOR 1950',
sum(if(year <1950 and year <2000, 1, 0)) as 'MAYOR 1950 pero menor 2000'
from books as b
join authors as a ON a.author_id = b.author_id
where a.nationality is not null
group  by a.nationality; 