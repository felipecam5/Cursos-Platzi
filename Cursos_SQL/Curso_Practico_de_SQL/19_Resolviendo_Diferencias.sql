SELECT carrera_id, COUNT(*) AS cuenta
FROM platzi.alumnos
GROUP BY carrera_id
ORDER BY cuenta DESC;

SELECT a.nombre, a.apellido, a.carrera_id, c.id, c.carrera
FROM platzi.alumnos AS a
LEFT JOIN platzi.carreras AS c
ON a.carrera_id = c.id
WHERE c.id IS NULL
ORDER BY a.carrera_id;

/*RETO: Left Join pero sin excluir gente*/

SELECT carrera_id, COUNT(*) AS cuenta
FROM platzi.alumnos
GROUP BY carrera_id
ORDER BY cuenta DESC;

SELECT a.nombre, a.apellido, a.carrera_id, c.id, c.carrera
FROM platzi.alumnos AS a
FULL OUTER JOIN platzi.carreras AS c
ON a.carrera_id = c.id
ORDER BY a.carrera_id;