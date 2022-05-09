SELECT a.nombre,a.apellido, t.nombre, t.apellido
FROM platzi.alumnos AS a
INNER JOIN platzi.alumnos AS t
ON a.id = t.tutor_id;

SELECT CONCAT (a.nombre, ' ', a.apellido) AS alumno,
	CONCAT(t.nombre, ' ', t.apellido) AS tutor
FROM platzi.alumnos AS a
INNER JOIN platzi.alumnos AS t
ON a.id = t.tutor_id;

SELECT CONCAT (a.nombre, ' ', a.apellido) AS tutor,
	COUNT (*) AS alumnos_por_tutor
FROM platzi.alumnos AS a
INNER JOIN platzi.alumnos AS t
ON a.id = t.tutor_id
GROUP BY tutor
ORDER BY alumnos_por_tutor DESC
LIMIT 10;

/* RETO: Sacar el promedio de alumnos por tutor */

SELECT AVG(test)
FROM(
	SELECT CONCAT (al.nombre,' ', al.apellido) AS tutor,  COUNT(*) AS test
	FROM platzi.alumnos as al
	INNER JOIN platzi.alumnos as ab
	ON al.id =ab.tutor_id
	GROUP BY tutor
	
)AS test

/*Reto Personal: Promedio de tutorores por carrera*/

SELECT carrera, AVG(cantidad_tutorias_carrera) AS t
FROM (
	SELECT CONCAT(a1.carrera_id) AS carrera, COUNT(*) AS cantidad_tutorias_carrera
	FROM platzi.alumnos AS a1
	INNER JOIN platzi.alumnos AS a2
	ON a1.id = a2.tutor_id
	GROUP BY carrera
	ORDER BY carrera ASC
) AS calculo
GROUP BY carrera
ORDER BY t ASC;
