DELETE from jugadores where ID =1;

UPDATE jugadores
set nacionalidad = 'colombia'
where id = 1 OR id = 2
LIMIT 1;

UPDATE tabla
SET active = 0
where client_id IN (1,2,3,4,5)