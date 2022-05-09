/* LEFT JOIN EXCLUSIVE*/
SELECT a.nombre, a.apellido, a.carrera_id, c.id, c.carrera
FROM platzi.alumnos AS a
LEFT JOIN platzi.carreras AS c
ON a.carrera_id = c.id
WHERE c.id IS NULL;

/* LEFT JOIN INCLUSIVE*/
SELECT a.nombre, a.apellido, a.carrera_id, c.id, c.carrera
FROM platzi.alumnos AS a
LEFT JOIN platzi.carreras AS c
ON a.carrera_id = c.id

/*RIGHT JOIN INCLUSIVE*/
SELECT a.nombre, a.apellido, a.carrera_id, c.id, c.carrera
FROM platzi.alumnos AS a
RIGHT JOIN platzi.carreras AS c
ON a.carrera_id = c.id

/*RIGHT JOIN EXCLUSIVE*/
SELECT a.nombre, a.apellido, a.carrera_id, c.id, c.carrera
FROM platzi.alumnos AS a
RIGHT JOIN platzi.carreras AS c
ON a.carrera_id = c.id
WHERE a.id IS NULL;

/* INNER JOIN*/

SELECT a.nombre, a.apellido, a.carrera_id, c.id, c.carrera
FROM platzi.alumnos AS a
JOIN platzi.carreras AS c
ON a.carrera_id = c.id

/* OUTER EXCLUSIVE JOIN*/
SELECT a.nombre, a.apellido, a.carrera_id, c.id, c.carrera
FROM platzi.alumnos AS a
FULL OUTER JOIN  platzi.carreras AS c
ON a.carrera_id = c.id
WHERE a.id IS NULL OR C.id IS NULL;