SELECT *
FROM(
	SELECT nombre, apellido, COUNT(nombre) AS a1, COUNT(apellido) AS apellido_repetido 
	FROM platzi.alumnos
	GROUP BY nombre, apellido
	ORDER BY a1 DESC, apellido_repetido DESC
) AS test 

WHERE a1 >=2 and apellido_repetido >=2;

SELECT(platzi.alumnos.nombre,platzi.alumnos.apellido)::text, COUNT(*) AS cuenta
FROM platzi.alumnos
GROUP BY platzi.alumnos.nombre, platzi.alumnos.apellido
HAVING COUNT(*) > 1;

SELECT *
FROM (
	SELECT id,
	ROW_NUMBER() OVER(
		PARTITION BY
			nombre,
			apellido,
			email,
			colegiatura,
			fecha_incorporacion,
			carrera_id,
			tutor_id
		ORDER BY id ASC
	) AS row,
	*
	FROM platzi.alumnos
) AS duplicados

WHERE duplicados.row >1;

/*RETO: Utilizar el query anterior para ahora borrar los duplciados de la tabla*/

DELETE FROM platzi.alumnos
WHERE id IN(
SELECT alumnos.id
FROM (
	SELECT id,
	ROW_NUMBER() OVER(
		PARTITION BY
			nombre,
			apellido,
			email,
			colegiatura,
			fecha_incorporacion,
			carrera_id,
			tutor_id
		ORDER BY id ASC
	) AS row,
	FROM platzi.alumnos
) AS duplicados

WHERE duplicados.row >1
);
