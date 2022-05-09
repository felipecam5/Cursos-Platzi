SELECT carrera_id, MAX(fecha_incorporacion)
FROM platzi.alumnos
GROUP BY carrera_id
ORDER BY carrera_id;

SELECT DISTINCT (carrera_id), MAX(fecha_incorporacion) AS tst, array_agg((nombre, apellido)) AS st
FROM platzi.alumnos
GROUP BY carrera_id,fecha_incorporacion
ORDER BY carrera_id;

/* Reto Personal: El estudiante que se matriculó de ultimo en cada carrera*/

SELECT *
FROM(
	SELECT DISTINCT  MAX(fecha_incorporacion) as t, carrera_id
	FROM platzi.alumnos AS a1
	GROUP BY carrera_id
) AS seleccion 

INNER JOIN platzi.alumnos
ON seleccion.t = fecha_incorporacion
ORDER BY alumnos.carrera_id;

/* Reto Personal: El estudiante que se matriculó de ultimo en cada carrera*/

SELECT b1.nombre, b1.apellido, t, b1.carrera_id
FROM(
	SELECT DISTINCT  MAX(fecha_incorporacion) as t, carrera_id
	FROM platzi.alumnos AS a1
	GROUP BY carrera_id
) AS seleccion 

INNER JOIN platzi.alumnos as b1
ON seleccion.t = fecha_incorporacion
ORDER BY b1.carrera_id;