select count()* from books;
SELECT * from authors where author_id > 0 and author_id <=5;
SELECT * from books where author_id between 1 and 5;

SELECT b.book_id, a.name, b.title
From books as b
inner join authors as a
ON a-author_id = b.author_id
where a.author_id between 1 and 5;

SELECT e.Nombre, e.ciudad,group_concat(l.nombre) as 'Torneos que juegan'
from equipos as e
INNER JOIN ligas_equipos ON ligas_equipos.equipos_id = e.id
INNER JOIN ligas as l ON l.ID = ligas_equipos.liga_id
group by e.nombre;

SELECT c.name, b.title, t.type
FROM transactions as t
INNER JOIN books as b on t.book_id = b.book_id
INNER JOIN clients as c on t.client_id = c.client_id
INNER JOIN authors as a on b-auhtor_id = a.author_id
WHERE c.gender = 'F' and t.type IN = ('sell', 'lend');