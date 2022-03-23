select a.author_id, a.name, a.nationality, b.title
from authors as a
join books as b on author_id = a.author_id
where a.author_id between 1 and 5
order by a.author_id;

select a.author_id, a.name, a.nationality, b.title
from authors as a
left join books as b on author_id = a.author_id
where a.author_id between 1 and 5
order by a.author_id;

SELECT *, count(jugadores.id_equipos) AS jugadores_por_equipo, group_concat(jugadores.Nombre, " ", jugadores.Apellido) AS jugadores_en_el_equipo
FROM equipos
INNER JOIN jugadores ON equipos.ID = jugadores.id_equipos
GROUP BY equipos.ID
ORDER BY jugadores_por_equipo DESC;

select a.author_id, a.name, a.nationality, COUNT(b.book_id)
from authors as a
left join books as b on author_id = a.author_id
where a.author_id between 1 and 5
GOUPR BY a.author_id
order by a.author_id;